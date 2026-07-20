#!/usr/bin/env python3
"""Second-round semantic quality gate for Qwen3 4B.

This gate was added after human review of the first green run found that a future
Success Plan target was phrased as completed and CSS workflow education was
incorrectly assigned to the CSM in Next Steps.
"""
from __future__ import annotations

import json
import os
import sys
import time
import urllib.request
from pathlib import Path

URL = os.environ.get("CDKGENAI_AI_URL", "http://127.0.0.1:8080/v1/chat/completions")
MODEL = os.environ.get("CDKGENAI_MODEL", "qwen3-4b")
OUT = Path(os.environ.get("CDKGENAI_VALIDATION_OUT", "validation-results"))
OUT.mkdir(parents=True, exist_ok=True)

SYSTEM = """You are the built-in CDKGenAI assistant for Customer Success Managers. Use only supplied source facts. Do not turn goals into completed results. Do not add unsupported business outcomes. Keep CSS and CSM responsibilities distinct: CSS provides workflow education and recommendations; the CSM coordinates, documents, and follows up. Follow the requested headings exactly. Return concise, copy-ready content."""


def chat(prompt: str, limit: int = 700) -> tuple[str, float]:
    body = {
        "model": MODEL,
        "messages": [{"role": "system", "content": SYSTEM}, {"role": "user", "content": prompt}],
        "temperature": 0.1,
        "top_p": 0.9,
        "max_tokens": limit,
        "stream": False,
        "chat_template_kwargs": {"enable_thinking": False},
    }
    request = urllib.request.Request(URL, data=json.dumps(body).encode(), headers={"Content-Type": "application/json"})
    started = time.time()
    with urllib.request.urlopen(request, timeout=300) as response:
        answer = json.loads(response.read().decode())["choices"][0]["message"]["content"].strip()
    return answer, round(time.time() - started, 3)


def section(text: str, heading: str, next_heading: str | None = None) -> str:
    upper = text.upper()
    start = upper.find(heading.upper())
    if start < 0:
        return ""
    start += len(heading)
    if next_heading:
        end = upper.find(next_heading.upper(), start)
        if end >= 0:
            return text[start:end]
    return text[start:]


def main() -> int:
    results = []

    success_prompt = """WORKFLOW: CREATE A FULL SUCCESS PLAN
Required headings: ACCOUNT OBJECTIVE, BUSINESS OUTCOME, CURRENT STATE, MILESTONES, OWNERS, RISKS, NEXT STEPS.
SOURCE FACTS: Northstar Automotive currently uses mobile check-in on 38% of eligible repair orders. The agreed goal is 70% by October 31, 2026. The Service Manager owns daily coaching. The CSM owns a virtual workflow review by August 15, 2026. A risk is inconsistent advisor adoption. No financial impact, customer-satisfaction result, efficiency result, or completed outcome has been documented.
RULES: Describe October 31 as a future target, not an achieved result. BUSINESS OUTCOME may state only improved consistency and adoption of the mobile check-in workflow. Build the copy-ready Success Plan."""
    answer, seconds = chat(success_prompt)
    low = answer.lower()
    success_checks = {
        "all_headings": all(h.lower() in low for h in ["ACCOUNT OBJECTIVE", "BUSINESS OUTCOME", "CURRENT STATE", "MILESTONES", "OWNERS", "RISKS", "NEXT STEPS"]),
        "facts_preserved": all(v.lower() in low for v in ["38%", "70%", "October 31, 2026", "August 15, 2026"]),
        "future_target_not_completed": "70% mobile check-in usage achieved" not in low and "target achieved" not in low and "goal achieved" not in low,
        "no_unsupported_outcomes": all(v not in low for v in ["customer satisfaction", "revenue", "financial impact", "streamlined operations"]),
        "approved_outcome_language": "consistency" in section(answer, "BUSINESS OUTCOME", "CURRENT STATE").lower() and "adoption" in section(answer, "BUSINESS OUTCOME", "CURRENT STATE").lower(),
    }
    results.append({"id": "success_plan_semantic_roles", "passed": all(success_checks.values()), "seconds": seconds, "checks": success_checks, "answer": answer})

    css_prompt = """WORKFLOW: STANDARD CSS REQUEST
Required headings: DEALER, REQUEST, CURRENT WORKFLOW, BUSINESS NEED, DESIRED CSS ENGAGEMENT, CSM ACTIONS COMPLETED, NEXT STEPS.
SOURCE FACTS: Blue Ridge Motors is moving A/R from Balance Forward to Open Item on September 1, 2026. The accounting team needs workflow education and clarification about in-house check printing. CSS should provide workflow education and recommended next steps. CSS is not being asked to configure or implement anything. The CSM reviewed the concern and documented the questions.
ROLE RULES: In NEXT STEPS, CSS owns providing workflow education and recommendations. The CSM may coordinate scheduling and follow up, but must not be assigned to provide the workflow education. Create the request."""
    answer, seconds = chat(css_prompt)
    low = answer.lower()
    next_steps = section(answer, "NEXT STEPS").lower()
    css_checks = {
        "all_headings": all(h.lower() in low for h in ["DEALER", "REQUEST", "CURRENT WORKFLOW", "BUSINESS NEED", "DESIRED CSS ENGAGEMENT", "CSM ACTIONS COMPLETED", "NEXT STEPS"]),
        "facts_preserved": all(v.lower() in low for v in ["Blue Ridge Motors", "Balance Forward", "Open Item", "September 1, 2026", "in-house check printing"]),
        "css_owns_education": "css" in next_steps and "workflow education" in next_steps,
        "csm_not_education_owner": "csm will provide workflow education" not in next_steps and "csm to provide workflow education" not in next_steps,
        "no_configuration_commitment": "css will configure" not in low and "css will implement" not in low,
    }
    results.append({"id": "css_request_role_boundaries", "passed": all(css_checks.values()), "seconds": seconds, "checks": css_checks, "answer": answer})

    passed = sum(1 for result in results if result["passed"])
    report = {"model": MODEL, "passed": passed, "total": len(results), "gate": "PASS" if passed == len(results) else "BLOCKED", "results": results}
    (OUT / "qwen3-4b-quality-round2.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    print(json.dumps({"gate": report["gate"], "passed": passed, "total": len(results)}, indent=2))
    return 0 if report["gate"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())

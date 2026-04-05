CDKXGen
AI Prompt Generator for CDK Global Customer Success Managers
CDKXGen is a single file HTML tool that generates structured, AI ready prompts for every CSM workflow: success planning, touchpoints, support cases, executive business reviews, escalations, adoption analysis, renewal strategy, and more. Built for teams that push to Microsoft Copilot and paste into Totango or Salesforce.
Current Version: 4.0 (April 5, 2026)
---
What It Does
CDKXGen takes your meeting notes, call transcripts, or account context and transforms them into structured prompts optimized for AI engines. Select a category, pick a command, paste your notes, and click Build for AI. The generated prompt tells the AI exactly what to produce, in what format, with what structure, so the response comes back ready to paste into your CRM.
The workflow:
Select a category and command
Enter the account name and paste your notes
Choose a CRM Output Mode (Totango Touchpoint, Salesforce Case, etc.)
Click Build for AI
Push to Copilot (copies prompt to clipboard, opens Copilot)
Paste the AI response into the Response Workspace
Parse into sections and copy each field into your CRM
---
Features
Prompt Generation
63 commands across 23 categories covering the full CSM lifecycle
Categories grouped into Planning, Day to Day, Reviews, Adoption and Renewal, Risk and Transitions, and Support
Output Style selector (Standard, Headings + Bullets, Bullets Only)
Detail Level selector (Standard, Short, Detailed)
Command search with real time filtering
Favorites and Recently Used panels for quick access
CRM Integration
CRM Output Mode: Tells the AI to format responses for Totango Touchpoint, Totango Success Plan, Salesforce Case, or Salesforce Activity with matching section headers
AI Response Workspace: Paste AI output, click Parse into Sections, get individual Copy buttons per CRM field
Quick Paste Strips: One click clipboard copy for frequently pasted text (CSS tags, status phrases, closing lines). Fully customizable.
Copilot Integration
Push to Copilot: Copies prompt to clipboard and opens Copilot in a new tab
Copilot Persona Injection: A persistent persona block automatically prepends to every prompt, ensuring consistent output format (plain text, ALL CAPS headers, no markdown)
Account Management
Your Dealers Panel: Save dealers, stores, and Points of Contact (POC) with name, role, phone, and email. One click Insert populates prompt fields.
Dealer group hierarchy with collapsible UI
Assign POCs across multiple stores
Auto save prompt for new account names
Export
Export to AI (.txt file)
Export to CSM AI Notetaker (.docx)
Push to Copilot
Other
Dark and Light theme
English and French language support
LOB / Product / Sub Product cascading selectors for support cases
localStorage persistence across sessions
Fully offline capable (single HTML file, no server required)
---
Categories and Commands (63 total)
Planning (13 commands)
Category	Commands
Success Plan	Create a Full Success Plan, Update Success Plan
Success Plan Hurts	Key Hurts & Focus Areas
Objectives	Objectives with Description and Milestones
Milestones	Milestone Objective Plan
Generic	Success Plan (Sales), Success Plan (Service), Success Plan (Parts), Success Plan (Accounting), Quick Win Identifier
Onsite	Training Agenda, Renewal Agenda, Discovery Agenda, EBR Agenda, Multi Rooftop Rollout Planner
Day to Day (17 commands)
Category	Commands
Check In	Notes (Structured), Recap (Executive)
Touchpoints	Email, Internal Note, Phone Call (Connected), Phone Call (Left Message), Text Message, Virtual Meeting, Visit, Executive Summary
Training Recap	Training Recap
Email Response	Create Email Response to Dealer, Rewrite Email Response
Call Prep	Pre Call Prep Brief, Pre Call Talk Track
Internal Comms	ASE Account Update, CSS Warm Handoff Message, Manager Escalation Note, Cross Functional Ask
Reviews (7 commands)
Category	Commands
Executive Business Review	Account Team Slide, Delivered Recap, Review (Usage, Objectives & Milestones)
QBR Prep / Internal Strategy	Pre EBR Strategy Brief, Talk Track Builder, SWOT Dealer Account Analysis
Adoption and Renewal (4 commands)
Category	Commands
Adoption	Adoption Scorecard, Adoption Gap Analysis
Renewal	Renewal Strategy Brief, Renewal Conversation Guide
Risk and Transitions (6 commands)
Category	Commands
Renewal / Retention Risk	Risk Assessment, Internal Action Plan
Account Transition / Handoff	Full Account Transition Document, Quick Transition Summary
Escalation Summary	Internal Handoff, Dealer Facing Communication
Support (16 commands)
Category	Commands
Support	Create a Support Case
CSS Request	Standard CSS Request, CSS Engagement Plan (Detailed), CSS Email to Dealer, Create a CSS Case
CSM Open Ended Questions	Discovery Follow Up, Service Discovery, Service Quick Call, Parts Discovery, Parts Quick Call, Accounting Discovery, Accounting Quick Call
---
Getting Started
Download `CDKXGen_v8.html`
Open it in any modern browser (Chrome, Edge, Firefox, Safari)
No installation, no server, no dependencies required
Everything runs locally in the browser
First Time Setup
Set your Copilot Persona: Expand the "Copilot Persona" panel and customize the default text, or leave it as is. Click Save Persona.
Add your dealers: Use the "Your Dealers" panel in the sidebar to save your accounts and POCs for one click insertion.
Add Quick Paste Strips: Expand "Add or manage strips" and add any text you paste into CRM fields frequently.
Select your CRM Output Mode: Choose your target CRM so AI responses come back pre formatted for your fields.
---
Technical Details
Architecture
Single file HTML application. All CSS, JavaScript, and prompt templates are embedded. No external dependencies at runtime. JSZip is loaded from CDN for .docx export only.
Data Storage
All user data is stored in the browser via localStorage:
Key	Purpose
`cdkxgen_state_v3`	Field values, selections, active category/command
`cdkxgen_favorites_v1`	Saved favorite commands
`cdkxgen_recent_v2`	Recently used commands
`cdkxgen_theme_v1`	Dark/Light theme preference
`cdkxgen_language_v1`	Language selection (en/fr)
`cdkxgen_dealers_v1`	Dealer and POC data
`cdkxgen_persona_v1`	Custom Copilot persona text
`cdkxgen_qps_v1`	Quick Paste Strips
Browser Support
Any modern browser with ES6+ and localStorage support. Tested on Chrome, Edge, and Firefox.
Offline Use
Fully functional offline after initial load. The only network dependency is JSZip CDN for .docx export, which can be cached by the browser.
---
Version History
Version	Date	Commands	Highlights
4.0 (v8)	April 5, 2026	63	CRM Output Mode, Response Workspace, Copilot Persona, Quick Paste Strips, SWOT, Call Prep, Internal Comms, Adoption, Renewal, type specific Touchpoints
3.1 (v7)	April 4, 2026	44	Push to Copilot, Dealer/POC Panel, French language, LOB selectors, Onsite category, Email Response, Touchpoint Type selector
2.2 (v6)	March 31, 2026	38	Core prompt engine, .docx export, favorites, search, theme toggle
---
License
Internal use only. CDK Global proprietary.

# Clocked Decision Experience | Project 2

## Purpose

Demonstrate Clocked as the central decision engine across Ticket Management, Asset Management, User Management, VoiceIQ, Bot Knowledge, Live Chat, Agent Studio and Bot Framework, while all modules reference a common synthetic dataset.

## What reviewers should see

**Input:** A user requests support from voice, chat, the portal or live chat.

**Understand:** Clocked interprets the task and loads the relevant user context, without forcing irrelevant asset questions.

**Compare:** Clocked checks configured ticket type descriptions, offering descriptions and synonyms, supported categories/subcategories and possible alternatives.

**Validate:** Clocked checks required fields, allowed catalog mappings, known assets, existing relevant tickets across channels, access rights and whether a clarifying question is needed.

**Recommend:** Clocked proposes an explainable next step: knowledge guidance, issue clarification, continuation of an existing ticket, a new ticket, or live chat. The user confirms meaningful actions.

**Execute:** In the future implementation, the responsible module performs the action after permission checks. In this mockup, execution is simulated and does not leave the browser.

## Key reference examples

### T003, DEMO001

Input: "My Dell computer is broken". The source workbook expects route `KNOWLEDGE_THEN_TICKETING`, ticket type `INC`, offering `INC001`, and clarification about laptop versus desktop and then model. DEMO001 owns AST001 Dell Latitude 5440, AST002 Dell OptiPlex 7010, and AST003 Dell Latitude 7440. Clocked should not pick one of these assets without clarification.

### Existing ticket across channels

Illustrative ticket INC1042 originates in Service Portal and is associated with DEMO001 and a Dell laptop. VoiceIQ offers to continue it or create a new one. On continuation, ask whether to add information or read the latest ticket status. The statuses and ticket records are mock extensions created for this demonstration.

### Unknown caller

An unrecognized number leads to collection of name and email. This does not automatically authorize access to an existing ticket or sensitive operations. The concept should withhold ticket details pending proper identity checks.

### Catalog overlap

Agent Studio calculates a simple token overlap percentage from the configured offering names and synonyms to illustrate ambiguous configurations. This is **not** a confidence probability, semantic classifier or validated overlap rate. A future real version should distinguish lexical coincidences from intent conflicts.

## Quality and safety rules

Use only mappings and fields present in the synthetic workbook for catalog choices. Do not imply real time status or real integrations. Keep the final action under the owning module and relevant permissions. Prefer transparent explanations over invented hidden reasoning. Do not automatically create tickets when knowledge resolves the request. Do not require an asset for software access simply because the utterance mentions a laptop. Keep all stakeholder feedback locally until it is explicitly exported or connected to a future feedback system.

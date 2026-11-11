# Clocked Studio | Project 2

A shareable, Figma style, interactive proof of concept of Clocked as the shared decision layer across Rezolve.ai service workflows.

This is **not a production system**. The interface is a deterministic, offline simulation. It makes proposed decision criteria visible so stakeholders can discuss the product vision without requiring live AI APIs, customer records, ticket systems, identity providers or telephony.

## The same synthetic dataset

The file `data.js` was generated from the workbook `Clocked_Smart_Service_Desk_Dataset.xlsx` used for the earlier Clocked Smart Service Desk GitHub project. It includes:

| Dataset | Records |
| --- | ---: |
| Users | 200 |
| Assets | 200 |
| Service offerings | 200 |
| Incident offerings | 15 |
| Categories | 200 |
| Subcategories | 260 |
| Offering to category mappings | 430 |
| Field rules | 268 |
| Demo test cases | 46 |

The workbook source is included under `source_data/` for comparison. All profiles and devices are fictional.

**Important distinction:** Sample tickets and knowledge article summaries added for the VoiceIQ and knowledge walkthroughs are explicitly *illustrative extensions*. They are not part of the source workbook. Ticket statuses, mock ticket IDs, channel provenance and knowledge summaries should not be mistaken for real data or imported rows.

## Experience

1. **Overview:** Eight connected module entry points and overall model.
2. **Decision Studio:** Select any of 46 original test cases or type a custom utterance. Step through understanding, comparison, validation, and a recommended next action. The inspector shows a transparent evidence summary.
3. **VoiceIQ Simulator:** Try a recognized or unknown caller, an existing ticket from another channel, adding information, checking status, clarification, or a new ticket. Unknown callers cannot see ticket matches without verification.
4. **Ticket Management:** Show selected ticket type, offering, permitted hierarchy, required fields and illustrative ticket records.
5. **Asset Management:** Browse the same 200 devices and highlight DEMO001's three Dell devices.
6. **User Management:** Browse the same 200 user profiles and change the selected user for all modules.
7. **Bot Knowledge:** Demonstrate evidence first guidance and appropriate escalation. The example articles are placeholders, not verified source text.
8. **Live Chat:** Prepare a simulated handoff with shared context; no agent contacted.
9. **Agent Studio:** Explore the 215 offerings, descriptions, phrases, catalog relationships, and calculated term overlap. The displayed percentage is **word overlap**, not model confidence or proof of misclassification.
10. **Bot Framework:** Show how the same user phrase receives shared classification regardless of the entry channel.
11. **Feedback:** Collect review notes locally in the browser, then export JSON for the team.

## Quick start

Open `index.html` in a modern browser. It loads `data.js`, `app.js` and `styles.css` from the same folder. No server installation or network connection is required. Alternatively, open the separate `clocked_project2_preview.html` file included with the delivery; it embeds everything in one file.

If local browser security settings prevent local files from opening, serve the folder from a local static server, e.g. `python -m http.server 8000`, then visit `http://localhost:8000`.

## GitHub and Vercel publishing

1. Create a new repository named `clocked-project-2` under the desired account.
2. Upload this project's files to the repository root, including `index.html`, `data.js`, `app.js`, `styles.css`, and `vercel.json`.
3. In Vercel, import the GitHub repository. Use a static project with the root directory set to the repository root. No build command, API key or environment variable is required.
4. Deploy, then check Overview, Decision Studio, T003, VoiceIQ continuation, Agent Studio, and Feedback.
5. Keep the project explicitly labelled as simulated and share it only with the intended audience.

Do not copy a production API key into the static site. Static JavaScript is visible to anyone with access to the page.

The connected GitHub access used to inspect the original repository was read only, so this delivery is a downloadable local project, not a pushed GitHub repository or confirmed Vercel deployment.

## Validation

`node --check app.js` checks syntax. `node test_logic.js` performs lightweight tests of the dataset, reference classification, multiple device matching, cross channel sample ticket match, and module rendering. Browser rendering was not validated in this workspace because the local browser navigation was blocked by the execution environment. Testing on the destination browser and published URL is still required.

## Design principle

Clocked shows **evidence, configured rules, candidate actions, uncertainty, and the final recommendation**. It does not expose or pretend to expose internal model thought traces. Owned modules retain authority over data, permissions, validation and the final action. In the actual product, the user confirms changes before any ticket creation or update.

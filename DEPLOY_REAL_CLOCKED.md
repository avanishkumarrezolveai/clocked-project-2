# Clocked Project 2: public demo using real Clocked API

## Requirements

This project uses the same `clocked-sdk==0.7.0` integration family as Project 1. The website is static, while `api/clocked.py` is a Vercel Python function that calls `decide` and `rerank`. All ticket actions and VoiceIQ interactions are demonstrations, not live systems.

## Deployment

1. Copy the full contents of this ZIP into your existing `clocked-project-2` GitHub repository, replacing older files. Commit and push to the main branch.
2. In Vercel Settings > Environment Variables, set **CLOCKED_API_KEY** to your real Clocked API key. Keep it secret and never put it in public JavaScript or GitHub files.
3. **DEMO_ACCESS_TOKEN is no longer required.** You may remove that old environment variable. The website does not prompt for an access code.
4. Redeploy the latest GitHub commit if Vercel does not automatically deploy it.
5. Open Decision Studio and click Run Clocked Decision. Confirm the inspector says REAL CLOCKED API and shows results for `decide` and `rerank`. An API ERROR is not a successful call.

## Important public access warning

There is no user authentication or access code on this version. Anyone who can reach `/api/clocked` can make your deployment incur Clocked API usage. The key itself remains server side, but an exposed API route can be abused. Before sharing widely, enable available Vercel Firewall rate limiting for `/api/clocked`, usage alerts or spending limits at the Clocked provider, and consider deployment authentication if needed. Application code does not implement durable distributed rate limiting.

## Validation

`node --check app.js`

`node test_logic.js`

`python -m py_compile api/clocked.py`

These tests cannot prove a live Clocked response without the real key and a successful deployed request.

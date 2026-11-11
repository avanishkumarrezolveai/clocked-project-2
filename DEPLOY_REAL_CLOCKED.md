# Project 2: Real Clocked SDK integration

This upgrade reuses Project 1 SDK version `clocked-sdk==0.7.0` and its `decide` and `rerank` method signatures, without copying the previous project's secret. All user profiles, catalog items, assets and sample tickets remain synthetic. Operational actions stay simulated.

## Set up on Vercel

1. Commit **all the files in this updated package** to your existing `clocked-project-2` repository, preserving `api/clocked.py` and root `requirements.txt`.
2. Import that repository into Vercel with Other preset and root directory `./`. No build command needed.
3. Under Vercel Environment Variables add **CLOCKED_API_KEY** with the real key as a secret value. Add **DEMO_ACCESS_TOKEN** with a separate strong reviewer access code. The access code is **not the API key**. Set for Production and Preview as needed.
4. Deploy or Redeploy. Open Decision Studio, enter the reviewer access code, then run a case.
5. Confirm inspector says `REAL CLOCKED API` and shows SDK `decide` and `rerank` results. A local fallback or API ERROR does not count as a successful live result.

Important: Vercel project is public. `DEMO_ACCESS_TOKEN` protects the paid API endpoint from casual anonymous use. Share this access code only with trusted reviewers. For stronger access control, use Vercel deployment protection and server side rate limiting. Never commit the Clocked key, put it in `data.js` or browser code, or share it in chat. Vercel will protect the key as long as it is only referenced by server code.

The Cloud function does not create real tickets, use a real asset CMDB, or connect to actual telephony. Only intent classification and offering relevance use the real SDK. Local fields and routing remain concept demonstrations.

## Verify

1. Check `https://YOUR_VERCEL_DOMAIN/api/clocked` with GET; it should not return a normal decision. It accepts POST requests only.
2. Without a reviewer access code the POST endpoint must return `401`.
3. With valid access it should return `source: REAL CLOCKED API` and structured SDK evidence.
4. Test the Dell T003 case and a service request such as Visio; check whether every suggested offering belongs to the catalog.
5. If the API errors, check Vercel Function Logs and verify SDK key and quota. Do not share secrets or raw authorization headers.

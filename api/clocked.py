"""Clocked Project 2 secure Vercel function. Synthetic catalog only.
Reuse the same clocked-sdk 0.7.0 endpoints as Project 1.
"""
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 18000


def error(message, status):
    response = jsonify({"source": "API ERROR", "error": message})
    response.status_code = status
    response.headers["Cache-Control"] = "no-store"
    return response


@app.route("/api/clocked", methods=["POST"])
def clocked():
    key = os.getenv("CLOCKED_API_KEY", "")
    if not key:
        return error("Clocked is not configured. Set CLOCKED_API_KEY in Vercel.", 503)
    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        return error("Expected a JSON object.", 400)
    utterance = body.get("utterance", "")
    documents = body.get("candidates", [])
    if not isinstance(utterance, str) or not 1 <= len(utterance.strip()) <= 800:
        return error("Issue text must be between 1 and 800 characters.", 400)
    if not isinstance(documents, list) or not 1 <= len(documents) <= 8:
        return error("Provide between 1 and 8 candidate offerings.", 400)
    clean = []
    ids = set()
    for doc in documents:
        if not isinstance(doc, dict):
            return error("Invalid catalog candidate.", 400)
        id_, title, description = doc.get("id"), doc.get("title"), doc.get("text")
        if not all(isinstance(x, str) for x in (id_, title, description)):
            return error("Catalog candidate fields must be strings.", 400)
        if not (1 <= len(id_) <= 30 and 1 <= len(title) <= 100 and len(description) <= 1500):
            return error("Catalog candidate too large or empty.", 400)
        if id_ in ids:
            return error("Duplicate catalog candidate.", 400)
        ids.add(id_)
        clean.append({"id": id_, "title": title, "text": description})
    try:
        from clocked_sdk import Clocked
        client = Clocked(timeout=22, max_attempts=2)
        try:
            intent = dict(client.decide(state=utterance, questions={
                "incident": {"type": "noul", "instructions": "Is this about failure, error, degradation or outage of something previously working?"},
                "service_request": {"type": "noul", "instructions": "Is this about obtaining access, installation, a new item or a requested change?"},
                "it_support": {"type": "noul", "instructions": "Is this about enterprise IT support rather than unrelated general knowledge?"}
            }))
            ranked = dict(client.rerank(query=utterance, documents=clean, top_n=3))
        finally:
            client.close()
    except Exception as exc:
        code = getattr(exc, "status", None) or getattr(exc, "status_code", None)
        return error("Clocked request failed" + (f" (HTTP {code})" if code else "") + ". Check SDK configuration and quota.", 502)
    # Keep only structured evidence, never echo request authorization or secret fields.
    answer = intent.get("answers") if isinstance(intent, dict) else {}
    if not isinstance(answer, dict):
        answer = {}
    safe_answers = {}
    for k in ("incident", "service_request", "it_support"):
        v = answer.get(k, {})
        if isinstance(v, dict):
            safe_answers[k] = {"noul": v.get("noul")}
    items = ranked.get("results", []) if isinstance(ranked, dict) else []
    valid_results = []
    if isinstance(items, list):
        for x in items[:3]:
            if isinstance(x, dict) and x.get("id") in ids:
                valid_results.append({"id": x.get("id"), "action": x.get("action"), "relevance_score": x.get("relevance_score")})
    response = jsonify({"source": "REAL CLOCKED API", "intent": safe_answers, "offerings": valid_results, "methods": ["decide", "rerank"]})
    response.headers["Cache-Control"] = "no-store"
    return response

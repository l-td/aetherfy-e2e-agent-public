"""
Test fixture for aetherfy-e2e-tests GitHub integration.

Minimal FastAPI agent used by tests in tests/test_github.py to exercise:
- afy github link / unlink (public repo path)
- webhook-triggered redeploy
- afy deploy --from-github

Mirrors fixtures/agents/python_basic/main.py in the e2e-tests repo.
"""

import os
from fastapi import FastAPI, Request

app = FastAPI()

print("E2E_TEST_MARKER: Python agent started")


@app.get("/")
async def root():
    return {
        "message": "Hello from aetherfy-e2e-agent!",
        "version": os.environ.get("AGENT_VERSION", "1.0.0"),
    }


@app.get("/env")
async def get_env():
    return {
        "PORT": os.environ.get("PORT", "8080"),
        "AGENT_NAME": os.environ.get("AGENT_NAME", "unknown"),
    }


@app.post("/echo")
async def echo(request: Request):
    try:
        data = await request.json()
    except Exception:
        data = {}
    return {"echo": data}

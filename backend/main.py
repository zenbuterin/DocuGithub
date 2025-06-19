from fastapi import FastAPI
from app.api import github

app = FastAPI(
    title="DocuGitHub",
    description="Codebase Documentation Automation Powered by AI",
    version="1.0.0"
)
app.include_router(github.router)

@app.get("/")
def read_root():
    return {"message": "AI-Powered Docs API"}
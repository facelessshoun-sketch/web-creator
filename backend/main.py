import io,zipfile
from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from ai_generator import generate_html

app=FastAPI(title="AI Website Builder API")
app.add_middleware(CORSMiddleware,allow_origins=["*"],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])

class GenerateRequest(BaseModel):
    prompt:str

@app.get("/")
def root(): return {"message":"AI Website Builder API is running"}

@app.get("/health")
def health(): return {"status":"ok"}

@app.post("/api/generate")
def generate(req:GenerateRequest):
    if not req.prompt.strip(): raise HTTPException(400,"Prompt is required")
    try:return {"html":generate_html(req.prompt)}
    except Exception as e: raise HTTPException(500,str(e))

@app.post("/api/download")
def download(req:GenerateRequest):
    if not req.prompt.strip(): raise HTTPException(400,"Prompt is required")
    try:
        html=generate_html(req.prompt);mem=io.BytesIO()
        with zipfile.ZipFile(mem,"w",zipfile.ZIP_DEFLATED) as z:z.writestr("index.html",html)
        mem.seek(0)
        return StreamingResponse(mem,media_type="application/zip",headers={"Content-Disposition":"attachment; filename=generated-website.zip"})
    except Exception as e: raise HTTPException(500,str(e))

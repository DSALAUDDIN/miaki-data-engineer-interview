from fastapi import FastAPI, UploadFile, File, HTTPException

# Initialize the FastAPI app
app = FastAPI(
    title="Document Extractor API",
    description="API for extracting structured data from documents.",
    version="0.1.0"
)

@app.get("/", tags=["Health Check"])
async def read_root():

    return {"status": "ok", "message": "Welcome to the Document Extractor API!"}

@app.post("/extract/pcc", tags=["Extraction Placeholders"])
async def extract_pcc_placeholder(file: UploadFile = File(..., description="A PCC document file.")):

    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded.")

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File received. PCC extraction logic is not yet implemented.",
        "scenario": "pcc"
    }

@app.post("/extract/university", tags=["Extraction Placeholders"])
async def extract_university_placeholder(file: UploadFile = File(..., description="A university certificate file.")):

    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded.")

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "message": "File received. University certificate extraction logic is not yet implemented.",
        "scenario": "university"
    }
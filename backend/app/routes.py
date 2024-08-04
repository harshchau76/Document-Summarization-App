from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from .models import SummarizeRequest
from .utils import summarize_document, save_file

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = save_file(file)
    if file_path:
        return JSONResponse(content={"file_path": file_path})
    else:
        raise HTTPException(status_code=500, detail="File upload failed")

@router.post("/summarize")
async def summarize_file(request: SummarizeRequest):
    summary = summarize_document(request.text)
    return JSONResponse(content={"summary": summary})

app.include_router(router)

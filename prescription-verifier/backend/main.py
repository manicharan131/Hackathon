from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os, shutil

app = FastAPI()

# Step A: Create uploads folder (to save uploaded files)
UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

# Step B: Mount the static folder (this is where your frontend files live)
# If you have "static/index.html", you can visit it at http://127.0.0.1:8000/static/index.html
app.mount("/static", StaticFiles(directory="static"), name="static")

# Step C: When someone opens http://127.0.0.1:8000, show index.html
@app.get("/")
def read_root():
    return FileResponse("static/index.html")

# Step D: Handle file upload (from frontend)
@app.post("/upload-prescription/")
async def upload_prescription(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded file locally
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # For now, just confirm upload
    return {"filename": file.filename, "status": "Uploaded successfully ✅"}
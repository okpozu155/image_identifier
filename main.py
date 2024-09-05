from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import StreamingResponse
from model import model_pipeline
import io
from PIL import Image 
from image_loader import image_opener


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI app!"}

@app.post("/ask")
def ask(text: str, file: UploadFile = File(None), url: str = Form(None), path: str = Form(None)):
    """
    Endpoint to process a text query and an optional image.

    Parameters:
    - text (str): The text input for the model.
    - file (UploadFile): The image file to upload (optional).
    - url (str): The URL of the image to retrieve (optional).
    - path (str): The local path of the image to retrieve (optional).

    Returns:
    - dict: The model's response.
    """
    try:
        # Use the image_opener function to get the image from one of the sources
        image = image_opener(image_file=file, image_url=url, image_path=path)
        
        # Process the text and image using the model pipeline
        result = model_pipeline(text, image)
        
        return {'answer': result}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail="An error occurred while processing the request") from e
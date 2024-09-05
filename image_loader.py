from fastapi import FastAPI, UploadFile, File, HTTPException, Form
from fastapi.responses import StreamingResponse
from PIL import Image
import io
import requests
import os

# Correct URL
url = "https://images1.fanpop.com/images/photos/1600000/Pics-from-the-zoo-animals-1674822-2560-1920.jpg"
local = "/home/okpozu/Pictures/IMG_20210429_170159.jpg"

def image_opener(image_file: UploadFile = None, image_url: str = None, image_path: str = None) -> Image.Image:
    """
    Opens an image from an UploadFile object, a URL, or a local file path.

    Parameters:
    - image_file (UploadFile): The uploaded image file.
    - image_url (str): The URL of the image.
    - image_path (str): The local file path of the image.

    Returns:
    - Image.Image: A PIL Image object representing the loaded image.

    Raises:
    - HTTPException: If the image cannot be opened (e.g., if the image is corrupted or in an unsupported format).
    """
    image = None
    
    if image_file:
        # Read the uploaded file into a byte stream (synchronously)
        image_bytes = io.BytesIO(image_file.file.read())
    elif image_url:
        # Download the image from the URL
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            image_bytes = io.BytesIO(response.content)
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=400, detail="Invalid image URL or unable to download the image") from e
    elif image_path:
        # Open the image from the local file system
        if not os.path.exists(image_path):
            raise HTTPException(status_code=400, detail="Image path does not exist")
        try:
            image_bytes = open(image_path, 'rb')
        except OSError as e:
            raise HTTPException(status_code=400, detail="Unable to open image from local path") from e
    else:
        raise HTTPException(status_code=400, detail="No image source provided")

    try:
        # Open the image using PIL
        image = Image.open(image_bytes)
        image.verify()  # Verify that it is a valid image
        if image_file or image_url:
            image_bytes.seek(0)  # Rewind the stream if using file or URL
        image = Image.open(image_bytes)  # Reopen the image after verification
    except (IOError, OSError) as e:
        raise HTTPException(status_code=400, detail="Invalid image file") from e

    return image

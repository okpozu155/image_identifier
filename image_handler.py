import requests
from PIL import Image
import os

# Correct URL
url = "https://images1.fanpop.com/images/photos/1600000/Pics-from-the-zoo-animals-1674822-2560-1920.jpg"
local = "/home/okpozu/Pictures/IMG_20210429_170159.jpg"

def image_opener(source: Image):
    """
    This function loads image from the local drive, 
    If the image is a url then it downloads and loads the image
    """
    if os.path.isfile(source):
        image = Image.open(source)
    else:
        # Fetch and open the image
        response = requests.get(source, stream=True)
        response.raise_for_status()  # Check for HTTP errors
        image = Image.open(response.raw)

    # Display the image (optional)
    # image.show()
    return image

image_opener(local)
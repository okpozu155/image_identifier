
Image Identifier Application

This Dockerized application utilizes the ViLT (Vision-and-Language Transformer) model, specifically ViltProcessor and ViltForQuestionAnswering, to process both images and text together. It allows users to ask questions about an image and receive answers based on the visual content and accompanying text input. The application leverages state-of-the-art Vision-Language models for Visual Question Answering (VQA).
Features

    Vision-and-Language Transformer: Uses the ViLT model, fine-tuned for visual question answering tasks.
    Image and Text Input: Accepts an image and a related question to provide meaningful answers.
    Dockerized Application: Simplifies deployment across different environments.
    Pre-trained Model: Based on the dandelin/vilt-b32-finetuned-vqa model for efficient and accurate processing.

Requirements

To run this application, you'll need the following:

    Python 3.8 or higher
    Libraries:
        transformers
        Pillow
        torch
    Docker (if running as a container)

Installation

    Clone the Repository:

    git clone https://github.com/okpozu155/image_identifier.git

    cd image_identifier

    Install Dependencies: If running locally, use the following command:

    pip install transformers Pillow torch

    Set Up Docker and build the Docker image:

    docker init

    Then add the necessary files.

How to Use the Application
Local Execution

Import the necessary modules:

from PIL import Image
from app import model_pipeline
        

Prepare your inputs:

    Text: A question related to the image.
    Image: A valid image file (e.g., .jpg, .png).

Run the model:

question = "What is in the image?"
image = Image.open("path_to_image.jpg")
model_pipeline(question, image)
        

The output will display the model's answer:

The answer is: <predicted_answer>

File Structure
<pre>
image_identifier/
│
├── Dockerfile           # Configuration for Docker image
├── app.py               # Core application logic (includes image_handler.py, image_loader.py, main.py and model.py)
├── requirements.txt     # List of dependencies
├── README.md            # Documentation
└── images/              # Directory for input images
 </pre>       

Model Details

    Name: dandelin/vilt-b32-finetuned-vqa
    Description: Fine-tuned Vision-and-Language Transformer for Visual Question Answering tasks.
    Source: Hugging Face Transformers



from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image


processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")


def model_pipeline(text: str, image: Image):
	"""
    Takes text (question) and image, processes them using the ViLT model, and returns the model's answer.
    
    Parameters:
    text (str): The question related to the image.
    image (Image): The image to be analyzed alongside the text.
    
    Returns:
    None: Prints the answer predicted by the model.
    """
	# Encode the image and text into tensors, preparing them for the mode.
	encoding = processor(image, text, return_tensors="pt")

	# Pass the processed inputs through the model
	outputs = model(**encoding)

	# Get the predicted logits (raw scores) from the model output
	logits = outputs.logits

	# Identify the index of the highest-scoring answer
	idx = logits.argmax(-1).item()

	# return model.config.id2label[idx]
	print("The  answer is:", model.config.id2label[idx])
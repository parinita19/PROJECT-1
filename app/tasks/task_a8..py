from app.utils.file_utils import write_file_safe
from app.utils.llm_utils import extract_credit_card
from PIL import Image
import pytesseract
import os
from app.config import DATA_DIR

def run() -> str:
    """
    A8: Extract the credit card number from /data/credit-card.png using OCR and an LLM.
    This implementation uses pytesseract to extract text from the image file, then calls the LLM to extract 
    only the credit card number (digits only, with no spaces or dashes).
    """
    # Construct the absolute path for the image file
    image_path = os.path.join(DATA_DIR, "credit-card.png")
    
    # Open the image using Pillow
    image = Image.open(image_path)
    
    # Use pytesseract to extract text from the image (real OCR, not a dummy string)
    ocr_text = pytesseract.image_to_string(image)
    
    # Pass the OCR text to the LLM to extract the credit card number
    card_number = extract_credit_card(ocr_text)
    
    # Write the extracted card number to credit-card.txt
    write_file_safe("credit-card.txt", card_number)
    
    return f"Extracted credit card number: {card_number}"
import os
import time
import tkinter as tk
import pyautogui
import keras_ocr
from tkinter import messagebox

# Initialize Keras-OCR pipeline
pipeline = keras_ocr.pipeline.Pipeline()

# Function to create a folder named 'prompts' for saving screenshots
def create_prompts_folder():
    if not os.path.exists("prompts"):
        os.makedirs("prompts")

# Function to take a screenshot and save it to the 'prompts' folder
def take_screenshot():
    create_prompts_folder()
    screenshot = pyautogui.screenshot()
    screenshot_path = "prompts/screenshot.png"
    screenshot.save(screenshot_path)
    return screenshot_path

# Function to process the image and extract text using Keras-OCR
def extract_text_from_image(image_path):
    image = keras_ocr.tools.read(image_path)
    result = pipeline.recognize([image])
    extracted_text = ""
    for text, box in result[0]:
        extracted_text += text + "\n"
    return extracted_text

# Main function to handle the workflow
def main():
    root = tk.Tk()
    root.withdraw()  # Hide main window (we only need messageboxes)
    
    # Wait for the user to switch windows
    messagebox.showinfo("Information", "Please switch to the screen where the question is displayed, then press OK.")
    
    # Take a screenshot of the active screen
    screenshot_path = take_screenshot()
    print(f"Screenshot saved to {screenshot_path}")
    
    # Extract text from the screenshot using Keras-OCR
    extracted_text = extract_text_from_image(screenshot_path)
    print(f"Extracted Text:\n{extracted_text}")
    
    # Ask the user if the response is correct
    is_correct = messagebox.askyesno("Correct?", "Is the extracted text correct?")
    
    if not is_correct:
        print("Please correct the extracted text manually.")
    else:
        print("Text extraction is correct!")

if __name__ == "__main__":
    main()

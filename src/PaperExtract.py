import os
from pdfminer.high_level import extract_text
import pandas as pd
import re

# Define a function to replace consecutive newlines with a single space
def replace_newlines(text):
    # Replace consecutive newlines with a single newline
    text = re.sub('\n+', '\n', text)
    # Replace single newline with a space
    text = re.sub('\n', ' ', text)
    text = text.strip()
    return text

def save_text_to_file(file_path, text, save_dir):
    # Get the file name from the file path
    file_name = os.path.splitext(os.path.basename(file_path))[0] + '.txt'
    
    # Create the new directory if it does not exist
    os.makedirs(save_dir, exist_ok=True)

    # Create a new text file path in the save_dir directory
    text_file_path = os.path.join(save_dir, file_name)
    
    # Open the text file and write the text into it
    with open(text_file_path, 'w', encoding='utf-8') as text_file:
        text_file.write(text)


def replace_newlines():
    df = pd.read_excel('./TitleAbstract.xlsx')
    df['Title'] = df['Title'].apply(replace_newlines)
    df['Abstract'] = df['Abstract'].apply(replace_newlines)
    df.to_excel('./TitleAbstract.xlsx', index=False)


if __name__ == '__main__':
    PaperPath = 'D:\yuyouyu\SHU\HEA-REF'
    pdf_files = os.listdir(PaperPath)
    pdf_files = [os.path.join(PaperPath, pdf_file) for pdf_file in pdf_files]

    save_dir = 'D:\yuyouyu\SHU\HEA-REF\HEA-REF-TEXT'
    for file_path in pdf_files:
        text = extract_text(file_path)
        # Save the text to a .txt file in the specified directory
        save_text_to_file(file_path, text[:5000], save_dir)
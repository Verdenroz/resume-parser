from dotenv import load_dotenv
from fastapi import FastAPI
from pypdf import PdfReader

from utils.Formatter import Formatter
from utils.TextCleaner import TextCleaner

load_dotenv()

app = FastAPI()


@app.get("/")
def read_root():
    resume_text = parse_resume('HT_Resume.pdf')
    return resume_text


def parse_resume(file_path):
    reader = PdfReader(file_path)
    text = ''
    for page in reader.pages:
        text += page.extract_text()

    # Clean the extracted text
    cleaner = TextCleaner()
    cleaned_text = cleaner.clean_text(text)
    print(cleaned_text)

    formatter = Formatter()
    formatted_text = formatter.format(cleaned_text)

    return formatted_text


# def main():
#     text = parse_resume('HT_Resume.pdf')
#     print(text)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

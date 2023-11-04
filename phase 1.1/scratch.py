import PyPDF2
import re
import fitz  # PyMuPDF
import spacy
from spacy.matcher import Matcher
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

pdf_file = r"C:\Users\91823\Downloads\TR_02_Leistungsbeschreibung_DDF_23_Los2(copy).pdf"
doc = fitz.open(pdf_file)
pdf_text = ""
text = ""


for page in doc:
    text += page.get_text()
    alphabetic_text = re.sub(r'[^a-zA-Z\s]', '', text)
    pdf_text += alphabetic_text
doc.close()


file_path = r"C:\Users\91823\Desktop\example.txt"
with open(file_path, "w") as f:
    f.write(pdf_text)


from spacypdfreader.spacypdfreader import pdf_reader
nlp = spacy.load('en_core_web_sm')
text = r"C:\Users\91823\Desktop\example.txt"
with open(text, "r", encoding="utf-8") as file:
    summ = file.read()



doc = nlp(summ)
file_path = r"C:\Users\91823\Desktop\example1.txt"
with open(file_path, "a") as file:
   for sent in doc.sents:
       file.write((sent.text + "\n"))




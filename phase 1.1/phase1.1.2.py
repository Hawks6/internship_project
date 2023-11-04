import spacy
from spacy.matcher import Matcher

# Load the spaCy language model
nlp = spacy.load("en_core_web_sm")

# Create a Matcher object
matcher = Matcher(nlp.vocab)

# Define the patterns for the keywords
patterns = [
    [{"LOWER": "pre-qualification"}],
    [{"LOWER": "proof"}],
    [{"LOWER": "certification"}],
    [{"LOWER": "completed"}],
    [{"LOWER": "liquidation"}],
    [{"LOWER": "regulations"}],
    [{"LOWER": "insolvency"}],
    [{"LOWER": "iso"}],
    [{"LOWER": "proof"}, {"LOWER": "entry"}],
    # Add other keyword patterns here
]

# Add the patterns to the Matcher
matcher.add("ELIGIBILITY_CRITERIA", patterns)

# Read the text file
with open(r"C:\Users\91823\Desktop\example1.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Process the text with spaCy
doc = nlp(text)

# Initialize a list to store sentences containing matched keywords
sentences_with_keywords = set()

matched_sentence_indices = set()

# Iterate through the sentences in the processed text
for sentence_index, sentence in enumerate(doc.sents):
    # Use the Matcher to find matches in the sentence
    matches = matcher(sentence)
    if matches:
        matched_sentence_indices.add(sentence_index)

# Filter and store sentences with matches
for sentence_index, sentence in enumerate(doc.sents):
    if sentence_index in matched_sentence_indices:
        sentences_with_keywords.add(sentence.text)

# Print the sentences containing matched keywords
# Create and write the extracted sentences to a text file
output_file = r"C:\Users\91823\Desktop\example2.txt"
with open(output_file, "w", encoding="utf-8") as outfile:
    for sentence in sentences_with_keywords:
        outfile.write(sentence + "\n")

print(f"Extracted sentences have been saved to {output_file}.")
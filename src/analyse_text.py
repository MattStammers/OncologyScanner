import spacy

# Load the SciSpacy model
nlp = spacy.load("en_ner_bc5cdr_md")

# Define categories of interest
def analyse_text(text):
    doc = nlp(text)
    oncology_entities = []

    # Define keywords for filtering
    diagnosis_keywords = ["cancer", "tumor", "carcinoma", "melanoma", "lymphoma"]
    genetic_keywords = ["KRAS", "HER2", "EGFR", "BRCA", "TP53", "+", "-"]
    staging_keywords = ["TNM", "stage", "stage I", "stage II", "stage III", "stage IV", "IV", "I+", "T", "N", "M"]

    for entity in doc.ents:
        entity_lower = entity.text.lower()
        if any(keyword in entity_lower for keyword in diagnosis_keywords + genetic_keywords + staging_keywords):
            oncology_entities.append({"text": entity.text, "label": entity.label_})

    return oncology_entities

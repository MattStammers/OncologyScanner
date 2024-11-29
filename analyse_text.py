import sparknlp
from sparknlp.pretrained import PretrainedPipeline

# Initialize Spark NLP
spark = sparknlp.start()
pipeline = PretrainedPipeline("clinical_ner", "en", "clinical/models")

def analyse_text(text):
    # Run Spark NLP pipeline
    results = pipeline.annotate(text)
    
    # Extract specific entities
    diagnosis = [entity for entity, label in zip(results['entities'], results['ner_labels']) if label == 'DIAGNOSIS']
    genetic_mutations = [entity for entity, label in zip(results['entities'], results['ner_labels']) if label == 'GENETIC_MUTATION']
    tumour_staging = [entity for entity, label in zip(results['entities'], results['ner_labels']) if label == 'TUMOUR_STAGING']
    clinical_staging = [entity for entity, label in zip(results['entities'], results['ner_labels']) if label == 'CLINICAL_STAGING']
    
    # Organise extracted data
    extracted_info = {
        "diagnosis": diagnosis,
        "genetic_mutations": genetic_mutations,
        "tumour_staging": tumour_staging,
        "clinical_staging": clinical_staging
    }
    
    return extracted_info
    
    

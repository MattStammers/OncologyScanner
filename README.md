# OncologyScanner
Flask application. User uploads PDF. Text is extracted and parsed to JohnSnowLabs' MedicalNerModel, a pre-trained named entity recognition model, that can detect medical terms.

**Points of interest**: 
- Limited pathology reports for oncology, have started with non-oncology reports first in the meantime.
- Used SparkNLP by JohnSnowLabs, seems to be the superior open-source model.

**Pain points**:
- Package dependancies are incredibly painful to deal with (still bugs).
- Issues with hadoop (file manager) and Spark (engine), that allows SparkNLP to run.

Aim is to finalise the app over the next couple of days.

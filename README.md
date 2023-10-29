# Md_Shahnawaz_Hossain_BlockstakML
This folder contains the BlockstakML assessment tasks

## Installation

Run the following command to install the dependencies:

```bash
pip install -r requirements.txt
```

## Dependency

You must have the following files in your repository to operate locally:

Decision_classifier_bank_model.joblib (Trained Decision classifier model on basis of which user has to provide input for 14 specific mandatory fields to get predicted deposit status)

Naive_Bayes_classifier_bank_model.joblib (Trained Naive Bayes classifier model on basis of which user has to provide input for 14 specific mandatory fields to get predicted deposit status)

templates/index.html (Query and model output will be displayed according to this file)

BlockstakML.ipynb (Jupyter notebook regarding main answer script loaded with answers and source codes)

BlockstakML_web_app.py (Python script based on Flask regarding model response deployment through web application)
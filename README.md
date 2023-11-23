# MedicalSpacyNER
Development of proof of concept medical Named Entity Recognition (NER) based on SpaCy library

Hello! This is my test project on extracting medical terms from texts, built on the Spacy package. The initial small dataset with annotated entities, Corona2.json, can be found in the dataset folder. 
The code was initially developed and tested in Colab (https://drive.google.com/file/d/1hAkZvNhDoK6FlXDaeWM0YTo1N6gDDM4Y/view?usp=sharing) and later compiled in PyCharm.

ner_medical_spacy.py: Creates and trains the model.
ner_medical_spacy_exe.py: Takes a text file as input and outputs annotated text with identified medical entities.
ner_medical_spacy.exe: Compiled from ner_medical_spacy_exe.py using the tool available at https://habr.com/ru/companies/vdsina/articles/557316/.

To run, execute the command:
  ner_medical_spacy_exe.exe textFile01.txt

where the first and only parameter is the file with the source text. The output will be a file named result.html with highlighted medical terms (if any are found). You can also run ner_medical_spacy_exe.py similarly.

Important: When executing, the model is loaded (the 'model' folder must be present next to the executable file).

Good luck!  

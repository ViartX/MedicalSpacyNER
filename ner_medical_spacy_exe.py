# this is an executable code for using Medical NER model
# uses Spacy model, stored in "model" folder next to it
# receives txt file with text for NER processing as an argument
# creates .html file with annotated text with detected medical entities in same folder as incoming file
# call example ner_medical_spacy_exe.py C:\NerTest\textFile.txt"

import sys
import os.path
import spacy


def main():
    args = sys.argv[1:]

    if len(args) > 0:
        # first argument - file with the medical text
        path_to_source_file = args[0]
        process_ner_model(path_to_source_file)
    else:
        print(f'Error: wrong function call - no path to initial file')

# function receives filename with source text to be processed with NER model
# creates html file with spacy rendered results of processing in the same folder
def process_ner_model(input_filename):

    if not os.path.exists(input_filename):
        print(f'Error: File {input_filename} does not exist')
        quit

    f = open(input_filename)
    initial_text = ""       # initial text variable
    for line in f:
        initial_text += line

    nlp_trained_model = spacy.load("model")
    result_text = nlp_trained_model(initial_text)
    result_text_rendered = spacy.displacy.render(result_text, style="ent")  # get rendered text for output in html file

    output_filename = os.path.dirname(os.path.abspath(input_filename))+"/result.html"
    outfile = open(output_filename, "w")
    outfile.write(result_text_rendered)
    outfile.close()

# main function processing
if __name__ == '__main__':
    main()
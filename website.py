from flask import Flask, render_template

website = Flask(__name__)

@website.route('/') 
def first_page():
    return render_template('first_page.html')

@website.route('/homepage') 
def homepage():
    return render_template('homepage.html')

@website.route('/project_document') 
def project_document():
    return render_template('project_document.html')

@website.route('/active_operations') 
def active_operations():
    return render_template('active_operations.html')

@website.route('/basic_information') 
def basic_information():
    return render_template('basic_information.html')

@website.route('/list_of_unique_sequence_IDs') 
def list_of_unique_sequence_IDs():
    return render_template('list_of_unique_sequence_IDs.html')

@website.route('/number_of_features') 
def number_of_features():
    return render_template('number_of_features.html')

@website.route('/fraction_of_unassebled_sequences') 
def fraction_of_unassebled_sequences():
    return render_template('fraction_of_unassebled_sequences.html')

@website.route('/number_of_entries') 
def number_of_entries():
    return render_template('number_of_entries.html')

@website.route('/gene_names') 
def gene_names():
    return render_template('gene_names.html')

if __name__ == "__main__":
    website.run(debug=True)
from flask import Flask, request, render_template, url_for
from operations import *
import numpy as np
import pandas as pd
from create_html import *
import os

website = Flask(__name__)

@website.route('/') 
def first_page():
    return render_template('first_page.html')

@website.route('/homepage') 
def homepage():
    return render_template('homepage.html')

@website.route('/active_operations') 
def active_operations():
    menu = {"basic_info" :"1 basic information about the dataset", 
            "unique_sequence_ids":"2 unique sequence IDs available in the dataset", 
            "unique_operation_types":"3 unique operation types available in the dataset", 
            "count_features_by_source":"4 number of features provided by the dataset", 
            "count_features_by_type":"5 number of entries for each type of operation",
            "chromosome_dataset":"6 information about entire chromosomes",
            "fraction_unassembled_seq":"7 fraction of unassembled sequences",
            "ensembl_havana_dataset":"8 entries from source ensembl, havana and ensembl_havana", 
            "count_entries_by_type_ensembl_havana":"9 count entries for each type of operation from source ensembl, havana and ensembl_havana",
            "gene_names_ensembl_havana":"10 gene names from source ensembl, havana and ensembl_havana"}
    active_ops = dataset.get_active_operation()
    result = {i : menu[i] for i in active_ops}
    return render_template('active_operations.html', result = result)

@website.route('/1 basic information about the dataset') 
def basic_information():
    all = dataset.basic_info()
    cols, dt = all.data
    return render_template('1 basic information about the dataset.html', cols = cols, dt = dt)

@website.route('/2 unique sequence IDs available in the dataset') 
def unique_sequence_IDs():
    dt = dataset.unique_sequence_ids()
    result = dt.data
    return render_template('2 unique sequence IDs available in the dataset.html', result = result)

@website.route('/3 unique operation types available in the dataset') 
def unique_operation_types():
    dt = dataset.unique_operation_types()
    result = dt.data
    return render_template('3 unique operation types available in the dataset.html', result = result)

@website.route('/4 number of features provided by the dataset') 
def number_of_features():
    dt = dataset.count_features_by_source()
    result = dt.data
    return render_template('4 number of features provided by the dataset.html', result = result)

@website.route('/5 number of entries for each type of operation') 
def number_of_entries():
    dt = dataset.count_features_by_type()
    result = dt.data
    return render_template('5 number of entries for each type of operation.html', result = result)

@website.route('/6 information about entire chromosomes') 
def new_dataset():
    dt = dataset.chromosome_dataset()
    result = dt.data
    table = result.to_html()
    file = os.path.abspath("templates/6 information about entire chromosomes.html")
    h = "INFORMATION ABOUT ENTIRE CHROMOSOMES"
    creator(file, table, h)
    return render_template('6 information about entire chromosomes.html')

@website.route('/7 fraction of unassembled sequences') 
def fraction_of_unassembled_sequences():
    dt = dataset.fraction_unassembled_seq()
    result = dt.data
    return render_template('7 fraction of unassembled sequences.html', result = result)

@website.route('/8 entries from source ensembl, havana and ensembl_havana') 
def entries_from_source():
    dt = dataset.ensembl_havana_dataset()
    result = dt.data
    table = result.to_html()
    file = os.path.abspath("templates/8 entries from source ensembl, havana and ensembl_havana.html")
    h = "ENTRIES FROM SOURCE ensembl , havana AND ensembl_havana"
    creator(file, table, h)
    return render_template('8 entries from source ensembl, havana and ensembl_havana.html')

@website.route('/9 count entries for each type of operation from source ensembl, havana and ensembl_havana') 
def count_entries_from_source():
    dt = dataset.count_entries_by_type_ensembl_havana()
    result = dt.data
    table = result.to_html()
    file = os.path.abspath("templates/9 count entries for each type of operation from source ensembl, havana and ensembl_havana.html")
    h = "NUMBER OF ENTRIES FROM SOURCE ensembl , havana AND ensembl_havana FOR EACH TYPE OF OPERATION"
    creator(file, table, h)
    return render_template('9 count entries for each type of operation from source ensembl, havana and ensembl_havana.html')

@website.route('/10 gene names from source ensembl, havana and ensembl_havana') 
def gene_names():
    dt = dataset.gene_names_ensembl_havana()
    result = dt.data
    return render_template('10 gene names from source ensembl, havana and ensembl_havana.html', result = result)

if __name__ == "__main__":
    website.run(debug=True)
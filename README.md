# ADVANCED-PROGAMMING-PROJECT
 
###

## OPERATIONS
This is a list of operations provided in ```operations.py``` file:


Operation 1: basic_info

This operation returns the column names and their respective data types to a list. the names of each column and the data they store is universal in all gff3 files.

Operation 2: unique_sequence_ids

This operation traverses column 1 (‘seqid’), storing in a separate list all unique sequence IDs that are encountered. Multiple features can have the same sequid but store different types of data (like exons or supercontigs).

Operation 3: unique_operation_types

This operation traverses column 3 (‘types’), storing in a separate list all the unique types of operations. Both operation 2 and 3 use the .unique() method provided by Pandas

Operation 4:  count_features_by_source

This operation returns a dictionary where the key-value pairs correspond to the sources from which the features have been obtained (column 2) and the total number of features that originate from that source. This operation uses the .groupby() and the .count() method provided by Pandas

Operation 5: count_entries_by_operation_type

This operation follows a similar structure to Operation 4, but the features are grouped and counted based on their operation types (column 3)

Operation 6: chromosome_dataset

This operation returns a new data frame containing all features about entire chromosomes, deriving from source GRCh38. The data frame is created by filtering the data based on ‘source’ (column 2)

Operation 7: fraction_unassembled_seq

This operation creates a separate data frame containing all the data from source ‘GRCh38’ , and then counts the fraction of those filtered features that are unassembled (i.e. they are super contigs)

Operation 8: ensemble_havana_dataset

This operation creates a new dataset containing all data obtained from sources ‘havana’, ‘ensembl’ and ‘ensembl_havana’

Operation 9: count_entries_by_type_ensembl_havana

This operation creates a new dataset containing all data obtained from sources ‘havana’, ‘ensembl’ and ‘ensembl_havana’, and the counts the number of entries of this new dataset by type, storing them in a dictionary. It combined features implemented in Operation 8 and Operation 5

Operation 10: gene_names_ensembl_havana

This operation creates a new dataset containing only data of type ‘gene’ that derives from sources ‘havana’, ‘ensembl’ and ‘ensembl_havana’, and then filters the attributes column (column 9) for the names of each gene, storing them in a list.

## DATA
Dataset can be downloaded from the following link ***https://bit.ly/3X3yHXp*** or from the file list in the repository. In order for website to run smoothly the dataset should be located in the same folder as all the other files (ADVANCED PROGRAMMING EXAM) and named ```Homo_sapiens.gff3```. 

## LIBRARIES
Several different libraries are used in the programm:
```python
from flask import Flask, render_template
import gffpandas.gffpandas as gffpd
import pandas as pd
import os
from abc import ABC
```
## TEMPLATES
The templates folder contains HTML files that display the output that was cretaed through the operations in the ```operations.py``` file.

## CREATE_HTML
File ```create_html.py``` contains a function that we wrote to help design html pages that display results of 6, 8 and 9th operation. We import this file as module in website.py. Function ```creator``` takes three parameters:
 - filepath (absolute path to the html file which we want to edit)
 - table (table created from data returned by the operation we are running)
 - headline (the title we want displayed on top of html page)

The function edits an existing html file to create a page with general appearance resembling those of pages corresponding to remaining 7 operations. 

## RUNNING THE WEBSITE
Once the user has installed all the necessary libraries and downloaded the dataset (according to instructions in section DATA), html templates and py files, website can be run. We'd suggest running the website from Thonny since we've faced difficulties when running the program in VSCode. When the user runs *website.py*, a link will be provided in the terminal which can be used to access the web interface.
***http://127.0.0.1:5000***

## CRC CARDS
We have provided Class Responsibility Collaboration Cards (CRC cards) which we have used to brainstorm and put together our Object Oriented software. The CRC cards describe the two classes, Dataset and DatasetInterface, and the various methods within them. The CRC cards were created on a website called ***echeung.me/crcmaker/***

## UML DIAGRAM
In this diagram, DatasetInterface is an abstract base class representing the interface for a dataset object. Dataset is a concrete implementation of the DatasetInterface that represents a dataset in GFF3 format.

Dataset has a filepath attribute that stores the path to the GFF3 file. It also has a data attribute that stores a gffpd.DataFrame object, which is a subclass of pandas.DataFrame specifically designed to work with GFF3 files. The __active_operations attribute is a list that keeps track of which operations are currently active for the dataset. Dataset implements the check_df() method, which checks whether the GFF3 file is valid and returns the gffpd.DataFrame object. It also provides methods to activate, deactivate, and check the status of different operations that can be performed on the dataset. The Dataset class provides several methods that can be used to perform different operations on the dataset. These methods are decorated with the operation decorator, which is a higher-order function that returns a wrapper function that checks whether the operation is currently active and, if so, performs the operation and returns a new Dataset object with the updated data.
## AUTHORS
1. Bekink Laura
2. Mojsilović Natalija
3. Sarialan Sedef
4. Sgaramella Chiara

# ADVANCED-PROGAMMING-PROJECT
 
###

## SPECIFICATION
## OPERATIONS
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
Data can be downloaded from the following link ```https://bit.ly/3X3yHXp```.
## LIBRARIES
Several different libraries are used in the programm:
```python
from flask import Flask, render_template
import gffpandas.gffpandas as gffpd
import pandas as pd
from abc import ABC
```
## HTML PAGE
## TEMPLATES
## RUNNING THE HTML
To run the page properly, in the file ```operations.py```, filename needs to be set to path leading to the gff3 file on the user's computer. We tried storing the gff3 file in the same folder as the website and templates so that we don't have to copy the entire path to it, but just the name. However, this method just wouldn't work. Perhaps the issue was with our devices since laptops we tried on were the same model and running on the same interpreter (Visual studio code). 
## CRC CARDS
## UML DIAGRAMS
## AUTHORS
1. Bekink Laura
2. Mojsilović Natalija
3. Sarialan Sedef
4. Sgaramella Chiara
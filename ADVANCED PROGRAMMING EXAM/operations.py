import gffpandas.gffpandas as gffpd
import pandas as pd
from abc import ABC, abstractmethod

filename = "Homo_sapiens.gff3"

class DatasetInterface(ABC):
    @abstractmethod
    def check_df(self):
        pass

class Dataset(DatasetInterface):

    def check_df(self):
        if not self.filepath.lower().endswith('.gff3'):
           raise Exception(f"File'{self.filepath} 'is not a GFF3 file")
        else:
            gff3 = gffpd.read_gff3(self.filepath)
        return gff3.df

    def __init__(self, filename, data=None):
        self.filepath = filename
        if data is None:
            self.data = self.check_df()
        else:
            self.data = data
        self.__active_operations = ['basic_info','unique_sequence_ids', 'unique_operation_types', 'count_features_by_source', 'count_features_by_type', 'chromosome_dataset', 'fraction_unassembled_seq', 'ensembl_havana_dataset', 'count_entries_by_type_ensembl_havana', 'gene_names_ensembl_havana']

    def operation(func):
        def wrapper(*args, **kwargs):

            if args[0].is_operation_active(func.__name__):
                data = func(*args, **kwargs)
                return Dataset(args[0].filepath, data)
            else:
                raise Exception(f"The operation '{func.__name__}' is not active.")
        return wrapper
    

    def activate_operation(self, operation_name):
        if operation_name not in self.__active_operations:
            self.__active_operations.append(operation_name)
    

    def deactivate_operation(self, operation_name):
        if operation_name in self.__active_operations:
            self.__active_operations.remove(operation_name)
    

    def is_operation_active(self, operation_name):
        return operation_name in self.__active_operations
    
    def get_active_operation(self):
        return self.__active_operations
    
    @operation
    def basic_info(self):
        return self.data.columns.tolist(), self.data.dtypes.tolist()
    
    @operation
    def unique_sequence_ids(self):
      return self.data['seq_id'].unique().tolist()
    
    @operation
    def unique_operation_types(self):
        return self.data['type'].unique().tolist()
    
    @operation
    def count_features_by_source(self):
        temp=self.data.groupby('source').count().to_dict()
        res=temp['seq_id']
        return res
    
    @operation 
    def count_features_by_type(self):
        temp=self.data.groupby('type').count().to_dict()
        res=temp['seq_id']
        return res

    @operation 
    def chromosome_dataset(self):
        return self.data[self.data['source'] == 'GRCh38']
    
    @operation
    def fraction_unassembled_seq(self):
      dataset = self.data[self.data['source'] == 'GRCh38']
      return (dataset[dataset['type'] == 'supercontig'].count()/dataset.count())[0]

    @operation
    def ensembl_havana_dataset(self):
        sources = ['ensembl','havana','ensembl_havana']
        return self.data[self.data['source'].isin(sources)][:40]

    @operation
    def count_entries_by_type_ensembl_havana(self):
        sources = ['ensembl','havana','ensembl_havana']
        dataset = self.data[self.data['source'].isin(sources)]
        dataframe = pd.DataFrame(dataset)
        return dataframe.groupby('type').count()
      
    @operation
    def gene_names_ensembl_havana(self):
      sources = ['ensembl','havana','ensembl_havana']
      enshav=self.data[self.data["source"].isin(sources)]
      genes= enshav[enshav["type"]== "gene"]
      att_dict= {}
      atts= genes.loc[:, "attributes"]
      for index in atts.index:
          val= {entry.split("=")[0]: entry.split("=")[1] for entry in atts[index].split(";")}
          att_dict[index]= val        
      gene_names=[]
      for i in att_dict.keys():
        if "Name" in att_dict[i].keys():
            gene_names.append(att_dict[i]["Name"])
      return gene_names
    

dataset = Dataset(filename)
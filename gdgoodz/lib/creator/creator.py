import pandas as pd
from gdgoodz.definitions import *
from gdgoodz.lib.number_generator import NumberGenerator


class Creator():
    
    def __init__(self, dictionaries, module_name):
        self.dictionaries = dictionaries
        self.module_name = module_name
        self.number_generator = NumberGenerator()
        
    def get_export_path(self):
        pass
    
    def create_dataframe(self):
        return pd.DataFrame(self.dictionaries)
    
    def generate_unique_filename(self, file_type):
        pass
    
    def create_file(self):
        pass
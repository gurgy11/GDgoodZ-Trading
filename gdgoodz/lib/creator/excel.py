import os
import pandas as pd
from datetime import datetime
from . import Creator
from gdgoodz.definitions import *


class ExcelCreator():
    
    def __init__(self, dictionaries, module_name):
        super().__init__(dictionaries, module_name)
        self.export_dir = os.path.join(XLSX_DIR, self.module_name)
        
    def create_dataframe(self):
        return pd.DataFrame(self.dictionaries)
    
    def get_export_path(self):
        return self.export_dir
    
    def generate_unique_filename(self):
        name = "{module_name}__{now}__{file_id}.xlsx".format(module_name=self.module_name, now=datetime.now(), 
                                                            file_id=self.NumberGenerator.generate_file_id())
        filename = os.path.join(self.export_dir, name)
        
        return filename
    
    def create_file(self):
        df = self.create_dataframe()
        filename = self.generate_unique_filename()
        
        df.to_excel()
        
        return filename
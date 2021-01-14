import pandas as pd
from gdgoodz.lib.database import Database
from gdgoodz.lib.controllers import Controller
from . import SupplierModel
from datetime import datetime
from gdgoodz.definitions import *


class SupplierController(Controller):
    
    def __init__(self):
        self.db = Database()
        self.table = 'suppliers'
        self.columns = ['name', 'email_address', 'phone_number', 'website_url', 'street_address', 'city', 'region', 'postal_zip', 'country']
    
    def record_to_model(self, record):
        supplier_model = SupplierModel(record[1], record[2], record[3], record[4], record[5], record[6], record[7], record[8], record[9])
        supplier_model.id = record[0]
        supplier_model.created_at = record[10]
        supplier_model.updated_at = record[11]
        
        return supplier_model
    
    def create_record(self, form):
        pass
    
    def select_all_records(self):
        records = self.db.select_all_records(self.table)
        models = []
        
        for record in records:
            model = self.record_to_model(record)
            models.append(model)
            
        return models
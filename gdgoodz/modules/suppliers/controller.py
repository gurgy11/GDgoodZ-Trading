import re
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
    
    def form_to_model(self, form):
        model = SupplierModel(form.get('name'), form.get('email_address'), form.get('phone_number'), form.get('website_url'), 
                              form.get('street_address'), form.get('city'), form.get('region'), form.get('postal_zip'), 
                              form.get('country'))
        return model
    
    def form_to_values(self, form):
        values = [form.get('name'), form.get('email_address'), form.get('phone_number'), form.get('website_url'), 
                  form.get('street_address'), form.get('city'), form.get('region'), form.get('postal_zip'), form.get('country')]
        return values
    
    def create_record(self, form):
        form_errors = self.validate_form(form)
        
        if form_errors is not None:
            return form_errors
        else:
            values = self.form_to_values(form)
            self.db.insert_new_record(self.table, self.columns, values)
            return None
        
    def update_record(self, record_id, form):
        form_errors = self.validate_form(form)
        
        if form_errors is not None:
            return form_errors
        
        values = self.form_to_values(form)
        self.db.update_existing_record(self.table, record_id, self.columns, values)
        
        return None
    
    def validate_form(self, form):
        errors = []
        
        name = form.get('name')
        email_address = form.get('email_address')
        
        if len(name) < 3:
            errors.append('The name field cannot be less than 3 characters long!')
        elif len(name) > 100:
            errors.append('The name field cannot be greater than 100 characters long!')
        
        if len(email_address) == 0 or email_address == '' or email_address is None:
            pass
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
            errors.append('The email address provided is invalid!')
            
        if len(errors) > 0:
            return errors
        else:
            return None
    
    def select_all_records(self):
        records = self.db.select_all_records(self.table)
        models = []
        
        for record in records:
            model = self.record_to_model(record)
            models.append(model)
            
        return models
    
    def select_record_by_id(self, record_id):
        record = self.db.select_record_by_id(self.table, record_id)
        model = self.record_to_model(record)
        
        return model
    
    
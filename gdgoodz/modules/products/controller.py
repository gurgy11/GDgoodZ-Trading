from . import ProductModel
from gdgoodz.lib.database import Database
from datetime import datetime
import pandas as pd
from gdgoodz.definitions import *


class ProductController():
    
    def __init__(self):
        self.db = Database()
        self.table = 'products'
        self.columns = ['name', 'category', 'description', 'sku', 'status', 'supplier', 'country_of_origin', 'quantity', 
                        'quantity_sold', 'cost_per_unit', 'price_per_unit', 'notes']
        
    def create_new_product(self, product_form):
        product = ProductModel(product_form.get('name'), product_form.get('category'), product_form.get('description'), 
                               product_form.get('sku'), product_form.get('status'), product_form.get('supplier'), 
                               product_form.get('country_of_origin'), product_form.get('quantity'), 
                               product_form.get('quantity_sold'), product_form.get('cost_per_unit'), 
                               product_form.get('price_per_unit'), product_form.get('notes'))
        
        product_errors = self.validate_product(product)
        
        if product_errors is not None:
            return product_errors
        else:
            values = product.to_values()
            self.db.insert_new_record(self.table, self.columns, values)
            
            return None
        
    def validate_product(self, product):
        nam_error = self.validate_name(product.name)
        cat_error = self.validate_category(product.category)
        sku_error = self.validate_sku(product.sku)
        
        errors = []
        
        if nam_error is not None:
            errors.append(nam_error)
        
        if cat_error is not None:
            errors.append(cat_error)
            
        if sku_error is not None:
            errors.append(sku_error)
            
        if len(errors) > 0:
            return errors
        else:
            return None
    
    def validate_name(self, name):
        error = None
        
        if len(name) < 3:
            error = 'The product\'s name must be at least 3 characters long!'
        elif len(name) > 255:
            error = 'The product\'s name cannot be more than 255 characters long!'
            
        return error
    
    def validate_category(self, category):
        error = None
        
        if len(category) < 3:
            error = 'The product\'s category field must be at least 3 characters long!'
        elif len(category) > 45:
            error = 'The product\'s category field cannot be more than 45 characters long!'
            
        return error
    
    def validate_sku(self, sku):
        error = None
        
        if len(sku) < 6:
            error = 'The product\'s SKU field must be at least 6 characters long!'
        elif len(sku) > 12:
            error = 'The product\'s SKU field cannot be more than 12 characters long!'
            
        return error
    
    def record_to_product_model(self, record):
        product_model = ProductModel(record[1], record[2], record[3], record[4], record[5], record[6], record[7], 
                                     record[8], record[9], record[10], record[11], record[12])
        product_model.id = record[0]
        product_model.created_at = record[13]
        product_model.updated_at = record[14]
        
        return product_model
    
    def records_to_product_model(self, records):
        product_models = []
        
        for rec in records:
            product_model = ProductModel(rec[1], rec[2], rec[3], rec[4], rec[5], rec[6], rec[7], rec[8], rec[9], 
                                         rec[10], rec[11], rec[12])
            product_model.id = rec[0]
            product_model.created_at = rec[13]
            product_model.updated_at = rec[14]
            
            product_models.append(product_model)
        
        return product_models
    
    def select_all_products(self):
        product_records = self.db.select_all_records(self.table)
        product_models = self.records_to_product_model(product_records)
        
        return product_models
    
    def select_all_products_with_status(self):
        pass
    
    def select_product_by_id(self, product_id):
        product_record = self.db.select_record_by_id(self.table, product_id)
        product_model = self.record_to_product_model(product_record)
        
        return product_model
    
    def edit_product(self, product_id, product_form):
        ''' Edits a product and updates the record in the database '''
        
        # Create a product model object based on the newly submitted form
        product = ProductModel(product_form.get('name'), product_form.get('category'), product_form.get('description'), product_form.get('sku'), 
                                   product_form.get('status'), product_form.get('supplier'), product_form.get('country_of_origin'), 
                                   product_form.get('quantity'), product_form.get('quantity_sold'), product_form.get('cost_per_unit'), 
                                   product_form.get('price_per_unit'), product_form.get('notes'))
        
        # Validate the product form
        product_errors = self.validate_product(product) # Returns an array of errors or None if there aren't any validation issues
        
        # Return an error of errors if the form is invalid
        if product_errors is not None:
            return product_errors # If there are errors, this function returns and ends here
        
        # Create the array of values for each product field
        values = product.to_values()
        
        # Use the database object to execute the update
        self.db.update_existing_record(self.table, product_id, self.columns, values)
        
        # Return None since there are no form validation errors
        return None
    
    def delete_product(self, product_id):
        ''' Deletes a product in the database '''
        
        self.db.delete_existing_record(self.table, product_id)
        
    def product_models_to_dict(self, product_models):
        ''' Converts an array of product models into an array of product dicts '''
        
        products_dict = []
        
        for p in product_models:
            product_dict = p.to_dict()
            products_dict.append(product_dict)
            
        return products_dict
    
    def product_dicts_to_dataframe(self, product_dicts):
        ''' Converts an array of product dicts into a pandas dataframe '''
        
        products_df = pd.DataFrame(product_dicts)
        return products_df
    
    def products_dataframe_to_excel(self, products_df):
        ''' Exports the dataframe data into an XLSX file '''
        
        file_name = 'products-inventory.xlsx'
        file_path = os.path.join(XLSX_DIR, 'products/' + file_name)
        
        products_df.to_excel(file_path)
        
        return file_path
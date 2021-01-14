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
        
    def create_record(self, form):
        pass
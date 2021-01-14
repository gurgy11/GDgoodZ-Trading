from gdgoodz.lib.database import Database


class Controller():
    
    def __init__(self):
        self.db = Database()
        self.table = None
        self.columns = None
        
    def record_to_model(self, record):
        pass
    
    def select_all_records(self):
        records = self.db.select_all_records(self.table)
        models = []
        
        for record in records:
            model = self.record_to_model(record)
            models.append(model)
        
        return models
    
    def select_records_with_condition(self, column, value):
        pass
    
    def select_record_by_id(self, record_id):
        pass
    
    def create_record(self, form):
        pass
    
    def update_record(self, record_id, form):
        pass
    
    def delete_record(self, record_id):
        pass
    
    def validate_form(self, form):
        pass
    
    def models_to_dictionaries(self, models):
        pass
    
    def dictionaries_to_dataframe(self, dictionaries):
        pass
    
    def dataframe_to_excel(self, dataframe):
        pass
    
    def dataframe_to_csv(self, dataframe):
        pass
    
    def dataframe_to_json(self, dataframe):
        pass
from gdgoodz.lib.controllers import Controller
from gdgoodz.lib.database import Database


class DeveloperController(Controller):
    
    def __init__(self):
        self.db = Database()
        
    def fetchall_products_as_dicts(self):
        records = self.db.select_all_records('products')
        products = []
        
        for rec in records:
            product = {
                'id': rec[0],
                'name': rec[1],
                'category': rec[2],
                'description': rec[3],
                'sku': rec[4],
                'status': rec[5],
                'supplier': rec[6],
                'country_of_origin': rec[7],
                'quantity': rec[8],
                'quantity_sold': rec[9],
                'cost_per_unit': rec[10],
                'price_per_unit': rec[11],
                'notes': rec[12],
                'created_at': rec[13],
                'updated_at': rec[14]
            }
            products.append(product)
            
        return products
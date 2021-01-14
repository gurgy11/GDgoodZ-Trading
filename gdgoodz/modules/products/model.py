class ProductModel():
    
    def __init__(self, name, category, description, sku, status, supplier, country_of_origin, quantity, quantity_sold, 
                 cost_per_unit, price_per_unit, notes):
        self._id = None
        self._name = name
        self._category = category
        self._description = description
        self._sku = sku
        self._status = status
        self._supplier = supplier
        self._country_of_origin = country_of_origin
        self._quantity = quantity
        self._quantity_sold = quantity_sold
        self._cost_per_unit = cost_per_unit
        self._price_per_unit = price_per_unit
        self._notes = notes
        self._created_at = None
        self._updated_at = None
        
    ''' ID '''
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    ''' Name '''
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    ''' Category '''
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, category):
        self._category = category
    
    ''' Description '''
    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        self._description = description
        
    ''' SKU '''
    @property
    def sku(self):
        return self._sku
    
    @sku.setter
    def sku(self, sku):
        self._sku = sku
        
    ''' Status '''
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, status):
        self._status = status
    
    ''' Supplier '''
    @property
    def supplier(self):
        return self._supplier
    
    @supplier.setter
    def supplier(self, supplier):
        self._supplier = supplier
    
    ''' Country of Origin '''
    @property
    def country_of_origin(self):
        return self._country_of_origin
    
    @country_of_origin.setter
    def country_of_origin(self, country_of_origin):
        self._country_of_origin = country_of_origin
    
    ''' Quantity '''
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, quantity):
        self._quantity = quantity
    
    ''' Quantity Sold '''
    @property
    def quantity_sold(self):
        return self._quantity_sold
    
    @quantity_sold.setter
    def quantity_sold(self, quantity_sold):
        self._quantity_sold = quantity_sold
    
    ''' Cost Per Unit '''
    @property
    def cost_per_unit(self):
        return self._cost_per_unit
    
    @cost_per_unit.setter
    def cost_per_unit(self, cost_per_unit):
        self._cost_per_unit = cost_per_unit
    
    ''' Price Per Unit '''
    @property
    def price_per_unit(self):
        return self._price_per_unit
    
    @price_per_unit.setter
    def price_per_unit(self, price_per_unit):
        self._price_per_unit = price_per_unit
    
    ''' Notes '''
    @property
    def notes(self):
        return self._notes
    
    @notes.setter
    def notes(self, notes):
        self._notes = notes
    
    ''' Created At '''
    @property
    def created_at(self):
        return self._created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at
    
    ''' Updated At '''
    @property
    def updated_at(self):
        return self._updated_at
    
    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at
    
    ''' Helper Methods '''
    
    def to_dict(self):
        ''' Returns a dict of the product without underscores '''
        
        product_dict = {
            'id': self._id, 'name': self._name, 'category': self._category, 'description': self._description, 
            'sku': self._sku, 'status': self._status, 'supplier': self._supplier, 'country_of_origin': self._country_of_origin,
            'quantity': self._quantity, 'quantity_sold': self._quantity_sold, 'cost_per_unit': self._cost_per_unit, 
            'price_per_unit': self._price_per_unit, 'notes': self._notes, 'created_at': self._created_at, 
            'updated_at': self._updated_at
        }
        
        return product_dict
    
    def to_values(self):
        ''' Returns an array of the product's field values to inser into the database '''
        
        product_values = [self._name, self._category, self._description, self._sku, self._status, 
                          self._supplier, self._country_of_origin, self._quantity, self._quantity_sold, 
                          self._cost_per_unit, self._price_per_unit, self._notes]
        
        return product_values
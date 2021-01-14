class SupplierModel():
    
    def __init__(self, name, email_address, phone_number, website_url, street_address, city, region, postal_zip, country):
        self._id = None
        self._name = name
        self._email_address = email_address
        self._phone_number = phone_number
        self._website_url = website_url
        self._street_address = street_address
        self._city = city
        self._region = region
        self._postal_zip = postal_zip
        self._country = country
        self._created_at = None
        self._updated_at = None
        
    ''' Properties and Setter '''
    
    # ID
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, id):
        self._id = id
        
    # Name
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    # Email Address
    @property
    def email_address(self):
        return self._email_address
    
    @email_address.setter
    def email_address(self, email_address):
        self._email_address = email_address
    
    # Phone Number
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, phone_number):
        self._phone_number = phone_number
    
    # Website URL
    @property
    def website_url(self):
        return self._website_url
    
    @website_url.setter
    def website_url(self, website_url):
        self._website_url = website_url
    
    # Street Address
    @property
    def street_address(self):
        return self._street_address
    
    @street_address.setter
    def street_address(self, street_address):
        self._street_address = street_address
    
    # City
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        self._city = city
    
    # Region
    @property
    def region(self):
        return self._region
    
    @region.setter
    def region(self, region):
        self._region = region
    
    # Postal/Zip
    @property
    def postal_zip(self):
        return self._postal_zip
    
    @postal_zip.setter
    def postal_zip(self, postal_zip):
        self._postal_zip = postal_zip
    
    # Country
    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, country):
        self._country = country
    
    # Created At
    @property
    def created_at(self):
        return self._created_at
    
    @created_at.setter
    def created_at(self, created_at):
        self._created_at = created_at
    
    # Updated At
    @property
    def updated_at(self):
        return self._updated_at
    
    @updated_at.setter
    def updated_at(self, updated_at):
        self._updated_at = updated_at
    
    ''' Helper Methods '''
    
    # To Dict
    def to_dict(self):
        supplier_dict = {'id': self._id, 'name': self._name, 'email_address': self._email_address, 'phone_number': self._phone_number, 
                         'website_url': self._website_url, 'street_address': self._street_address, 'city': self._city, 'region': self._region, 
                         'postal_zip': self._postal_zip, 'country': self._country, 'created_at': self._created_at, 'updated_at': self._updated_at}
        return supplier_dict
    
    # To Values
    def to_values(self):
        values = [self._id, self._name, self._email_address, self._phone_number, self._website_url, self._street_address, self._city, 
                  self._region, self._postal_zip, self._country, self._created_at, self._updated_at]
        return values
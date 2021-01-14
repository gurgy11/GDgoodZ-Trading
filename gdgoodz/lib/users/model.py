class UserModel():

    def __init__(self, username, email_address, full_name, street_address, city, region, postal_zip, country,
                 password):
        self._id = None
        self._username = username
        self._email_address = email_address
        self._full_name = full_name
        self._street_address = street_address
        self._city = city
        self._region = region
        self._postal_zip = postal_zip
        self._country = country
        self._password = password
        self._created_at = None
        self._updated_at = None

    ''' ID '''
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    ''' Username '''
    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    ''' Full Name '''
    @property
    def full_name(self):
        return self._full_name
    
    @full_name.setter
    def full_name(self, full_name):
        self._full_name = full_name
        
    ''' Street Address '''
    @property
    def street_address(self):
        return self._street_address
    
    @street_address.setter
    def street_address(self, street_address):
        self._street_address = street_address
        
    ''' City '''
    @property
    def city(self):
        return self._city
    
    @city.setter
    def city(self, city):
        self._city = city
        
    ''' Region '''
    @property
    def region(self):
        return self._region
    
    @region.setter
    def region(self, region):
        self._region = region
    
    ''' Postal/Zip '''
    @property
    def postal_zip(self):
        return self._postal_zip
    
    @postal_zip.setter
    def postal_zip(self, postal_zip):
        self._postal_zip = postal_zip
        
    ''' Country '''
    @property
    def country(self):
        return self._country
    
    @country.setter
    def country(self, country):
        self._country = country
        
    ''' Password '''
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, password):
        self._password = password
        
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
        
    ''' To Dict '''
    def to_dict(self):
        ''' Converts UserModel into a formatted dict '''
        
        user_dict = {
            'id': self._id, 'username': self._username, 'full_name': self._full_name, 'street_address': self._street_address, 
            'city': self._city, 'region': self._region, 'postal_zip': self._postal_zip, 'country': self._country,
            'password': self._password, 'created_at': self._created_at, 'updated_at': self._updated_at
        }
        
        return user_dict

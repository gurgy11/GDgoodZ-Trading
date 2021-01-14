from random import randint


class NumberGenerator():
    
    def generate_file_id(self):
        ''' Generates a random ID for identifying files for download '''
        
        value = randint(10000000, 99999999)
        return value
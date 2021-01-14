import re

from gdgoodz.lib.users import UserModel
from gdgoodz.lib.database import Database

from flask import session
from werkzeug.security import generate_password_hash, check_password_hash


class AuthController():
    
    def __init__(self):
        self.db = Database()
        self.table = 'users'
        self.columns = ['username', 'email_address', 'full_name', 'street_address', 'city', 'region', 
                        'postal_zip', 'country', 'password']
        
    def login_user(self, username, password):
        records = self.db.select_records_by_field(self.table, 'username', username)
        user_record = None
        
        if len(records) >= 1:
            user_record = records[0]
            valid, errors = self.validate_user(user_record, password)
            
            if errors is not None:
                return errors
            else:
                self.set_user_session(user_record[0], user_record[1])
                return errors

    def validate_user(self, user_record, password):
        ''' Validates the user by making sure the password provided corresponds to the user with the username provided '''
        
        if check_password_hash(user_record[9], password) is True:
            return True, None
        else:
            return False, ['The password provided is incorrect! Please try again!']
    
    def register_new_user(self, reg_form):
        ''' Processes the user registration form '''
        
        user_form = {
            'username': reg_form.get('username'), 'email_address': reg_form.get('email_address'), 
            'full_name': reg_form.get('full_name'), 'street_address': reg_form.get('street_address'),
            'city': reg_form.get('city'), 'region': reg_form.get('region'), 'postal_zip': reg_form.get('postal_zip'), 
            'country': reg_form.get('country'), 'password': reg_form.get('password'), 
            'confirm_password': reg_form.get('confirm_password')
        }
        
        errors = []
        
        # Validate username
        un_valid, un_errors = self.validate_username(user_form.get('username'))
        if un_valid is False:
            for err in un_errors:
                errors.append(err)
                
        # Validate email address
        ea_valid, ea_errors = self.validate_email_address(user_form.get('email_address'))
        if ea_valid is False:
            for err in ea_errors:
                errors.append(err)
                
        # Validate password
        pw_valid, pw_errors = self.validate_password(user_form.get('password'), user_form.get('confirm_password'))
        if pw_valid is False:
            for err in pw_errors:
                errors.append(err)
                
        if len(errors) >= 1:
            return False, errors
        else:
            values = [
                reg_form.get('username'), reg_form.get('email_address'), reg_form.get('full_name'), 
                reg_form.get('street_address'), reg_form.get('city'), reg_form.get('region'), reg_form.get('postal_zip'),
                reg_form.get('country'), generate_password_hash(reg_form.get('password'))
            ]
            
            self.db.insert_new_record(self.table, self.columns, values)
            
            return True, None
        
    def validate_username(self, username):
        valid = False
        errors = []
        
        records = self.db.select_records_by_field(self.table, 'username', username)
        
        if len(records) >= 1:
            error = 'The username provided is already taken!'
            errors.append(error)
        
        if len(username) < 4:
            error = 'The username field must be at least 4 characters long!'
            errors.append(error)
        
        if len(username) > 24:
            error = 'The username field cannot be more than 24 characters long!'
            errors.append(error)
            
        if len(errors) <= 0:
            valid = True
            
        return valid, errors
    
    def validate_email_address(self, email_address):
        valid = False
        errors = []
        
        records = self.db.select_records_by_field(self.table, 'email_address', email_address)
        
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email_address):
            error = 'The email address provided is invalid!'
            errors.append(error)
            
        if len(records) > 0:
            error = 'The email address provided is already in use!'
            errors.append(error)
            
        if len(email_address) < 3:
            error = 'The email address field must be at least 3 characters long!'
            errors.append(error)
            
        if len(email_address) > 320:
            error = 'The email address field cannot be longer than 320 characters!'
            errors.append(error)
            
        if len(errors) <= 0:
            valid = True
        
        return valid, errors
        
    def validate_password(self, password, confirm_password):
        valid = False
        errors = []
        
        if password != confirm_password:
            error = 'The password fields provided must match!'
            errors.append(error)
            
        if len(password) < 6:
            error = 'The password fields must be at least characters long!'
            errors.append(error)
            
        if len(password) > 255:
            error = 'The password fields cannot be more than 255 characters long!'
            errors.append(error)
           
        if len(errors) <= 0:
            valid = True
            
        return valid, errors
    
    def set_user_session(self, id, username):
        session['uid'] = id
        session['username'] = username
        
    def clear_user_session(self):
        session.pop('uid')
        session.pop('username')
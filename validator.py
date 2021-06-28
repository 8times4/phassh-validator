import crypt 
import getpass

class Password:
    def __init__(self, password):
        self.password = password

    def validate(self):        
        vals = {
        'Password must contain at least one uppercase letter.': lambda s: any(x.isupper() for x in s),
        'Password must contain at least one lowercase letter.': lambda s: any(x.islower() for x in s),
        'Password must contain at least one digit.': lambda s: any(x.isdigit() for x in s),
        'Password must be at least 12 characters.': lambda s: len(s) >= 12,
        'Password cannot contain white spaces.': lambda s: not any(x.isspace() for x in s)            
        } 
        valid = True  
        for n, val in vals.items():                         
           if not val(self.password):                   
               valid = False
               return n
        return valid                

    def compare(self, password2):
        if self.password == password2:
            return True


if __name__ == '__main__':
    input_password = getpass.getpass('Insert Password: ')
    input_password2 = getpass.getpass('Repeat Password: ')
    p = Password(input_password)
    if p.validate() is True:
        if p.compare(input_password2) is True:
            print('Your SHA-512 password hash is:',crypt.crypt(input_password2, crypt.mksalt(crypt.METHOD_SHA512)))
        else: 
            print('Passwords do not match, please try again.')
    else:
       print(p.validate())
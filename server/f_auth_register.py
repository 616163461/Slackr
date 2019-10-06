# Function name: auth_register()
# Parameters: (email, password, name_first, name_last)
# Return type: { u_id, token }
# Exception: ValueError when:
# - Email entered is not a valid email.
# - Email address is already being used by another user
# - Password entered is not a valid password
# - name_first is more than 50 characters
# - name_last is more than 50 characters
# Description: Given a user's first and last name, email address, and password, 
# create a new account for them and return a new token for authentication in their session
#

def auth_register(email, password, name_first, name_last): 
<<<<<<< HEAD
    pass
=======
    
    pass
    
    
    
    
    
    
    
    
    
    
def check_valid_email(email): 
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex, email)):
        return True
    else:
        return False
    
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128

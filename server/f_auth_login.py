# Function name: auth_login()
# Parameters: (email, password)
# Return type: { u_id, token }
# Exception: ValueError when:
# - Email entered is not a valid email
# - Email entered does not belong to a user
# - Password is not correct
# Description: Given a registered users' email and password and generates a valid token for the user to remain authenticated
#

def auth_login(email, password):
    pass
<<<<<<< HEAD
=======

    
def check_valid_email(email): 
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex, email)):
        return True
    else:
        return False
    
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128

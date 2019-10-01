import re

def auth_login(email, password):
    #checking the password length is greater than or equal 5 characters
    if len(password) < 5:
        raise Exception(f"Error, password less than 5 characters")
    #checking the email is valid (note: we're assuming emails are valid if they contain a "@")
    if check_valid_email(email) == False: 
        raise Exception(f"Error, please enter a valid email")
    
    token = password
    u_id = email
    return u_id, token

    
def check_valid_email(email): 
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex, email)):
        return True
    else:
        return False
    

import re

def auth_login(email, password):
    #checking the password length is greater than or equal 5 characters
    if len(password) < 5:
        raise ValueError(f"Error, password less than 5 characters")
    #checking the email is valid (note: we're assuming emails are valid if they contain a "@")
    if check_valid_email(email) == False: 
        raise ValueError(f"Error, please enter a valid email")
    if
    #assuming valid tokens begin with 1
    dictionary = {}
    dictionary["token"] = "1" + password
    dictionary["u_id"] = email
    return dictionary

    
def check_valid_email(email): 
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex, email)):
        return True
    else:
        return False
    
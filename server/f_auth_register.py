import re

def auth_register(email, password, name_first, name_last): 
    
    #checking the password length is greater than or equal 5 characters
    if len(password) < 5:
        raise ValueError(f"Error, password less than 5 characters")
    #checking the email is valid (note: we're assuming emails are valid if they contain a "@")
    if check_valid_email(email) == False: 
        raise ValueError(f"Error, please enter a valid email")
    #checking that the name_first length is less than 50 characters 
    if len(name_first) > 50:
        raise ValueError(f"Error, first name exceeds 50 characters")
    #checking that the name_last length is less than 50 characters
    if len(name_last) > 50:
        raise ValueError(f"Error, last name exceeds 50 characters")
    #NEED TO CHECK IF EMAIL IS ALREADY IN USE BY ANOTHER USER OR NOT
    
    #create account here
    
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
    

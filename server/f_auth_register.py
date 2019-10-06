import re

def auth_register(email, password, name_first, name_last): 
    
    pass
    
    
    
    
    
    
    
    
    
    
def check_valid_email(email): 
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex, email)):
        return True
    else:
        return False
    

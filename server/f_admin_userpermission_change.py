import re

def admin_userperm_change(token, u_id, permission_id):
    #assuming invalid token don't begin with a 1
    if token[0:1] == "1": 
        token = token[1:]
        return token
    else:
        pass
        
        
    if check_valid_uid(u_id) == False:
        raise ValueError(f"Error, User ID does not refer to a valid user")
    if check_valid_permid(permission_id) == False:
        raise ValueError(f"Error, Permission ID does not refer to a valid value permission")
    if permission_id != "1" or permission_id != "2":
        raise AccessError(f"Error, the user is not an Admin or Owner")
        
    
    dictionary = {}
    
    return dictionary
    
def check_valid_uid(u_id):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, u_id):
        return True
    else:
        return False
        
def check_valid_permid(permission_id):
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if re.search(regex, u_id):
        return True
    else:
        return False

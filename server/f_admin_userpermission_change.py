import re
def admin_userperm_change(token, u_id, permission_id):        
    if isinstance(u_id, str) == False: #check_uid(u_id): == False:
        raise ValueError(f"Error, User ID does not refer to a valid user")
    if isinstance(permission_id, int) == False: #check_permid(permission_id) == False:
        raise ValueError(f"Error, Permission ID does not refer to a valid value permission")
    if permission_id != 1 and permission_id != 2:
        # AccessError does not exist, SystemError for now as placeholder
        raise SystemError(f"Error, the user is not an Admin or Owner")
    
    # Given u_id, set their perm to new permission_id
    
    # for testing purposes, create a sample dictionary
    dictionary = {}
    dictionary["permission_id"] = 1
    
    dictionary["permission_id"] = permission_id       
    
    return_dictionary = {}
    
    return return_dictionary
    
def check_uid(u_id):
    # checking if the u_id is valid
    regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    if(re.search(regex, u_id)):
        return True
    else:
        return False
    
    # for testing purposes, create a sample dictionary
    #dictionary_uid = {}
    #dictionary_uid["u_id"] = u_id
    
    #if u_id == dictionary_uid["u_id"]:
        #return True
    #else:
        #return False
    
def check_permid(permission_id):
    # checking if the permission_id refer to a value permission
    
    # for testing purposes, create a sample dictionary
    dictionary_permid = {}
    dictionary_permid["permission_id"] = permission_id
    
    if permission_id == dictionary_permid["permission_id"]:
        return True
    else:
        return False

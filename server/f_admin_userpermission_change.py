def admin_userperm_change(token, u_id, permission_id):        
    if check_uid(u_id) == False:
        raise ValueError(f"Error, User ID does not refer to a valid user")
    if check_permid(permission_id) == False:
        raise ValueError(f"Error, Permission ID does not refer to a valid value permission")
    if permission_id != "1" or permission_id != "2":
        raise SystemError(f"Error, the user is not an Admin or Owner")
        # AccessError does not exist, SystemError for now as placeholder
    
    # Given u_id, set their perm to new permission_id
    dictionary["permission_id"] = permission_id       
    
    return_dictionary = {}
    
    return return_dictionary
    
def check_uid(u_id):
    # check if the u_id is valid
    if u_id == dictionary["u_id"]:
        return True
    else:
        return False
    
def check_permid(permission_id):
    # check if the permission_id refer to a value permission
    if permission_id == dictionary["permission_id"]:
        return True
    else:
        return False

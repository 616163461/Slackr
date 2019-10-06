<<<<<<< HEAD
# Function name: admin_userperm_change()
# Parameters: (token, u_id, permission_id)
# Return type: {}
=======
# Function: admin_userpermission_change()
# Parameters: (token, u_id, permission_id)
# Output: {}
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
# Exception: ValueError when:
# - u_id does not refer to a valid user
# - permission_id does not refer to a value permission
# AccessError when:
# - The authorised user is not an admin or owner
# Description: Given a User by their user ID, set their permissions to new permissions described by permission_id
<<<<<<< HEAD
# 

def admin_userperm_change(token, u_id, permission_id):        
    
    admin_userperm_change_dict = {}

    return admin_userperm_change_dict
=======
#

def admin_userperm_change(token, u_id, permission_id):
    pass
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128

# Function: admin_userpermission_change()
# Parameters: (token, u_id, permission_id)
# Output: {}
# Exception: ValueError when:
# - u_id does not refer to a valid user
# - permission_id does not refer to a value permission
# AccessError when:
# - The authorised user is not an admin or owner
# Description: Given a User by their user ID, set their permissions to new permissions described by permission_id
#

def admin_userperm_change(token, u_id, permission_id):
    pass

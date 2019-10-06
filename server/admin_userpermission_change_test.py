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

import pytest
from f_admin_userpermission_change import admin_userperm_change
from f_auth_register import auth_register
from f_auth_logout import auth_logout


def test_admin_userperm_change():
    
    # SETUP BEGIN   
    
    # Generate a valid user
    registerValidUserDict = auth_register("valid@email.com", "password", "Thom", "Browne")
    token = registerValidUserDict["token"]
    u_id = registerValidUserDict["u_id"]    
    permission_id = 1    
    
    # Generate an invalid user
    registerInvalidUserDictTwo = auth_register("valid2@email.com", "feelspecial", "Hwang", "Yeji")
    invalid_token = registerInvalidUserDictTwo["token"]
    invalid_uid = registerInvalidUserDictTwo["u_id"]
    invalid_permission_id = "a"
    
    # Invalidate the invalid user
    auth_logout(invalid_token)
    
    # SETUP END
    
    # Asserting that the default case works
    assert admin_userperm_change(token, u_id, permission_id) == {}
    
    # Testing that ValueError is raised when invalid parameters are passed
    with pytest.raises(ValueError, match = r"*"):
   
        # Testing function with an invalid token
        admin_userperm_change(invalid_token, u_id, permission_id)
        
        # Testing function with an invalid u_id
        admin_userperm_change(token, invalid_uid, permission_id)
        
    # Testing that SystemError is raised when invalid parameters are passed    
    with pytest.raises(SystemError):
    
        # Testing function with an invalid permission_id
        admin_userperm_change(token, u_id, invalid_permission_id)

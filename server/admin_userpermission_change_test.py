import pytest
from f_admin_userpermission_change import admin_userperm_change
from f_auth_register import auth_register
from f_auth_logout import auth_logout

def test_admin_userperm_change():
    
    # SETUP START   
    
    # Generate a valid user dictionary
    registerValidUserDict = auth_register("thom_browne@gmail.com", "password", "Thom", "Browne")
    token = registerValidUserDict["token"]
    u_id = registerValidUserDict["u_id"]    
    permission_id = 1    
    
    # Generate an invalid user dictionary
    registerInvalidUserDict = auth_register("hwang_yeji@gmail.com", "feelspecial", "Hwang", "Yeji")
    invalid_token = registerInvalidUserDict["token"]
    invalid_uid = registerInvalidUserDict["u_id"]
    invalid_permission_id = "a"
    
    # Invalidate the invalid user
    auth_logout(invalid_token)
    
    # SETUP END
    
    # Asserting that the default case works
    assert admin_userperm_change(token, u_id, permission_id) == {}
    
    # Testing that ValueError is raised when invalid parameters are passed
    with pytest.raises(ValueError, match = r"*"):
   
        # invalid token
        admin_userperm_change(invalid_token, u_id, permission_id)
        
        # invalid u_id
        admin_userperm_change(token, invalid_uid, permission_id)
        
    # Testing that SystemError is raised when invalid parameters are passed    
    with pytest.raises(SystemError):
    
        # invalid permission_id
        admin_userperm_change(token, u_id, invalid_permission_id)

import pytest
from f_admin_userpermission_change import admin_userperm_change
from f_auth_register import auth_register
from f_auth_logout import auth_logout

def test_admin_userperm_change():
    
    # SETUP START   
    
    registerValidUserDict = auth_register("thom_browne@gmail.com", "password", "Thom", "Browne")
    token = registerValidUserDict["token"]
    u_id = registerValidUserDict["u_id"]    
    permission_id = 1    
    
    invalid_first_name = "thisnameiswaytoolongforafirstnamesoitreturnsvalueerror"
    invalid_last_name = "thisnameiswaytoolongforalastnamesoitreturnsvalueerror"
    
    registerInvalidUserDict = auth_register("hwang_yeji@gmail.com", "feelspecial", "Hwang", "Yeji")
    invalid_token = registerInvalidUserDict["token"]
    invalid_uid = registerInvalidUserDict["u_id"]
    invalid_permission_id = "a"
    
    auth_logout(invalid_token)
    
    # SETUP END
    
    # Asserting that default case works
    assert admin_userperm_change(token, u_id, permission_id) == {}
    
    with pytest.raises(ValueError, match = r"*"):
   
        # invalid token
        admin_userperm_change(invalid_token, u_id, permission_id)
        # invalid u_id
        admin_userperm_change(token, invalid_uid, permission_id)
        
    with pytest.raises(SystemError):
    
        # invalid permission_id
        admin_userperm_change(token, u_id, invalid_permission_id)

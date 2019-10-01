import pytest
from f_admin_userpermission_change import admin_userperm_change

def test_admin_userperm_change():
    valid_uid = "thom_browne@gmail.com"
    valid_token = "1password1"    
    valid_permission_id = "1"
    
    assert admin_userperm_change(valid_token, valid_uid, valid_permission_id)

def test_bad_admin_userperm_change():
    valid_uid = "thom_browne@gmail.com"
    valid_token = "1password1"    
    valid_permission_id = "1"

    invalid_uid = "ihearttrimesters"
    invalid_token = "password"
    invalid_permission_id = "1337"
    
    with pytest.raises(ValueError):
        # invalid token
        admin_userperm_change(invalid_token, valid_uid, valid_permission_id)
        # invalid u_id
        admin_userperm_change(invalid_token, valid_uid, valid_permission_id)
        
    with pytest.raises(SystemError):
        # invalid permission_id
        admin_userperm_change(valid_token, valid_uid, invalid_permission_id)

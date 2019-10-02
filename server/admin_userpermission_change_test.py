import pytest
from f_admin_userpermission_change import admin_userperm_change
from f_auth_register import auth_register

def test_admin_userperm_change():
   
    registerValidDict = auth_register("thom_browne@gmail.com", "password", "Thom", "Browne")
    valid_token = registerValidDict["token"]
    valid_uid = registerValidDict["u_id"]    
    valid_permission_id = 1
    
    assert admin_userperm_change(valid_token, valid_uid, valid_permission_id) == {}

def test_bad_admin_userperm_change():

    registerValidDict = auth_register("thom_browne@gmail.com", "password", "Thom", "Browne")
    valid_token = registerValidDict["token"]
    valid_uid = registerValidDict["u_id"]    
    valid_permission_id = 1

    
    with pytest.raises(ValueError):
        registerInvalidDict = auth_register("ihearttrimesters", "t", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf")
        invalid_token = registerInvalidDict["token"]
        invalid_uid = registerInvalidDict["u_id"]
        invalid_permission_id = "a"
        # invalid token
        admin_userperm_change(invalid_token, valid_uid, valid_permission_id)
        # invalid u_id
        admin_userperm_change(valid_token, invalid_uid, valid_permission_id)
        # invalid permission_id
        admin_userperm_change(valid_token, valid_uid, invalid_permission_id)
        
    with pytest.raises(SystemError):
        invalid_permid = 3
        # invalid permission_id
        admin_userperm_change(valid_token, valid_uid, invalid_permid)

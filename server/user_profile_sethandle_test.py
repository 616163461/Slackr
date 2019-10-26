# Function name: user_profile_sethandle()
# Parameters: (token, handle_str)
# Return value: {}
# Exception: ValueError when: 
# - handle_str is no more than 20 characters
# Description: Update the authorised user's handle (i.e. display name)
#

import pytest
from f_user_profile_sethandle import user_profile_sethandle
from f_auth_register import auth_register
from f_auth_logout import auth_logout
import json

# retrieve data from local data base 
def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

def test_user_profile_sethandle():
    # SETUP BEGIN
    handle_str_good = "thisismorethantwentycharacters"
    handle_str_bad =  "goodhandle"
    handle_str_max = "hithisis20characters"
    
    validAuthRegisterDic = auth_register("valid@email.com", "validpassword", "Richard", "Jiang")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    invalidAuthRegisterDicTwo = auth_register("valid2@email.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDicTwo['token']
    invalid_u_id = invalidAuthRegisterDicTwo['u_id']
    # Invalidates token
    auth_logout(invalid_token)
    # SETUP END
    
    # Testing successful run (default case)
    assert user_profile_sethandle(token, handle_str_good) == {}
    
    # checking name is changed in local data base
    handle_set = False
    data = getData()
    for users in data['users']:
        if users['token'] == token:
            if users['handle_str'] == handle_str_good:
                handle_set = True

    if handle_set == False: 
        raise ValueError(f"Handle set unsuccessful...\n")
        
    # Testing maximum case of handle_str
    assert user_profile_sethandle(token, handle_str_max) == {}
    
    # checking name is changed in local data base
    handle_set = False
    data = getData()
    for users in data['users']:
        if users['token'] == token:
            if users['handle_str'] == handle_str_max:
                handle_set = True

    if handle_set == False: 
        raise ValueError(f"Handle set unsuccessful...\n")
    
    with pytest.raises(ValueError):
        # Testing good token, with bad handle_str
        user_profile_sethandle(token, handle_str_bad)
        # Testing bad token, with good handle_str
        user_profile_sethandle(invalid_token, handle_str_good)
        # Testing both bad token and bad handle_str
        user_profile_sethandle(invalid_token, handle_str_bad)

        
        
    


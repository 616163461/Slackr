# Function: auth_logout()
# Parameters: (token)
# Return type: {}
# Exception: N/A
# Description: Given an active token, invalidates the taken to log the user out. Given a non-valid token, does nothing
#

import pytest
from f_auth_login import auth_login
from f_auth_register import auth_register
from f_auth_logout import auth_logout
from myexcept import ValueError
from json_clean import jsonClean
import json

# retrieve data from local data base 
def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

def test_auth_logout(): 
    jsonClean()
    # SETUP BEGIN
    
    authRegisterDic = auth_register("valid13@email.com", "valid13password", "first13name", "last13name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SETUP END
    
    with pytest.raises(ValueError): 
        # Testing login function with user which hasn't been logged out
        auth_login("valid13@email.com", "valid13password")
    # auth_login does not check to see if the user is already logged in!
    auth_logout(token)
    data = getData()
    
    # checking that the token is invalidated 
    token_invalidated = False
    for users in data['users']:
        if u_id == users['u_id']:
            if users['token'] == None:
                token_invalidated = True
    
    if token_invalidated == False:
        raise ValueError(f"Logout unsuccessful...\n")
    
    # Testing login function with logged out user to check he's succesfully logged out 
    auth_login("valid13@email.com", "valid13password")
    
    auth_logout(token)
    # Testing logout function with a logged out user 
    with pytest.raises(ValueError):
        assert auth_logout(token) == {}
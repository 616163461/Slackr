# Function: auth_login()
# Parameters: (email, password)
# Return type:
# Exception: Value Error when: 
# - Email entered is not a valid email
# - Email entered does not belong to a user
# - Password is not correct
# Description: Given a registered users' email and password
# and generates a valid token for the user to remain authenticated
#

import pytest
from f_auth_login import auth_login
from f_auth_register import auth_register
from f_auth_logout import auth_logout
import json

# retrieve data from local data base 
def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

def test_auth_login():
    
    # SETUP BEGIN
    
    authRegisterDic = auth_register("valid10@email.com", "valid10password", "first10name", "last10name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SETUP END
    
    with pytest.raises(ValueError): 
        # Testing function with account which hasn't been logged out 
        auth_login("valid10@email.com", "valid10password")
     
    # Testing function with account which has been logged out 
    auth_logout(token)

    authLoginDic = auth_login("valid10@email.com", "valid10password")
    token = authLoginDic['token']
    u_id = authLoginDic['u_id']
    
    # checking the token matches the token in the database
    token_valid = False
    for users in data['users']:
        if u_id == users['u_id']:
            if users['token'] == token:
                token_valid = True
    
    if token_valid == False:
        raise ValueError(f"Login unsuccessful...\n")
        
    # Testing if we can logout using new token
    auth_logout(token)
    
    
def test_auth_login_bad():
    
    # SETUP BEGIN
    
    authRegisterDic = auth_register("valid@11email.com", "valid11password", "first11name", "last11name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    authRegisterDicOne = auth_register("valid12@email.com", "valid12password", "first12name", "last12name")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    
    # SETUP END
    
    with pytest.raises(ValueError):
        # Testing function with invalid email
        auth_login("invalidemail", "validpassword")
        # Testing function with invalid password
        auth_login("valid11@email.com", "invalidpassword")
        # Testing function with incorrect password
        auth_login("valid12@email.com", "incorrectpassword")
        # Testing function with incorrect email
        auth_login("valid2@email.com", "validpassword")
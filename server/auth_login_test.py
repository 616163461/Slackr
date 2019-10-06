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

def test_auth_login():
    
    # SETUP BEGIN
    
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SETUP END
    
    with pytest.raises(ValueError): 
        # Testing function with account which hasn't been logged out 
        auth_login("validemail", "validpassword")
     
    # Testing function with account which has been logged out 
    auth_logout(token)

    authLoginDic = auth_login("validemail", "validpassword")
    token = authLoginDic['token']
    u_id = authLoginDic['u_id']
    
    # Testing if we can logout using new token
    auth_logout(token)
    
    
def test_auth_login_bad():
    
    # SETUP BEGIN
    
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    authRegisterDicOne = auth_register("valid2@email.com", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    
    # SETUP END
    
    with pytest.raises(ValueError):
        # Testing function with invalid email
        auth_login("invalidemail", "validpassword")
        # Testing function with invalid password
        auth_login("valid@email.com", "invalidpassword")
        # Testing function with incorrect password
        auth_login("valid@email.com", "incorrectpassword")
        # Testing function with incorrect email
        auth_login("valid2@email.com", "validpassword")

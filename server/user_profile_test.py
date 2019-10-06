# Function: user_profile()
# Parameter: (token, u_id)
# Output: { email, name_first, name_last, handle_str }
# Exception: ValueError when: 
# - User with u_id is not a valid user
# Description: For a valid user, returns information about their email, first name, last name, and handle
#

import pytest
from f_user_profile import user_profile
from f_auth_register import auth_register
from f_auth_logout import auth_logout

def test_user_profile():

    # SETUP BEGIN
    validAuthRegisterDic = auth_register("valid@email.com", "validpassword", "Richard", "Jiang")
    goodtoken = validAuthRegisterDic['token']
    goodu_id = validAuthRegisterDic['u_id']
    
    invalidAuthRegisterDic = auth_register("valid2@email.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDic['token']
    auth_logout(invalid_token) #Creates an Invalid Token
    badu_id = "invaliduserid"
    # SETUP END
    
    assert  user_profile(goodtoken, goodu_id) == {'email' : "valid@email.com", 'name_first' : "Richard", 'name_last' : "Jiang", 'handle_str' : "Faerid"}
    # In Iteration 1, auth_register doesn't let you set a handle_str...
    # Assume handle_str is "Faerid" in this scenario
    
    with pytest.raises(ValueError):
        # Testing a bad token with a good user_id
        user_profile(invalid_token, goodu_id)
        # Testing a good token with a bad user_id
        auth_profile(invalid_token, badu_id)
        # Testing both a bad token and bad user_id
        auth_profile(invalid_token, badu_id)
        

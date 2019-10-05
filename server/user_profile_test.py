#Function: user_profile
#Parameter: (token, u_id)
#Output: {email, name_first, name_last, handle_str}
#ValueError: User with u_id is not a valid user
#Description: For a valid user, returns information about their email, first name, last name, and handle

import pytest
from f_user_profile import user_profile
from f_auth_register import auth_register
from auth

def test_user_profile():

    #BEGIN SET UP
    validAuthRegisterDic = auth_register("richard123@gmail.com", "validpassword", "Richard", "Jiang")
    token = authRegisterDic['token']
    goodu_id = authRegisterDic['u_id']
    
    invalidAuthRegisterDic = auth_register("richard2@gmail.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDic['token']
    invalid_u_id = invalidAuthRegisterDic['u_id']
    auth_logout(invalid_token) #Creates an Invalid Token
    badu_id = "invaliduserid"
    #SET UP END
    
    assert  user_profile(goodtoken, goodu_id) == {'email' : "richardjiang123@gmail.com", 'name_first' : "Richard", 'name_last' : "Jiang", 'handle_str' : "Faerid"}
    #In Iteration 1, auth_register doesn't let you set a handle_str...
    #Assume handle_str is "Faerid" in this scenario
    
    with pytest.raises(ValueError):
        #Testing a bad token with a good user_id
        user_profile(badtoken, goodu_id)
        #Testing a good token with a bad user_id
        auth_login(goodtoken, badu_id)
        #Testing both a bad token and bad user_id
        auth_login(badtoken, badu_id)
        

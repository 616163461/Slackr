# Function name: user_profile_setemail
# Parameters: (token, email)
# Return: {}
# Exception: ValueError when:
# - handle_str is no more than 20 characters
# Description: Update the authorised user's email address
#

import pytest
from f_user_profile_setemail import user_profile_setemail
from f_auth_register import auth_register
from f_auth_logout import auth_logout
import json

# retrieve data from local data base 
def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data
    
def test_user_profile_setemail():
    # SETUP BEGIN
    validAuthRegisterDic = auth_register("valid@email.com", "validpassword", "Richard", "Jiang")
    token = validAuthRegisterDic['token']
    u_id = validAuthRegisterDic['u_id']
    email_good = "valid@email.com"
    
    invalidAuthRegisterDicTwo = auth_register("valid2@email.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDicTwo['token']
    invalid_u_id = invalidAuthRegisterDicTwo['u_id']
    email_bad = "bademail"
    auth_logout(invalid_token)
    # SETUP END
    # Default testing
    assert user_profile_setemail(token, email_good) == {}
    
    # checking that email was set
    email_set = False
    data = getData()
    for users in data['users']:
        if users['token'] == token:
            if users['email'] == email_good:
                email_set = True
                
    if email_set == False:
        raise ValueError(f"Email set was unsuccessful...\n")
    
    with pytest.raises(ValueError):
        # Testing user_profile_setemail with invalid token
        user_profile_setemail(invalid_token, email_good)
        # Testing user_profile_setemail with invalid token
        user_profile_setemail(token, email_bad)
        # Testing user_profile_setemail with invalid token and bad email
        user_profile_setemail(invalid_token, email_bad)
        # Testing user_profile_setemail with valid token and error email
        user_profile_setemail(invalid_token, email_bad)
        # Haven't implemented: ValueError when email address is already being used by another user

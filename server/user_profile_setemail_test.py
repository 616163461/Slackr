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
from myexcept import ValueError, AccessError
from json_clean import jsonClean

def test_user_profile_setemail():
    jsonClean()
    # SETUP BEGIN
    validAuthRegisterDic = auth_register("valid20@email.com", "valid20password", "first20name", "last20name")
    token = validAuthRegisterDic['token']
    u_id = validAuthRegisterDic['u_id']
    email_good = "valid222@email.com"
    email_good_new = "valid333@email.com"
    
    invalidAuthRegisterDicTwo = auth_register("valid2@email.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDicTwo['token']
    invalid_u_id = invalidAuthRegisterDicTwo['u_id']
    email_bad = "bademail"
    auth_logout(invalid_token)
    # SETUP END
    # Default testing
    assert user_profile_setemail(token, email_good) == {}
    
    with pytest.raises(ValueError):
        # Testing user_profile_setemail with invalid token
        user_profile_setemail(invalid_token, email_good_new)
        # Testing user_profile_setemail with invalid token
        user_profile_setemail(token, email_bad)
        # Testing user_profile_setemail with invalid token and bad email
        user_profile_setemail(invalid_token, email_bad)
        # Testing user_profile_setemail with valid token and error email
        user_profile_setemail(invalid_token, email_bad)
        # Haven't implemented: ValueError when email address is already being used by another user
    
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

def test_user_profile_setemail():
    # SETUP BEGIN
    validAuthRegisterDic = auth_register("richard123@gmail.com", "validpassword", "Richard", "Jiang")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    email_good = "richard123@gmail.com"
    
    invalidAuthRegisterDicTwo = auth_register("richard3@gmail.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDicTwo['token']
    invalid_u_id = invalidAuthRegisterDicTwo['u_id']
    email_bad = "rich"
    auth_logout(invalid_token)
    # SETUP END
    # Default testing
    assert user_profile_setemail(token, email_good) == {}
    
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

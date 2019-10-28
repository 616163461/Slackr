# Function name: auth_register()
# Parameters: (email, password, name_first, name_last)
# Return type: { u_id, token }
# Exception: ValueError when:
# - Email entered is not a valid email.
# - Email address is already being used by another user
# - Password entered is not a valid password
# - name_first is more than 50 characters
# - name_last is more than 50 characters
# Description: Given a user's first and last name, email address, and password, 
# create a new account for them and return a new token for authentication in their session
#

import pytest
from f_auth_register import auth_register
from f_auth_logout import auth_logout
from f_auth_login import auth_login
from myexcept import ValueError

def test_auth_register(): 

    # SETUP BEGIN

    authRegisterDic = auth_register("valid9@email.com", "valid9password", "first9name", "last9name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SETUP END
    
    # Testing auth_logout function to check that I successfully registered
    auth_logout(token)
    
    # Testing auth_login function to check that the account was successfully registered
    auth_login("valid9@email.com", "valid9password")
    
    
def test_auth_register_bad(): 
    
    # SETUP BEGIN

    authRegisterDic = auth_register("valid7@email.com", "valid7password", "first7name", "last7name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    authRegisterDic_one = auth_register("valid8@email.com", "valid8password", "first8name", "last8name")
    token_one = authRegisterDic_one['token']
    u_id_one = authRegisterDic_one['u_id']
    
    # SETUP END

    with pytest.raises(ValueError):
        # Testing function with invalid email 
        auth_register("invalidemail", "validpassword1", "firstname1", "lastname1")
        # Testing function with already registered email
        auth_register("valid@email.com", "validpassword1", "firstname1", "lastname1") 
        # Testing function with invalid password
        auth_register("valid2@email.com", "ivp", "firstname1", "lastname1")
        # Testing function with invalid first_name
        auth_register("valid2@email.com", "validpassword1", "firstnameiswayyyyyyyyyytoooooooooooooolongsounforunatelyitwillcauseanerror", "lastname1")
        # Testing function with invalid last_name
        auth_register("valid2@email.com", "validpassword1", "firstname1", "lastnameiswayyyyyyyyyytoooooooooooooolongsounforunatelyitwillcauseanerror")
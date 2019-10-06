# Function: user_profile_setname
# Parameters: (token, name_first, name_last)
# Return value: {}
# Exception: ValueError when: 
# - name_first is more than 50 characters
# - name_last is more than 50 characters
# Description: Update the authorised user's first and last name

import pytest
from f_user_profile_setname import user_profile_setname
from f_auth_register import auth_register
from f_auth_logout import auth_logout

def test_user_profile_setname():
    # SETUP BEGIN
    name_first_bad = "exam1exam2exam3exam4exam5exam6exam7exam8exam9exam10"
    name_last_bad = "exam1exam2exam3exam4exam5exam6exam7exam8exam9exam10"
    name_first_good = "Richard" 
    name_last_good = "Jiang"
    
    
    validAuthRegisterDic = auth_register("richard123@gmail.com", "validpassword", "Richard", "Jiang")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']

   
    invalidAuthRegisterDicTwo = auth_register("richard1@gmail.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDicTwo['token']
    invalid_u_id = invalidAuthRegisterDicTwo['u_id']
    # Invalidates token
    auth_logout(invalid_token)
    
    # SETUP END
    # Testing the default case
    assert user_profile_setname(token, name_first_good, name_last_good) == {}
    
    with pytest.raises(ValueError):
        # Testing user_profile_setname with bad name_first
        user_profile_setname(token, name_first_bad, name_last_good)
        # Testing user_profile_setname with bad name_last
        user_profile_setname(token, name_first_good, name_last_bad)
        # Testing user_profile_setname with both bad name_first and name_last
        user_profile_setname(token, name_first_bad, name_last_bad)
        # Testing user_profile_setname with a bad token
        user_profile_setname(invalid_token, name_first_good, name_last_good)
      

        
        

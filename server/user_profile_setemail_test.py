#Function name: user_profile_setemail
#Parameters: token, email
#Return: {}
#ValueError when: Email entered is not a valid email, Email address is already being used by another user
#Description: Update the authorised user's email address

from f_user_profile_setemail import user_profile_setemail
from f_auth_register import auth_register
from f_auth_logout import auth_logout

def test_user_profile_setemail():
    #SET UP BEGIN
    validAuthRegisterDic = auth_register("richard123@gmail.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    email_good = "richard123@gmail.com"
    
    invalidAuthRegisterDic = auth_register("richard123@gmail.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDic['token']
    invalid_u_id = invalidAuthRegisterDic['u_id']
    email_bad = "rich"
    auth_logout(invalid_token)
    #SET UP END
    #Default testing
    assert user_profile_setemail(token, email_good) == {}
    
    with pytest.raises(ValueError):
        #testing user_profile_setemail with invalid token
        user_profile_setemail(invalid_token, email_good)
        #testing user_profile_setemail with invalid token
        user_profile_setemail(token, email_bad)
        #testing user_profile_setemail with invalid token and bad email
        user_profile_setemail(invalid_token, email_bad)
        #testing user_profile_setemail with valid token and error email
        user_profile_setemail(invalid_token, email_bad)
        # Haven't implemented: ValueError when email address is already being used by another user

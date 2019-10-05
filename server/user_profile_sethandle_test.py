#Function name: user_profile_sethandle
#Parameters: (token, handle_str)
#Return value: {}
#Value Error: handle_str is no more than 20 characters
#Description: Update the authorised user's handle (i.e. display name)

from f_user_profile_sethandle import user_profile_sethandle
from f_auth_register import auth_register
from f_auth_logout import auth_logout

def user_profile_sethandle_test():
    #SET UP BEGIN
    handle_str_good = "thisismorethantwentycharacters"
    handle_str_bad =  "goodhandle"
    handle_str_max = "hithisis20characters"
    
    validAuthRegisterDic = auth_register("richard123@gmail.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']

   
    invalidAuthRegisterDic = auth_register("richard123@gmail.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDic['token']
    invalid_u_id = invalidAuthRegisterDic['u_id']
    auth_logout(invalid_token) #Creates an Invalid Token
    #SET UP END
    
    #Testing successful run (default case)
    assert user_profile_sethandle(token, handle_str_good) == {}
    #Testing maximum case of handle_str
    assert user_profile_sethandle(token, handle_str_max) == {}
    
    with pytest.raises(ValueError):
        #Testing good token, with bad handle_str
        user_profile_sethandle(token, handle_str_bad)
        #Testing bad token, with good handle_str
        user_profile_sethandle(invalid_token, handle_str_good)
        #Testing both bad token and bad handle_str
        user_profile_sethandle(invalid_token, handle_str_bad)

        
        
    


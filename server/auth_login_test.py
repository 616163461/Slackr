import pytest
from f_auth_login import auth_login
from f_auth_register import auth_register
from f_auth_logout import auth_logout

def test_auth_login(): 
    # SET UP BEGIN
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END
    with pytest.raises(ValueError): 
        # calling function with account which hasn't been logged out 
        auth_login("validemail", "validpassword")
     
    auth_logout(token)
    # calling function with account which has been logged out 
    authLoginDic = auth_login("validemail", "validpassword")
    token = authLoginDic['token']
    u_id = authLoginDic['u_id']
    
    # checking we can logout using new token
    auth_logout(token)
    
    
def test_auth_login_bad():
    
     # SET UP BEGIN
    authRegisterDic = auth_register("validemail", "validpassword")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    authRegisterDic1 = auth_register("validemail1", "validpassword1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    
    # SET UP END
    
    with pytest.raises(ValueError):
        # calling function with invalid email
        auth_login("invalidemail", "validpassword")
        # calling function with invalid password
        auth_login("validemail", "invalidpassword")
        # calling function with incorrect password
        auth_login("validemail", "incorrectpassword")
        # calling function with incorrect email
        auth_login("validemail1", "validpassword")
        
        

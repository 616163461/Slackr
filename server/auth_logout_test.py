import pytest
from f_auth_login import auth_login
from f_auth_register import auth_register
from f_auth_logout import auth_logout


def test_auth_logout(): 
    # SET UP BEGIN
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END
    
    with pytest.raises(ValueError): 
        # calling login function with user which hasn't been logged out
        auth_login("validemail", "validpassword")
        
    auth_logout(token)
    # calling login function with logged out user to check he's succesfully logged out 
    auth_login("validemail", "validpassword")
    
    auth_logout(token)
    # calling logout function with a logged out user 
    assert auth_logout(token) == {}
    


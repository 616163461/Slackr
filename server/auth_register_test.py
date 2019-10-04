import pytest
from f_auth_register import auth_register
   
def test_auth_register(): 
    
    # SET UP BEGIN
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END
    
    # calling auth_logout function to check that I successfully registered
    auth_logout(token)
    
    # calling auth_login function to check that the account was successfully registered
    auth_login("valid@email", "validpassword")
    
    
    
def test_auth_register_bad(): 
    
    # SET UP BEGIN
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SET UP END
    
    with pytest.raises(ValueError):
        # calling function with invalid email 
        auth_register("invalidemail", "validpassword1", "firstname1", "lastname1")
        # calling function with already registered email
        auth_register("valid@email", "validpassword1", "firstname1", "lastname1") 
        # calling function with invalid password
        auth_register("valid@email1", "ivp", "firstname1", "lastname1")
        # calling function with invalid first_name
        auth_register("valid@email1", "validpassword1", "firstnameiswayyyyyyyyyytoooooooooooooolongsounforunatelyitwillcauseanerror", "lastname1")
        # calling function with invalid last_name
        auth_register("valid@email1", "validpassword1", "firstname1", "lastnameiswayyyyyyyyyytoooooooooooooolongsounforunatelyitwillcauseanerror")
        
        
        

        
        
        
        
        
        
        
        

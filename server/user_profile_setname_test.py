#user_profile_setname
#Parameters: (token, name_first, name_last)
#Return value: {}
#ValueError: ValueError when: name_first is more than 50 characters, name_last is more than 50 characters
#Description: Update the authorised user's first and last name

def test_user_profile_setname():
    #SET UP BEGIN
    name_first_bad = "exam1exam2exam3exam4exam5exam6exam7exam8exam9exam10"
    name_last_bad = "exam1exam2exam3exam4exam5exam6exam7exam8exam9exam10"
    name_first_good = "Richard" 
    name_last_good = "Jiang"
    
    
    validAuthRegisterDic = auth_register("richard123@gmail.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']

   
    invalidAuthRegisterDic = auth_register("richard123@gmail.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDic['token']
    invalid_u_id = invalidAuthRegisterDic['u_id']
    auth_logout(invalid_token)
    
    #SET UP END
   
    with pytest.raises(ValueError):
        #testing user_profile_setname with bad name_first
        user_profile_setname(token, name_first_bad, name_last_good)
        #testing user_profile_setname with bad name_last
        user_profile_setname(token, name_first_good, name_last_bad)
        #testing user_profile_setname with both bad name_first and name_last
        user_profile_setname(token, name_first_bad, name_last_bad)
        #testing user_profile_setname with a bad token
        user_profile_setname(invalid_token, name_first_good, name_last_good)
      

        
        

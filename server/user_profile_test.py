import pytest
from f_user_profile import user_profile

def test_user_profile():
    goodu_id = "richardjiang2@gmail.com"
    badu_id = "richardjiang123@gmail.com"
    
    goodtoken = "12345678"
    badtoken = "2345671"
    
    assert  user_profile(goodtoken, goodu_id) == {'email' : "richardjiang2@gmail.com", 'name_first' : "Richard", 'name_last' : "Jiang", 'handle_str' : "Faerid"}
    

def test_user_profile_bad():
    with pytest.raises(ValueError):
    
        goodu_id = "richardjiang2@gmail.com"
        badu_id = "richardjiang123@gmail.com"
        
        goodtoken = "12345678"
        badtoken = "2345671"
        #bad token
        user_profile(badtoken, goodu_id)
        #bad id
        auth_login(goodtoken, badu_id)
        #both bad token and bad id
        auth_login(badtoken, badu_id)

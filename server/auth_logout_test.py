from f_auth_logout import auth_logout

def test_auth_logout(): 
    #characters
    assert auth_logout("1richardkang") == "richardkang"
    #numbers
    assert auth_logout("143124") == "43124"
    #spaces
    assert auth_logout("1 ahklsdf") == " ahklsdf"
    
    #I'm not sure how to assert these cases since there's no return
    auth_logout("richardkang")
    auth_logout("43124")
    auth_logout(" ahklsdf")

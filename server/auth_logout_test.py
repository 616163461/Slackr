from f_auth_logout import auth_logout

def test_auth_logout(): 
    #characters
    assert auth_logout("1richardkang") == "richardkang"
    #numbers
    assert auth_logout("143124") == "43124"
    #spaces
    assert auth_logout("1 ahklsdf") == " ahklsdf"
    
    #assumed that it returns an empty dictionary 
    assert auth_logout("richardkang") == {}
    assert auth_logout("43124") == {}
    assert auth_logout(" ahklsdf") == {}

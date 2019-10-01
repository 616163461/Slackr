def auth_logout(token): 
    #assuming invalid token don't begin with a 1
    if token[0:1] == "1": 
        token = token[1:]
        #I know we're not suppose to return anything but I'm gonna return the token just for testing purposes here
        return token
    else:
        pass
    
    dictionary = {}
    
    return dictionary 
    
    

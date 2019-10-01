

def user_profile(token, u_id):

    if u_id == "richardjiang123@gmail.com": #Should be in the database, if not, return error
        raise ValueError(f"Error, please enter a valid u_id")
        
    if token == "2345671": #Should be a valid token, if not, return error
        raise ValueError(f"Error, please enter a valid token")
        
    userDictionary = {}
    userDictionary["email"] = "richardjiang2@gmail.com"
    userDictionary["name_first"] = "Richard"
    userDictionary["name_last"] = "Jiang"
    userDictionary["handle_str"] = "Faerid"
    return userDictionary

    

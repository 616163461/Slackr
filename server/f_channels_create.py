def channels_create(token, name, is_public): 
    if len(name) > 20: 
        raise ValueError(f"Error, name needs to be shorter than 20 characters")
    dictionary = {}
    dictionary["channel_id"] = 12345
    return dictionary
    

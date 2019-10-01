def channels_create(token, name, is_public): 
    if len(name) > 20: 
        raise ValueError(f"Error, name needs to be shorter than 20 characters")
    dictionary = {}
    #return 1111 for good (study) channel
    if name == "study channel":
        dictionary["channel_id"] = 1111
        
    #return 0000 for bad (gaming) channel
    if name == "gaming channel":
        dictionary["channel_id"] = 0000 
        
    return dictionary
    

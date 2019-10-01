def channel_invite(token, channel_id, u_id):
    #if channel_id does not refer to a valid channel that the authorised user is part of
    if channel_id == 0000:
        raise ValueError(f"error, channel_id does not refer to a valid channel that the authorised user is part of")
    if u_id == "bad u_id":
        raise ValueError(f"error, u_id does not refer to a valid user")
    
    dictionary = {}
    
    return dictionary

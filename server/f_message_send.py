from f_auth_register import auth_register

def send_message(token, channel_id, message):
    # message > 1000 characters
    if len(message) > 1000:
        raise ValueError(f"Error, message is longer than 1000 characters")
    # channel ID not valid
    if check_channelid(channel_id) == False:
        raise ValueError(f"Error, channel does not exist")
        
    # send a message from authorised_user to the channel specified by channel_id    
    authorisedUserDict = auth_register("thombrowne@gmail.com", "feelspecial", "Thom", "Browne")
    
    if token == "1feelspecial":
        print(message)
    
    return_dict = {}
    
    return return_dict
    
def check_channelid(channel_id):
    # sample dictionary for testing purposes
    dictionary = {}
    dictionary["channel_id"] = channel_id
    
    if channel_id == dictionary["channel_id"]:
        return True
    else:
        return False

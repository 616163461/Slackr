import pytest
from f_channel_invite import channel_invite
from f_auth_register import auth_register
from f_channels_create import channels_create

def test_channel_invite(): 
    # SET UP BEGIN 
    dictionary = auth_register("geoffrey.he777@gmail.com", "Bigpabo", "Geoffrey", "He")
    u_id = "valid u_id"
    token = dictionary["token"]
    
    channel = channels_create(token, "study channel", True)
    channel_id = channel["channel_id"]
    # SET UP END 
    
    assert channel_invite(token, channel_id, u_id) == {}
    
def test_channel_invite_bad(): 
    # SET UP BEGIN 
    dictionary = auth_register("geoffrey.he777@gmail.com", "Bigpabo", "Geoffrey", "He")
    u_id = "valid u_id"
    token = dictionary["token"]
    
    channel = channels_create(token, "gaming channel", True)
    channel_id = channel["channel_id"]
    # SET UP END 
    
    #case where channel id does not refer to a valid channel that the authorised user is part of
    with pytest.raises(ValueError, match = r"*"):
        channel_invite(token, channel_id, u_id) 
        
    # SET UP BEGIN 
    dictionary = auth_register("geoffrey.he777@gmail.com", "Bigpabo", "Geoffrey", "He")
    u_id = "bad u_id"
    token = dictionary["token"]
    
    channel = channels_create(token, "study channel", True)
    channel_id = channel["channel_id"]
    # SET UP END 
    
    #case where the u_id does not refer to a valid user
    with pytest.raises(ValueError, match = r"*"): 
        channel_invite(token, channel_id, u_id)

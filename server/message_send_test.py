import pytest
from f_message_send import message_send
from f_auth_register import auth_register
from f_channels_create import channels_create

def test_message_send():

    # SETUP START

    # Generate a valid user and a valid channel for "channel_id"
    registerValidUserDict = auth_register("hwangyeji@gmail.com", "feelspecial", "Hwang", "Yeji")
    token = registerValidUserDict["token"]
    createValidChannelDict = channels_create(token, "validchannel", True)
    channel_id = createValidChannelDict["channel_id"]
    message = "I Heart Hwang Yeji"

    # Generate an invalid user and an invalid "channel_id"
    registerInvalidUserDict = auth_register("kangdaniel@gmail.com", "password", "Kang", "Daniel")
    invalid_token = registerInvalidUserDict["token"]
    createInvalidChannelDict = channels_create(invalid_token, "invalidchannel", True)
    invalid_channelid = createInvalidChannelDict["channel_id"]
    invalid_message = 0
    
    # Invalidate the invalid user
    auth_logout(invalid_token)
    
    # SETUP END 
    
    # Asserting that the default case works
    assert message_send(token, channel_id, message) == {}
    
    # Testing that ValueError is raised when invalid parameters are passed
    with pytest.raises(ValueError, match = r"*"): 

        # invalid token
        message_send(invalid_token, channel_id, message)
        
        # invalid channel id
        message_send(token, invalid_channelid, message)
        
        # invalid message
        message_send(token, channel_id, invalid_message)

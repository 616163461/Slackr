import pytest
from f_message_sendlater import message_sendlater
from f_auth_register import auth_register
from f_channels_create import channels_create

def test_send_message_later():

    # SETUP START
    
    # Generate a valid user, valid message, and valid timesent
    registerValidUserDict = auth_register("thom_browne@gmail.com", "password", "Thom", "Browne")
    token = registerValidUserDict["token"]
    createValidChannelDict = channels_create(token, "validchannel", True)
    channel_id = createValidChannelDict["channel_id"]
    message = "I Heart Thom Browne"
    timesent = "20/10/2020"
    
    # Generate an invalid user, invalid message, and invalid timesent
    registerInvalidUserDict = auth_register("gmail@gmail.com", "password", "Thom", "Browne")
    invalid_token = registerInvalidUserDict["token"]
    createInvalidChannelDict = channels_create(invalid_token, "invalidchannel", True)
    invalid_channelid = createInvalidChannelDict["channel_id"]
    invalid_message = 0
    invalid_timesent = "20/10/1999"
    
    # Invalidate the invalid user
    auth_logout(invalid_token)
    
    # SETUP END
    
    # Asserting that the default case works
    assert message_sendlater(token, channel_id, message, timesent) == {}
    
    # Testing that ValueError is raised when invalid parameters are passed
    with pytest.raises(ValueError, match = r"*"):
        
        # invalid token
        message_sendlater(invalid_token, channel_id, message, timesent)
        
        # invalid channel id
        message_sendlater(token, invalid_channelid, message, timesent)
        
        # invalid message
        message_sendlater(token, channel_id, invalid_message, timesent)
        
        # invalid timesent input
        message_sendlater(token, channel_id, message, invalid_timesent)

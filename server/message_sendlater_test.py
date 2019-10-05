import pytest
from f_message_sendlater import send_message_later
from f_auth_register import auth_register

def test_send_message_later():

    # SETUP START
    
    # Generate a valid user, valid message, and valid timesent
    registerValidUserDict = auth_register("thom_browne@gmail.com", "password", "Thom", "Browne")
    token = registerValidUserDict["token"]
    channel_id = 1337
    message = "I Heart Thom Browne"
    timesent = "20/10/2020"
    
    # Generate an invalid user, invalid message, and invalid timesent
    registerInvalidUserDict = auth_register("gmail@gmail.com", "password", "Thom", "Browne")
    invalid_token = registerInvalidUserDict["token"]
    invalid_channelid = "notavalidchannelid"
    invalid_message = 0
    invalid_timesent = "20/10/1999"
    
    # Invalidate the invalid user
    auth_logout(invalid_token)
    
    # SETUP END
    
    # Asserting that the default case works
    assert send_message_later(token, channel_id, message, timesent) == {}
    
    # Testing that ValueError is raised when invalid parameters are passed
    with pytest.raises(ValueError, match = r"*"):
        
        # invalid token
        send_message_later(invalid_token, channel_id, message, timesent)
        
        # invalid channel id
        send_message_later(token, invalid_channelid, message, timesent)
        
        # invalid message
        send_message_later(token, channel_id, invalid_message, timesent)
        
        # invalid timesent input
        send_message_later(token, channel_id, message, invalid_timesent)

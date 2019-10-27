# Function: message_sendlater()
# Parameter: (token, channel_id, message, time_sent)
# Output: {}
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# - Message is more than 1000 characters
# - Time sent is a time in the past
# Description: Send a message from authorised_user to the channel specified by channel_id automatically at a specified time in the future
#

import pytest
from f_message_sendlater import message_sendlater
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_invite import channel_invite
import time

def test_message_sendlater():

    # SETUP BEGIN
    
    # Generate a valid user
    registerValidUserDict = auth_register("valid@email.com", "password", "Thom", "Browne")
    token = registerValidUserDict["token"]
    u_id = registerValidUserDict["u_id"]
    createValidChannelDict = channels_create(token, "validchannel", True)
    channel_id = createValidChannelDict["channel_id"]
    channel_invite(token, channel_id, u_id)
    message = "I Heart Thom Browne"
    timesent = present + timedelta(minutes = 1) + tdelta
    
    # Generate an invalid user
    registerInvalidUserDict = auth_register("valid2@email.com", "password", "Thom", "Browne")
    invalid_token = registerInvalidUserDict["token"]
    invalid_uid = registerValidUserDict["u_id"]
    createInvalidChannelDict = channels_create(invalid_token, "invalidchannel", True)
    invalid_channelid = createInvalidChannelDict["channel_id"]
    channel_invite(invalid_token, invalid_channelid, invalid_uid)
    invalid_message = 0
    invalid_timesent = "20/10/1999"
    
    # Invalidate the invalid user
    auth_logout(invalid_token)
    
    # SET UP END
    
    # Asserting that the default case works
    message_id = message_sendlater(token, channel_id, message, timesent)
    time.sleep(60)
    
    data = getData()
    for channels in data['channels']:
        for messages in channels['messages']:
            if messages['message'] == message:
                assert messages['message_id'] == message_id['message_id']
            
    '''
    # Testing that ValueError is raised when invalid parameters are passed
    with pytest.raises(ValueError, match = r"*"):
        
        # Testing function with an invalid token
        message_sendlater(invalid_token, channel_id, message, timesent)
        
        # Testing function with an invalid channel id
        message_sendlater(token, invalid_channelid, message, timesent)
        
        # Testing function with an invalid message
        message_sendlater(token, channel_id, invalid_message, timesent)
        
        # Testing function with an invalid timesent input
        message_sendlater(token, channel_id, message, invalid_timesent)
    '''
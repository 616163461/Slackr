# Function: message_send()
# Parameters: (token, channel_id, message)
# Output: {}
# Exception: ValueError when:
# - Message is more than 1000 characters
# Description: Send a message from authorised_user to the channel specified by channel_id
#

import pytest
from f_message_send import message_send
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_invite import channel_invite
from f_auth_logout import auth_logout
import hashlib

def getData():
    with open('export.json', 'r') as FILE:
        data = json.load(FILE)
    return data

def test_message_send():

    # SETUP BEGIN

    # Generate a valid user 
    registerValidUserDict = auth_register("valid6@email.com", "valid6password", "first6name", "last6name")
    token = registerValidUserDict['token']
    u_id = registerValidUserDict['u_id']
    createValidChannelDict = channels_create(token, "validchannel", True)
    channel_id = createValidChannelDict['channel_id']
    channel_invite(token, channel_id, u_id)
    message = "I Heart Hayden Smith"

    # Generate an invalid user
    registerInvalidUserDict = auth_register("invalid6@email.com", "invalid6password", "invalid6firstname", "invalid6lastname")
    invalid_token = registerInvalidUserDict['token']
    invalid_uid = registerValidUserDict['u_id']
    createInvalidChannelDict = channels_create(invalid_token, "invalidchannel", True)
    invalid_channelid = createInvalidChannelDict['channel_id']
    channel_invite(invalid_token, invalid_channelid, invalid_uid)
    invalid_message = 0
    
    # Invalidate the invalid user
    auth_logout(invalid_token)
    
    # SETUP END
    
    # Asserting that the default case works
    message_id = message_send(token, channel_id, message)
    
    data = getData()
    for channels in data['channels']:
        for messages in channel['messages']:
            if messages['message'] == message:
                assert messages['message_id'] == message_id['message_id']
    
    # Testing that ValueError is raised when invalid parameters are passed
    with pytest.raises(ValueError, match = r"*"): 

        # Testing function with an invalid token
        message_send(invalid_token, channel_id, message)
        
        # Testing function with an invalid channel id
        message_send(token, invalid_channelid, message)
        
        # Testing function with an invalid message
        message_send(token, channel_id, invalid_message)
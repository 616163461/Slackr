# Function: standup_start()
# Parameters: (token, channel_id)
# Output: { time_finish }
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# AccessError when:
# - The authorised user is not a member of the channel
# that the message is within
# Description: For a given channel, start the standup period 
# whereby for the next 15 minutes if someone calls "standup_send" with a message, 
# it is buffered during the 15 minute window then at the end of the 15 minute window 
# a message will be added to the message queue in the channel from the user who started the standup.
#

import pytest
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_standup_start import standup_start
from f_message_send import message_send

def test_standup_start():
	# Valid channel ID
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    createValidChannelDict = channels_create(token, "validchannel", True)
    channel_id = createValidChannelDict["channel_id"]
    time_finish = 19:15/02/10/2019
    
    
    # Invalid channel ID
    registerInvalidUserDict = auth_register("gmail@gmail.com", "password", "Thom", "Browne")
    invalid_token = registerInvalidUserDict["token"]
    invalid_uid = registerValidUserDict["u_id"]
    createInvalidChannelDict = channels_create(invalid_token, "invalidchannel", True)
    invalid_channelid = createInvalidChannelDict["channel_id"]
    
    assert standup_start(token, channel_id) == {time_finish}
    
    with pytest.raises(ValueError): 
        # Testing function with invalid channel_id
    	standup_start(token, invalid_channelid)
		# Testing function with invalid token
		standup_start(invalid_token, channelid)

# Function name: channel_messages()
# Parameters: (token, channel_id, start)
# Return type: { messages, start, end }
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# - start is greater than the total number of messages in the channel
# AccessError when:
# Authorised user is not a member of channel with channel_id
# Description: Given a Channel with ID channel_id that the authorised user is part of, 
# return up to 50 messages between index "start" and "start + 50". 
# Message with index 0 is the most recent message in the channel. 
# This function returns a new index "end" which is the value of "start + 50", or, if this function has 
# returned the least recent messages in the channel, returns -1 in "end" to indicate there are no more messages 
# to load after this return.
#

import pytest
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channel_leave import channel_leave
from f_auth_logout import auth_logout
from f_message_send import message_send


def test_channel_messages(): 
    # SETUP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic1 = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    
    message_send(token, channel_id, "validmessage")
    # SETUP END
    
    # Couldn't assert since unable to obtain message_id also need to assert end == - 1
    channel_messages(token, channel_id, 0)
    
    # Adding 50 more messages to the channel to make 51 total messages
    for i in range(0,50): 
        message_send(token, channel_id, "validmessage")
    
    # Should be asserting that end is not equal to -1      
    channel_messages(token, channel_id, 0)
    
    # Checking that the start index works 
    channel_messages(token, channel_id, 31)
    
    
    
def test_channel_messages_bad(): 

    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    
    message_send(token, channel_id, "validmessage")
    # SETUP END
    
    with pytest.raises(ValueError): 
        # Testing function with invalid channel_id
        channel_messages(token, "invalidchannel_id", 0)
        # Testing function with non-member of the channel
        channel_messages(token_one, channel_id, 0)
       
    message_send(token, channel_id, "secondvalidmessage")
    with pytest.raises(ValueError): 
        # Testing function with starting index greater than total number of messages in the channel
        channel_messages(token, channel_id, 10)


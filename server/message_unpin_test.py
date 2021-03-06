# Function: message_unpin()
# Parameters: (token, message_id)
# Output: {}
# Exception: ValueError when:
# - message_id is not a valid message
# - The authorised user is not an admin
# - Message with ID message_id is already unpinned
# AccessError when:
# - The authorised user is not a member of the channel that the message is within
# Description: Given a message within a channel, remove it's mark as unpinned
#

import pytest
from f_message_send import message_send
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_messages import channel_messages
from f_message_pin import message_pin
from f_message_unpin import message_unpin
from f_channel_join import channel_join
from myexcept import ValueError, AccessError
from json_clean import jsonClean

def test_message_pin(): 
    jsonClean()
    # SETUP BEGIN 
    authRegisterDic = auth_register("valid60@email.com", "valid60password", "first60name", "last60name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("valid61@email.com", "valid61password", "first61name", "last61name")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    
    message_send(token, channel_id, "validmessage")
    channelMessagesDic = channel_messages(token, channel_id, 0)
    message_list = channelMessagesDic["messages"]
    message_dic = message_list[0]
    message_id = message_dic["message_id"]
    # SETUP END
    
    message_pin(token, message_id)
    
    with pytest.raises(ValueError):
        message_pin(token, message_id)
    
    assert message_unpin(token, message_id) == {}
    # Testing message_pin to check the message was successfully unpinned 
    message_pin(token, message_id)
    
        
def test_message_pin_bad(): 
    jsonClean()
    # SETUP BEGIN 
    authRegisterDic = auth_register("valid70@email.com", "valid70password", "first70name", "last70name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("valid71@email.com", "valid71password", "first71name", "last71name")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    channel_join(token_one, channel_id)
    
    authRegisterDicTwo = auth_register("valid72@email.com", "valid72password", "first72name", "last72name")
    token_two = authRegisterDicTwo['token']
    u_id_two = authRegisterDicTwo['u_id']
    
    message_send(token, channel_id, "validmessage")
    channelMessagesDic = channel_messages(token, channel_id, 0)
    message_list = channelMessagesDic["messages"]
    message_dic = message_list[0]
    message_id = message_dic["message_id"]
    # SETUP END
    
    with pytest.raises(ValueError): 
        # Testing function with user who isn't admin 
        message_unpin(token_one, message_id)
        # Testing function with invalid message_id
        message_unpin(token, "invalidmessage_id")
        # Testing function with user who isn't part of the channel
        message_unpin(token_two, message_id)
        
        
    message_unpin(token, message_id)
    with pytest.raises(ValueError):        
        # Testing function with already unpinned message_id
        message_unpin(token, message_id)
    
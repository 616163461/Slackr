# Function: message_pin()
# Parameters: (token, message_id)
# Output: {}
# Exception: ValueError when:
# - message_id is not a valid message
# - The authorised user is not an admin
# - Message with ID message_id is already pinned
# AccessError when:
# - The authorised user is not a member of the channel that the message is within
# Description: Given a message within a channel, mark it as "pinned" to be given special display treatment by the frontend
# 

import pytest
from f_message_send import message_send
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_messages import channel_messages
from f_message_pin import message_pin
from myexcept import ValueError


def test_message_pin(): 
    
    # SETUP BEGIN
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("valid1@email.com", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    
    message_send(token, channel_id, "validmessage")
    channelMessagesDic = channel_messages(token, channel_id, 0)
    message_list = channelMessagesDic["messages"]
    message_dic = message_list[0]
    message_id = message_dic["message_id"]
    # SETUP END
    
    assert message_pin(token, message_id) == {}
    
    
        
def test_message_pin_bad():
    
    # SETUP BEGIN
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("valid1@email.com", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    channel_join(token_one, channel_id)
    
    authRegisterDicTwo = auth_register("valid2@email.com", "validpassword2", "firstname2", "lastname2")
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
        message_pin(token_one, message_id)
        # Testing function with invalid message_id
        message_pin(token, "invalidmessage_id")
        # Testing function with user who isn't part of the channel
        message_pin(token_two, message_id)
        
        
    message_pin(token, message_id)
    with pytest.raises(ValueError):        
        # Testing function with already pinned message_id
        message_pin(token, message_id)
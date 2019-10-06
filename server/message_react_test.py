# Function: message_react()
# Parameters: (token, message_id, react_id)
# Output: {}
# Exception: ValueError when:
# - message_id is not a valid message within a channel that the authorised user has joined
# - react_id is not a valid React ID
# - Message with ID message_id already contains an active React with ID react_id
# Description: Given a message within a channel the authorised user is part of, add a "react" to that particular message
#

import pytest
from f_message_send import message_send
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_messages import channel_messages
from f_message_unreact import message_unreact
from f_message_react import message_react

def test_message_react(): 
    
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
    
    # Assuming 123 is valid react_id
    react_id = 123
    
    # SETUP END
    
    assert message_react(token, message_id, react_id) == {}
   
        
def test_message_react_bad(): 
    
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
        message_react(token_one, message_id, react_id)
        # Testing function with invalid message_id
        message_react(token, "invalidmessage_id", react_id)
        # Testing function with user who isn't part of the channel
        message_react(token_two, message_id, react_id)
        # Testing function with invalid react_id
        message_react(token, message_id, "invalidreact_id")
        
    message_react(token, message_id, react_id)
    with pytest.raises(ValueError):        
        # Testing function with already reacted message_id
        message_react(token, message_id, react_id)
        
    message_unreact(token, message_id, react_id)
    auth_logout(token)
    with pytest.raises(ValueError): 
        # Testing function with invalid token 
        message_react(token, message_id, react_id)

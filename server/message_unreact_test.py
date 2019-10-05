import pytest
from f_message_send import message_send
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_messages import channel_messages
from f_message_unreact import message_unreact
from f_message_react import message_react

def test_message_unreact(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic1 = auth_register("valid@email1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    
    message_send(token, channel_id, "validmessage")
    channelMessagesDic = channel_messages(token, channel_id, 0)
    message_list = channelMessagesDic["messages"]
    message_dic = message_list[0]
    message_id = message_dic["message_id"]
    
    # assuming 123 is valid react_id
    react_id = 123
    # SET UP END
    
    message_react(token, message_id, react_id)
    
    with pytest.raises(ValueError):
        message_react(token, message_id, react_id)
        
    assert message_unreact(token, message_id, react_id) == {}
    # calling message_react to check the message was successfully unreacted 
    message_react(token, message_id, react_id)
    
        
def test_message_unreact_bad(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic1 = auth_register("valid@email1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    channel_join(token1, channel_id)
    
    authRegisterDic2 = auth_register("valid@email2", "validpassword2", "firstname2", "lastname2")
    token2 = authRegisterDic2['token']
    u_id2 = authRegisterDic2['u_id']
    
    message_send(token, channel_id, "validmessage")
    channelMessagesDic = channel_messages(token, channel_id, 0)
    message_list = channelMessagesDic["messages"]
    message_dic = message_list[0]
    message_id = message_dic["message_id"]
    # SET UP END

    message_react(token, message_id, react_id)
    with pytest.raises(ValueError): 
        # calling function with user who isn't admin 
        message_unreact(token1, message_id, react_id)
        # calling function with invalid message_id
        message_unreact(token, "invalidmessage_id", react_id)
        # calling function with user who isn't part of the channel
        message_unreact(token2, message_id, react_id)
        # calling function with invalid react_id
        message_unreact(token, message_id, "invalidreact_id")
        
    message_unreact(token, message_id, react_id)
    with pytest.raises(ValueError):        
        # calling function with already unreacted message_id
        message_unreact(token, message_id, react_id)
        
    message_react(token, message_id, react_id)
    auth_logout(token)
    with pytest.raises(ValueError): 
        # calling function with invalid token 
        message_unreact(token, message_id, react_id)

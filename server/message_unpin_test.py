import pytest
from f_message_send import message_send
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_messages import channel_messages
from f_message_pin import message_pin
from f_message_unpin import message_unpin


def test_message_pin(): 
    
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
    # SET UP END
    
    message_pin(token, message_id)
    
    with pytest.raises(ValueError):
        message_pin(token, message_id)
        
    assert message_unpin(token, message_id) == {}
    # calling message_pin to check the message was successfully unpinned 
    message_pin(token, message_id)
    
        
def test_message_pin_bad(): 
    
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
    
    with pytest.raises(ValueError): 
        # calling function with user who isn't admin 
        message_unpin(token1, message_id)
        # calling function with invalid message_id
        message_unpin(token, "invalidmessage_id")
        # calling function with user who isn't part of the channel
        message_unpin(token2, message_id)
        
        
    message_unpin(token, message_id)
    with pytest.raises(ValueError):        
        # calling function with already unpinned message_id
        message_unpin(token, message_id)
        

from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channel_leave import channel_leave
from f_auth_logout import auth_logout
from f_message_send import message_send
import pytest

def test_channel_messages(): 
    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic1 = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    
    message_send(token, channel_id, "validmessage")
    # SET UP END
    
    # couldn't assert since unable to obtain message_id also need to assert end == - 1
    channel_messages(token, channel_id, 0)
    
    # adding 50 more messages to the channel to make 51 total messages
    for i in range(0,50): 
        message_send(token, channel_id, "validmessage")
    
    # should be asserting that end is not equal to -1      
    channel_messages(token, channel_id, 0)
    
    # checking that the start index works 
    channel_messages(token, channel_id, 31)
    
    
    
def test_channel_messages_bad(): 

    # SET UP BEGIN 
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDic1 = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    
    message_send(token, channel_id, "validmessage")
    # SET UP END
    
    with pytest.raises(ValueError): 
        # calling function with invalid channel_id
        channel_messages(token, "invalidchannel_id", 0)
        # calling function with non-member of the channel
        channel_messages(token1, channel_id, 0)
       
    message_send(token, channel_id, "secondvalidmessage")
    with pytest.raises(ValueError): 
        # calling function with starting index greater than total number of messages in the channel
        channel_messages(token, channel_id, 10)

from f_auth_register import auth_register
from f_channels_create import channels_create
from f_standup_start import standup_start
from f_message_send import message_send
from f_channel_invite import channel_invite
import pytest


def test_standup_send():

    # Generate a valid user 
    registerValidUserDict = auth_register("hwangyeji@gmail.com", "feelspecial", "Hwang", "Yeji")
    token = registerValidUserDict["token"]
    u_id = registerValidUserDict["u_id"]
    createValidChannelDict = channels_create(token, "validchannel", True)
    channel_id = createValidChannelDict["channel_id"]
    message = "I Heart Hwang Yeji"
    message_list = channelValidMessagesDict["messages"]
    message_dict = message_list[0]
    message_id = message_dict["message_id"]

    time = 19:16/02/10

    # Generate an invalid user
    registerInvalidUserDict = auth_register("kangdaniel@gmail.com", "password", "Kang", "Daniel")
    invalid_token = registerInvalidUserDict["token"]
    invalid_uid = registerValidUserDict["u_id"]
    createInvalidChannelDict = channels_create(invalid_token, "invalidchannel", True)
    invalid_channelid = createInvalidChannelDict["channel_id"]
    channel_invite(invalid_token, invalid_channelid, invalid_uid)
    invalid_message = 0
    

    # Asserting that the default case works
    assert standup_send(token, channel_id, message) == {}
    
    # Testing that ValueError is raised when invalid parameters are passed
    with pytest.raises(ValueError): 

        # calling function with an invalid token
        standup_send(invalid_token, channel_id, message)
        
        # calling function with an invalid channel id
        standup_send(token, invalid_channelid, message)
        
        # calling function with an invalid message
        standup_send(token, channel_id, invalid_message)


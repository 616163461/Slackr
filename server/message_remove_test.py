from f_message_send import message_send
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_message_remove import message_remove
from f_channel_messages import channel_messages
from f_channel_invite import channel_invite
import pytest

def test_message_remove():
    
    # SET UP BEGIN
    
    # Generate a valid user
    registerValidUserDict = auth_register("hwangyeji@gmail.com", "feelspecial", "Thom", "Browne")
    token = registerValidUserDict["token"]    
    u_id = registerValidUserDict["u_id"]
    createValidChannelDict = channels_create(token, "validchannel", True)
    channel_id = createValidChannelDict["channel_id"]
    channel_invite(token, channel_id, u_id)
    message_send(token, channel_id, "Hi")
    message_send(token, channel_id, "My name is")
    message_send(token, channel_id, "Thom Browne")
    channelValidMessagesDict = channel_messages(token, channel_id, 0)
    message_list = channelValidMessagesDict["messages"]
    message_dict = message_list[0]
    message_id = message_dict["message_id"]
    
    # Generate an invalid user
    registerInvalidUserDict = auth_register("chungha@gmail.com", "snapping", "Kang", "Daniel")
    invalid_token = registerInvalidUserDict["token"]  
    invalid_uid = registerValidUserDict["u_id"]  
    createInvalidChannelDict = channels_create(invalid_token, "invalidchannel", True)
    invalid_channelid = createInvalidChannelDict["channel_id"]
    channel_invite(invalid_token, invalid_channelid, invalid_uid)
    message_send(invalid_token, channel_id, "iH")
    message_send(invalid_token, channel_id, "si eman yM")
    message_send(invalid_token, channel_id, "enworB mohT")
    channelInvalidMessagesDict = channel_messages(invalid_token, invalid_channelid, 1)
    invalid_messagelist = channelValidMessagesDict["messages"]
    invalid_messagedict = invalid_messagelist[1]
    invalid_messageid = invalid_messagedict["message_id"]
    
    # Invalidate the invalid user
    auth_logout(invalid_token)
    
    # SET UP END
    
    # Asserting that the default case works
    assert remove_message(token, message_id) == {}
    
    # Testing that ValueError is raised when invalid parameters are passed
    with pytest.raises(ValueError, match = r"*"):
        
        # calling function with an invalid token
        remove_message(invalid_token, message_id)

        # calling function with an invalid message id
        remove_message(valid_token, invalid_messageid)

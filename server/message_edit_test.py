# Function: message_edit()
# Parameters: (token, message_id, message)
# Output: {}
# Exception: ValueError when: 
# - all of the following are not true:
# - Message with message_id was not sent by the authorised user making this request
# - Message with message_id was not sent by an owner of this channel
# - Message with message_id was not sent by an admin or owner of the slack
# Description: Given a message, update it's text with new text
#

import pytest
from f_message_send import message_send
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_messages import channel_messages
from f_channel_invite import channel_invite
from f_channel_edit import channel_edit


def test_message_edit():
    
    # SETUP BEGIN
    
    # Token creates the channel so it should be the owner
	registerValidUserDict = auth_register("hwangyeji@gmail.com", "feelspecial", "Thom", "Browne")
    token = registerValidUserDict["token"]    
    u_id = registerValidUserDict["u_id"]
    createValidChannelDict = channels_create(token, "validchannel", True)
    channel_id = createValidChannelDict["channel_id"]
    message_send(token, channel_id, "Hi")
    message_send(token, channel_id, "My name is")
    message_send(token, channel_id, "Thom Browne")
    channelValidMessagesDict = channel_messages(token, channel_id, 0)
    message_list = channelValidMessagesDict["messages"]
    message_dict = message_list[0]
    message_id = message_dict["message_id"]

    # A member in the channel
    authRegisterDicOne = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    channel_invite(token, channel_id, u_id_one)
    message_send(token_one, channel_id, "iH")
    message_send(token_one, channel_id, "si eman yM")
    message_send(token_one, channel_id, "enworB mohT")
    channelInvalidMessagesDict = channel_messages(token_one, channel_id, 1)
    invalid_messagelist = channelValidMessagesDict["messages"]
    invalid_messagedict = invalid_messagelist[1]
    invalid_messageid = invalid_messagedict["message_id"]
    # SETUP END

    # Asserting that the default case works
    assert edit_message(token, message_id, message_list[0]) == {}
    
    # Testing that ValueError is raised when invalid parameters are passed
    with pytest.raises(ValueError):
        
        # Testing function with an invalid token
        edit_message(token_one, message_id, message_list[0])

        # Testing function with an invalid message id
        edit_message(token_one, invalid_messageid, message_list[1])





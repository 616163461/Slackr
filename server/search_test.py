# Function: search()
# Parameter: (token, query_str)
# Output: { messages }
# Exception: N/A
# Description: Given a query string, return a collection of messages that match the query
#

import pytest
from f_search import search
from f_message_send import message_send
from f_channels_create import channels_create
from f_auth_register import auth_register
from f_auth_logout import auth_logout
from f_channel_invite import channel_invite
from f_channel_messages import channel_messages

def test_search(): 
    
    # SETUP BEGIN
    # User One 
    validAuthRegisterDic = auth_register("valid@email.com", "validpassword", "Richard", "Jiang")
    token = validAuthRegisterDic['token']
    u_id = validAuthRegisterDic['u_id']
    
    # User Two
    validAuthRegisterDicOne = auth_register("valid2@email.com", "validpassword", "Daniel", "Yang")
    token_one = validAuthRegisterDicOne['token']
    u_id_one = validAuthRegisterDicOne['u_id']
    
    # False User Three
    invalidAuthRegisterDic = auth_register("valid3@email.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDic['token']
    # Creates an Invalid Token
    auth_logout(invalid_token) 
    
    # Create a channel
    channel_id = channels_create(token, "Channel Nine", True)
    
    # Invite the member
    channel_invite(token, channel_id, u_id_one)
    
    # Send the messages
    message_send(token_one, channel_id, "Safe and secure society")
    message_send(token, channel_id, "Hello")
    message_send(token_one, channel_id, "Hellomydude")
    message_send(token, channel_id, "Hellomyman")
    message_send(token, channel_id, "Seriously cool")
    message_send(token_one, channel_id, "Absolutely astonishing")
    message_send(token, channel_id, "Congratulations on the role!")
    message_send(token_one, channel_id, "Happy work anniversary!")
    message_send(token, channel_id, "New world. New skills.")
    message_send(token, channel_id, "New world")
    
    # Find the Message ID's
    channelMessagesDic = channel_messages(token, channel_id, 0)
    message_list = channelMessagesDic["messages"]
    message_dic = message_list[0]
    message_id_safe = message_dic["message_id"]
    message_dic_one = message_list[2]
    message_id_one = message_dic_one["message_id"]
    message_dic_two = message_list[3]
    message_id_two = message_dic_two["message_id"]
    # SETUP END
    
    # Testing for no results
    assert search(token, "???") == {}
    
    # Testing for one result
    assert search(token, "Safe") == {"message_id" : message_id_safe, "u_id": u_id_one, "message" : "Safe and secure society", "time_created" : "19:35", "is_unread" : True}
    
    # Testing for two or more results
    assert search(token, "Hellomy") == [{  
        "message_id" : 112,
        "u_id" : message_id_one, 
        "message" : "Hellomydude",
        "time_created" : "17:35",
        "is_unread" : True
    },
    {
        "message_id" : 113,
        "u_id" : message_id_two, 
        "message" : "Helloymyman",
        "time_created" : "18:35",
        "is_unread" : True
    }]
    
    # Testing Bad Cases
    with pytest.raises(ValueError):
        # Bad token with multiple search results
        search(invalid_token, "Hellomy")
        # Bad token with no search results
        search(invalid_token, "ahahahahahaha")

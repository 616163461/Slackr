#Functions: search()
#Parameters: (token, query_str)
#Output: {messages}
#ValueError: N/A
#Description: Given a query string, return a collection of messages that match the query

import pytest
from f_search import search
from f_message_send import message_send
from f_channels_create import channels_create
from f_auth_register import auth_register
from f_auth_logout import auth_logout
from f_channel_invite import channel_invite

def test_search():
    
    #SET UP BEGIN
    #User One 
    validAuthRegisterDicOne = auth_register("richard123@gmail.com", "validpassword", "Richard", "Jiang")
    token_user_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    #User Two
    validAuthRegisterDicTwo = auth_register("daniel123@gmail.com", "validpassword", "Daniel", "Yang")
    token_user_two = authRegisterDicTwo['token']
    u_id_two = authRegisterDicTwo['u_id']
    
    #False User Three
    invalidAuthRegisterDic = auth_register("richard123@gmail.com", "validpassword", "firstname", "lastname")
    invalid_token = invalidAuthRegisterDic['token']
    auth_logout(invalid_token) #Creates an Invalid Token
    
    channel_id = channels_create(token, "Channel Nine", True)
    channel_invite(token_user_one, channel_id, u_id_one)
    channel_invite(token_user_two, channel_id, u_id_two)
    message_send(token_user_one, channel_id, "Hello")
    message_send(token_user_two, channel_id, "Hellomydude")
    message_send(token_user_one, channel_id, "Hellomyman")
    message_send(token_user_one, channel_id, "Seriously cool")
    message_send(token_user_two, channel_id, "Absolutely astonishing")
    message_send(token_user_one, channel_id, "Congratulations on the role!")
    message_send(token_user_two, channel_id, "Happy work anniversary!")
    message_send(token_user_one, channel_id, "New world. New skills.")
    message_send(token_user_two, channel_id, "Safe and secure society")
    message_send(token_user_one, channel_id, "New world")
    #SET UP END
    
    #Testing for no results
    assert search(token_user_one, "???") == {}
    
    #Testing for one result
    assert search(token_user_one, "Safe") == {"message_id" : 111 , "u_id": u_id_two, "message" : "Safe and secure society", "time_created" : "19:35", "is_unread" : True}
    
    #Testing for two or more results
    assert search(token_user_one, "Hellomy") == [{  "message_id" : 112, 
        "u_id": u_id_two, 
        "message" : "Hellomydude",
        "time_created" : "17:35",
        "is_unread" : True
    } ,
    {
       "message_id" : 113, 
        "u_id": u_id_one, 
        "message" : "Helloymyman",
        "time_created" : "18:35",
        "is_unread" : True
    }]
    
    #Testing Bad Cases
    with pytest.raises(ValueError):
        #Bad token with multiple search results
        search(invalid_token, "hey")

import pytest
from f_search import search

def test_search():
    token = "12345678"
    badtoken = "2345671" #bad token
    
    #Singular search
    assert search(token, "b") == {"message_id" : "11112", "u_id": "dyang", "message" : "b", "time_created" : "17:35", "is_unread" : "r"}
    #No matches
    assert search(token, "aaaaaaaaaaa") == {}
    #Multiple searches
    assert search(token, "hey") == [{  "message_id" : "11111", 
        "u_id": "rjiang", 
        "message" : "hey man",
        "time_created" : "17:35",
        "is_unread" : "r"
    } ,
    {
       "message_id" : "11113", 
        "u_id": "ghe", 
        "message" : "hey dude",
        "time_created" : "18:35",
        "is_unread" : "ur"
    }]

    
def test_search_bad():
    with pytest.raises(ValueError):
        badtoken = "2345671" #bad token
        #Bad token with multiple search results
        search(badtoken, "hey")
    

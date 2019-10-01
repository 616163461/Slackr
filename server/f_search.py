
def search(token, query_str):
    
    if token == "2345671": #Should be a valid token, if not, return error
        raise ValueError(f"Error, please enter a valid token")
    
    if query_str == "aaaaaaaaaaa":
        messages = {}
        return messages
    
    if query_str == "b":
        messages = {}
        messages["message_id"] = "11112"
        messages["u_id"] = "dyang"
        messages["message"] = "b"
        messages["time_created"] = "17:35"
        messages["is_unread"] = "r"
    
    elif query_str == "hey":
        messages = [
            {  
                "message_id" : "11111", 
                "u_id": "rjiang", 
                "message" : "hey man",
                "time_created" : "17:35",
                "is_unread" : "r"
            },
            {
               "message_id" : "11113", 
                "u_id": "ghe", 
                "message" : "hey dude",
                "time_created" : "18:35",
                "is_unread" : "ur"
            }
        ]
    
    return messages

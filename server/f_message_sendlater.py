from datetime import datetime

def send_message_later(token, channel_id, message, time_sent):
    # message > 1000 characters
    if len(message) > 1000:
        raise ValueError(f"Error, message is longer than 1000 characters")
    # channel ID not valid
    if isinstance(channel_id, int) == False:
        raise ValueError(f"Error, channel does not exist")
        
    curr_time = datetime.now()  
    input_date = datetime.strptime(time_sent, "%d/%m/%Y")  
    if input_date.date() < curr_time.date():
        raise ValueError(f"Error, time entered is in the past")
        
    return_dict = {}
    
    return return_dict

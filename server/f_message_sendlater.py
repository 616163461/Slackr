# Function name: message_sendlater()
# Parameters: (token, channel_id, message, time_sent)
# Return type: {}
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# - Message is more than 1000 characters
# - Time sent is a time in the past
# Description: Send a message from authorised_user to the channel specified by channel_id automatically at a specified time in the future
#

def message_sendlater(token, channel_id, message, time_sent):
    
    message_sendlater_dict = {}
    
    return message_sendlater_dict
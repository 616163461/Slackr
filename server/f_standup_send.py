# Function name: standup_send()
# Parameters: (token, channel_id, message)
# Return type: {}
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# - Message is more than 1000 characters
# AccessError when:
# - The authorised user is not a member of the channel that the message is within
# - If the standup time has stopped
# Description: Sending a message to get buffered in the standup queue, assuming a standup is currently active
#

def standup_send(token, channel_id, message):
    
    standup_send_dict = {}
    
    return standup_send_dict
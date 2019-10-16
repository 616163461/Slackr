# Function name: channel_join()
# Parameters: (token, channel_id)
# Return type: {}
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# AccessError when:
# - channel_id refers to a channel that is private (when the authorised user is not an admin)
# Description: Given a channel_id of a channel that the authorised user can join, adds them to that channel
#

def channel_join(token, channel_id): 
    
    channel_join_dict = {}

    return channel_join_dict
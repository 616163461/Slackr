# Function name: channel_removeowner()
# Parameters: (token, channel_id, u_id)
# Return type: {}
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# - When user with user id u_id is not an owner of the channel
# AccessError when:
# - the authorised user is not an owner of the slackr, or an owner of this channel
# Description: Remove user with user id u_id an owner of this channel
#

def channel_removeowner(token, channel_id, u_id):
    
    channel_removeowner_dict = {}
    
    return channel_removeowner_dict
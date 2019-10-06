# Function name: standup_send()
# Parameters: (token, channel_id)
# Return type: { time_finish }
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# AccessError when:
# - The authorised user is not a member of the channel that the message is within
# Description: Given a message within a channel the authorised user is part of, add a "react" to that particular message
#

def standup_start(token, channel_id, message):
    pass
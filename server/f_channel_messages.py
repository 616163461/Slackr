# Function name: channel_messages()
# Parameters: (token, channel_id, start)
# Return type: { messages, start, end }
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# - start is greater than the total number of messages in the channel
# AccessError when:
# - Authorised user is not a member of channel with channel_id
# Description: Given a Channel with ID channel_id that the authorised user is part of, 
# return up to 50 messages between index "start" and "start + 50". 
# Message with index 0 is the most recent message in the channel. 
# This function returns a new index "end" which is the value of "start + 50", 
# or, if this function has returned the least recent messages in the channel, 
# returns -1 in "end" to indicate there are no more messages to load after this return.
#

def channel_messages(token, channel_id, start):
    pass
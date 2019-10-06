# Function name: message_remove()
# Parameters: (token, message_id)
# Return type: {}
# Exception: ValueError when:
# - Message (based on ID) no longer exists
# AccessError when:
# - Message with message_id was not sent by the authorised user making this request
# - Message with message_id was not sent by an owner of this channel
# - Message with message_id was not sent by an admin or owner of the slack
# Description: Given a message_id for a message, this message is removed from the channel
#

def message_remove(token, message_id):
    pass
# Function name: channel_invite()
# Parameters: (token, channel_id, u_id)
# Return type: {}
# Exception: ValueError when:
# - channel_id does not refer to a valid channel that the authorised user is part of.
# - u_id does not refer to a valid user
# Description: Invites a user (with user id u_id) to join a channel with ID channel_id. Once invited the user is added to the channel immediately
#

def channel_invite(token, channel_id, u_id):

    channel_invite_dict = {}

    return channel_invite_dict
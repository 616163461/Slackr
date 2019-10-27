# Function name: channel_invite()
# Parameters: (token, channel_id, u_id)
# Return type: { name, owner_members, all_members }
# Exception: ValueError when:
# - channel_id does not refer to a valid channel that the authorised user is part of.
# - u_id does not refer to a valid user
# Description: Invites a user (with user id u_id) to join a channel with ID channel_id. Once invited the user is added to the channel immediately
#

import pytest
from f_channel_invite import channel_invite
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_auth_logout import auth_logout
from f_channel_details import channel_details
from f_channel_invite import channel_invite
from f_channel_leave import channel_leave

def test_channel_invite(): 
    
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid6@email.com", "validpassword", "first6name", "last6name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("valid8@email.com", "validpassword1", "first8name1", "last8name1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    # SETUP END 
    
    channel_invite(token, channel_id, u_id_one)
    # Asserting that the invited user is now a member of the channel
    assert channel_details(token_one, channel_id) == {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "first6name", "name_last": "last6name"}], "all_members": [{"u_id": u_id, "name_first": "first6name", "name_last": "last6name"}, {"u_id": u_id_one, "name_first": "first8name1", "name_last": "last8name1"}]}
    # Testing channel_leave to check that he's a member of the channel
    channel_leave(token_one, channel_id)
    

def test_channel_invite_bad(): 
    # SET UP BEGIN 
    authRegisterDic = auth_register("valid@email.com", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']

    authRegisterDicOne = auth_register("valid2@email.com", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    channelsCreateDicOne = channels_create(token_one, "validchannel1", True)
    channel_id_one = channelsCreateDicOne['channel_id']
    
    authRegisterDicTwo = auth_register("valid3@email.com", "validpassword2", "firstname2", "lastname2")
    token_two = authRegisterDicTwo['token']
    u_id_two = authRegisterDicTwo['u_id']
    # SETUP END
    '''
    with pytest.raises(ValueError): 
        # Testing function with invalid channel_id
        channel_invite(token, "invalidchannel_id", u_id_one)
        # Testing function with channel_id which the authorised user isn't a member of
        channel_invite(token, channel_id_one, u_id_two)
        # Testing function with an invalid u_id
        channel_invite(token, channel_id, "invalidu_id")
        
    auth_logout(token_one)

    with pytest.raises(ValueError): 
        # Testing function with invalid token
        channel_invite(token_one, channel_id_one, u_id_two)
    '''

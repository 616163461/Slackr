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

import pytest
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channet_leave import channel_leave
from f_channels_list import channels_list
from f_auth_logout import auth_logout
from f_channel_removeowner import channel_removeowner
from f_channel_addowner import channel_addowner


def test_channel_removeowner():
    
    # SET UP BEGIN
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    
    authRegisterDicTwo = auth_register("validemail2", "validpassword2", "firstname2", "lastname2")
    token_two = authRegisterDicTwo['token']
    u_id_two = authRegisterDicTwo['u_id']
    # SETUP END
    
    # Adding user_one as an owner
    channel_addowner(token, channel_id, u_id_one)
    # Removing user_one as an owner
    channel_removeowner(token, channel_id, u_id_one)
    # Calling function with recently removed owner to check he's not an owner
    channel_addowner(token_one, channel_id, u_id_two)
    

def test_channel_removeowner_bad():
    # SET UP BEGIN
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
    authRegisterDicOne = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    
    authRegisterDicTwo = auth_register("validemail2", "validpassword2", "firstname2", "lastname2")
    token_two = authRegisterDicTwo['token']
    u_id_two = authRegisterDicTwo['u_id']
    
    authRegisterDicThree = auth_register("validemail3", "validpassword3", "firstname3", "lastname3")
    token_three = authRegisterDicThree['token']
    u_id_three = authRegisterDicThree['u_id']
    # SETUP END
    
    channel_addowner(token, channel_id, u_id_one)
    
    with pytest.raises(ValueError): 
        # Testing function with invalid channel_id
        channel_removeowner(token, "invalidchannel_id", u_id_one)
        # Testing function removing a user who isn't an owner
        channel_removeowner(token, channel_id, u_id_two)
        # Testing function with a user who isn't an owner
        channel_removeowner(token_two, channel_id, u_id_three)
        
    auth_logout(token)
    with pytest.raises(ValueError): 
        # Testing function with invalid token
        channel_removeowner(token, channel_id, u_id_one)


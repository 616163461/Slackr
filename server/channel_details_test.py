<<<<<<< HEAD
# Function name: channel_details()
# Parameters: (token, channel_id)
# Return type: { name, owner_members, all_members }
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# AccessError when:
# - Authorised user is not a member of channel with channel_id
# Description: Given a Channel with ID channel_id that the authorised user is part of, provide basic details about the channel
#

import pytest
=======
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_auth_logout import auth_logout
<<<<<<< HEAD


def test_channel_details(): 
    
    # SETUP BEGIN 
=======
import pytest

def test_channel_details(): 
    
    # SET UP BEGIN 
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
<<<<<<< HEAD
    # SETUP END 
=======
    # SET UP END 
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
    
    assert channel_details(token, channel_id) == {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}], "all_members": [{}]}
    
    
def test_channel_details_bad(): 
    
<<<<<<< HEAD
    # SETUP BEGIN
=======
    # SET UP BEGIN
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
    authRegisterDic = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
<<<<<<< HEAD
    authRegisterDicOne = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    channelsCreateDicOne = channels_create(token_one, "validchannel1", True)
    channel_id_one = channelsCreateDicOne['channel_id']
    # SETUP END 
    
    with pytest.raises(ValueError): 
        # Testing function with invalid channel_id
        channel_details(token, "invalidchannel_id")
        # Testing function with unauthorised user
        channel_details(token, channel_id_one)
=======
    authRegisterDic1 = auth_register("valid@email", "validpassword", "firstname", "lastname")
    token1 = authRegisterDic['token']
    u_id1 = authRegisterDic['u_id']
    channelsCreateDic1 = channels_create(token1, "validchannel1", True)
    channel_id1 = channelsCreateDic['channel_id']
    # SET UP END 
    
    with pytest.raises(ValueError): 
        # calling function with invalid channel_id
        channel_details(token, "invalidchannel_id")
        # calling function with unauthorised user
        channel_details(token, channel_id1)
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128

        
    auth_logout(token)
    with pytest.raises(ValueError): 
<<<<<<< HEAD
        # Testing function with invalid token
        channel_details(token, channel_id)

=======
        # calling function with invalid token
        channel_details(token, channel_id)
        
        
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128

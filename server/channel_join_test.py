<<<<<<< HEAD
# Function name: channel_join()
# Parameters: (token, channel_id)
# Return type: {}
# Exception: ValueError when:
# - Channel (based on ID) does not exist
# AccessError when:
# - channel_id refers to a channel that is private (when the authorised user is not an admin)
# Description: Given a channel_id of a channel that the authorised user can join, adds them to that channel
#

import pytest
=======
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_auth_logout import auth_logout
<<<<<<< HEAD


def test_channel_join(): 
    
    # SETUP BEGIN 
=======
import pytest

def test_channel_join(): 
    
    # SET UP BEGIN 
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
<<<<<<< HEAD
    authRegisterDicOne = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    # SETUP END 
    
    channel_join(token_one, channel_id)
    # Assuming admin isn't in all_members list since admin was specifically isn't a member
    assert channel_details(token, channel_id) == {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}], "all_members": [{"u_id": u_id_one, "name_first": "firstname1", "name_last": "lastname1"}]}
=======
    authRegisterDic1 = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    # SET UP END 
    
    channel_join(token1, channel_id)
    # assuming admin isn't in all_members list since admin was specifically isn't a member
    assert channel_details(token, channel_id) == {"name": "validchannel", "owner_members": [{"u_id": u_id, "name_first": "firstname", "name_last": "lastname"}], "all_members": [{"u_id": u_id1, "name_first": "firstname1", "name_last": "lastname1"}]}
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
    
    
def test_channel_join_bad(): 
    
<<<<<<< HEAD
    # SETUP BEGIN 
=======
    # SET UP BEGIN 
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", False)
    channel_id = channelsCreateDic['channel_id']
    
<<<<<<< HEAD
    authRegisterDicOne = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token_one = authRegisterDicOne['token']
    u_id_one = authRegisterDicOne['u_id']
    # SETUP END 
    
    with pytest.raises(ValueError): 
        # Testing function with invalid channel_id
        channel_join(token, "invalidchannel_id")
        # Testing function with unauthorised token when channel is private
        channel_join(token_one, channel_id)
    
    # Invalidate token
    auth_logout(token)
    
    with pytest.raises(ValueError): 
        # Testing function with invalid token
=======
    authRegisterDic1 = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    # SET UP END 
    
    with pytest.raises(ValueError): 
        # calling function with invalid channel_id
        channel_join(token, "invalidchannel_id")
        # calling function with unauthorised token when channel is private
        channel_join(token1, channel_id)
    
    # invalidate token
    auth_logout(token)
    
    with pytest.raises(ValueError): 
        # calling function with invalid token
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
        channel_join(token, channel_id)
        
        
    
    
    
<<<<<<< HEAD

=======
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128

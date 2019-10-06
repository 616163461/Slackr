<<<<<<< HEAD
# Function name: channels_list()
# Parameters: (token)
# Return type: { channels }
# Exception: N/A
# Description: Provide a list of all channels (and their associated details) that the authorised user is part of
#

import pytest
=======
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
from f_channel_details import channel_details
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_channel_join import channel_join
from f_channet_leave import channel_leave
from f_channels_list import channels_list
from f_auth_logout import auth_logout
<<<<<<< HEAD


def test_channels_list(): 
    
    # SETUP BEGIN 
=======
import pytest

def test_channels_list(): 
    
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
    
    # Testing function using authorised user
    assert channels_list(token) = [{channels: {channel_id: "validchannel"}}]
    
    
def test_channels_list_bad(): 
    
    # SETUP BEGIN 
=======
    authRegisterDic1 = auth_register("validemail1", "validpassword1", "firstname1", "lastname1")
    token1 = authRegisterDic1['token']
    u_id1 = authRegisterDic1['u_id']
    # SET UP END
    
    # calling function using authorised user
    assert channels_list(token) = [{channels: {channel_id: "validchannel"}}]
    

def test_channels_list_bad(): 
    
    # SET UP BEGIN 
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    channelsCreateDic = channels_create(token, "validchannel", True)
    channel_id = channelsCreateDic['channel_id']
    
<<<<<<< HEAD
    # SETUP END 
=======
    # SET UP END 
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128
    
    
    auth_logout(token)
    with pytest.raises(ValueError):
<<<<<<< HEAD
        # Testing function using invalid token 
        channels_list(token)

=======
        # calling function using invalid token 
        channels_list(token)
        
>>>>>>> 35d67967a106c3c7d62aae781161f5fb5e25d128

from f_auth_register import auth_register
from f_channels_create import channels_create
from f_standup_start import standup_start
from f_message_send import message_send
import pytest

def test_standup_start():
	# valid channel id
    authRegisterDic = auth_register("validemail", "validpassword", "firstname", "lastname")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
	createValidChannelDict = channels_create(token, "validchannel", True)
    channel_id = createValidChannelDict["channel_id"]
    time_finish = 19:15/02/10/2019


    # invalid channel id
 	registerInvalidUserDict = auth_register("gmail@gmail.com", "password", "Thom", "Browne")
    invalid_token = registerInvalidUserDict["token"]
    invalid_uid = registerValidUserDict["u_id"]
    createInvalidChannelDict = channels_create(invalid_token, "invalidchannel", True)
    invalid_channelid = createInvalidChannelDict["channel_id"]

    assert standup_start(token, channel_id) == {time_finish}



    with pytest.raises(ValueError): 
        # calling function with invalid channel_id
    	standup_start(token, invalid_channelid)
		# calling function with invalid token
		standup_start(invalid_token, channelid)

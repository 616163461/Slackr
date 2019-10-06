import pytest
from f_message_send import send_message
from f_auth_register import auth_register
from f_channels_create import channels_create
from f_message_remove import remove_message

def test_remove_message():
    
    # SETUP START (valid tests)
    
    registerValidDict = auth_register("thombrowne@gmail.com", "feelspecial", "thom", "browne")
    token = registerValidDict["token"]
    message_id = 12345
    
    # SETUP END (valid test)
    
    assert remove_message(token, message_id) == {}
    
def test_invalid_remove_message():
    
    # SETUP START (valid tests)
    
    registerValidDict = auth_register("thombrowne@gmail.com", "feelspecial", "thom", "browne")
    token = registerValidDict["token"]
    message_id = 12345
    
    # SETUP END (valid test)
    
    with pytest.raises(ValueError, match = r"*"):
    
        # SETUP START (invalid tests)
        
        registerInvalidDict = auth_register("bademail.com", "b", "Thom", "Browne")
        registerInvalidDict2 = auth_register("bademail.com", 1531, "Thom", "Browne")
        
        invalid_token = registerInvalidDict["token"]
        invalid_token2 = registerInvalidDict2["token"]
        
        invalid_message_id = "yes"
        
        # SETUP END (invalid tests)
        
        remove_message(invalid_token, message_id)
        remove_message(invalid_token, invalid_message_id)
        remove_message(invalid_token2, message_id)
        remove_message(invalid_token2, invalid_message_id)
        remove_message(valid_token, invalid_message_id)


from f_channels_create import channels_create
from f_auth_register import auth_register
import pytest

def test_channels_create(): 
    
    dictionary = auth_register("geoffrey.he777@gmail.com", "PigBabo", "Geoffrey", "He")
    u_id = dictionary["u_id"]
    token = dictionary["token"]
    
    #assumed all returned channel_id are 12345
    #case public good/study channel
    assert channels_create(token, "study channel", True) == {"channel_id" : 1111}
    #case private good/study channel
    assert channels_create(token, "study channel", False) == {"channel_id" : 1111}
    #case public bad/gaming channel
    assert channels_create(token, "gaming channel", True) == {"channel_id" : 0000}
    #case private bad/gaming channel
    assert channels_create(token, "gaming channel", False) == {"channel_id" : 0000}
    
def test_channels_create_bad(): 
    #case where name is too long
    dictionary = auth_register("geoffrey.he777@gmail.com", "PigBabo", "Geoffrey", "He")
    u_id = dictionary["u_id"]
    token = dictionary["token"]
    
    with pytest.raises(ValueError): 
        #case public channel
        channels_create(token, "this name is way too long so it will cause an error", True)
        #case private channel
        channels_create(token, "this name is way too long so it will cause an error", False)

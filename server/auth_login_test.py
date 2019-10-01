import pytest
from f_auth_login import auth_login

def test_auth_login(): 
    #no capitals
    assert auth_login("besthearthstoneplayer@gmail.com", "bigpabo") == ("besthearthstoneplayer@gmail.com", "1bigpabo")
    #capitals 
    assert auth_login("BestHearthstonePlayer@gmail.com", "BigPabo") == ("BestHearthstonePlayer@gmail.com", "1BigPabo")
    #numbers
    assert auth_login("besthearthstoneplayer@gmail.com", "b1gp4b0") == ("besthearthstoneplayer@gmail.com", "1b1gp4b0")
    #numbers in email
    assert auth_login("rank87legend@gmail.com", "bigpabo") == ("rank87legend@gmail.com", "1bigpabo")
    #special expressions in email
    assert auth_login("Message.To.Daniel.Kang@gmail.com", "Jihyo") == ("Message.To.Daniel.Kang@gmail.com", "1Jihyo")
    #non-gmail emails
    assert auth_login("IC_THAT_IM_ICY@microsoftoutlook.com", "ITZY5") == ("IC_THAT_IM_ICY@microsoftoutlook.com", "1ITZY5")
    
def test_auth_login_bad():
    with pytest.raises(Exception):
        #short password
        auth_login("besthearthstoneplayer@gmail.com", "b")
        #capital short password
        auth_login("besthearthstoneplayer@gmail.com", "B")
        #short numerical password
        auth_login("besthearthstoneplayer@gmail.com", "87")
        #invalid email
        auth_login("besthearthstoneplayer.com", "bigpabo")
        #special expression invalid email
        auth_login("Message.To.Daniel.Kanggmail.com", "jihyo")
        #numerical invalid email
        auth_login("rank87legend.com", "bigpabo")
        #short password and invalid email
        auth_login("besthearthstoneplayer.com", "b")
        
        

import pytest
from f_auth_register import auth_register
   
def test_auth_register(): 
    #no capitals 
    assert auth_register("besthearthstoneplayer@gmail.com", "bigpabo", "daniel", "kang") == {'u_id' : "besthearthstoneplayer@gmail.com", 'token' : "1bigpabo"}
    #capitals 
    assert auth_register("BestHearthstonePlayer@gmail.com", "BigPabo", "DANIEL", "KANG") == {'u_id' : "BestHearthstonePlayer@gmail.com", 'token' : "1BigPabo"}
    #numbers
    assert auth_register("besthearthstoneplayer@gmail.com", "b1gp4b0", "D4N13L", "K4NG") == {'u_id' : "besthearthstoneplayer@gmail.com", 'token' : "1b1gp4b0"}
    #special expressions in email, name_first and name_last
    assert auth_register("Message.To.Daniel.Kang@gmail.com", "Jihyo", "Da^#%#", "K&#&*(#") == {'u_id' : "Message.To.Daniel.Kang@gmail.com", 'token' : "1Jihyo"}
    #non-gmail emails and spaces in the name_first and name_last
    assert auth_register("IC_THAT_IM_ICY@microsoftoutlook.com", "ITZY5", "MESSAGE TO", "DANIEL KANG") == {'u_id' : "IC_THAT_IM_ICY@microsoftoutlook.com", 'token' : "1ITZY5"}
    
    
    
    
def test_auth_register_bad(): 
    with pytest.raises(ValueError):
        #first name too long
        auth_register("besthearthstoneplayer@gmail.com", "bigpabo", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf", "a")
        #last name too long
        auth_register("besthearthstoneplayer@gmail.com", "bigpabo", "a", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf")
        #short password
        auth_register("besthearthstoneplayer@gmail.com", "b", "Big", "Pabo")
        #capital short password
        auth_register("besthearthstoneplayer@gmail.com", "B", "Big", "Pabo")
        #short numerical password
        auth_register("besthearthstoneplayer@gmail.com", "87", "Big", "Pabo")
        #short password and first name too long
        auth_register("besthearthstoneplayer@gmail.com", "b", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf", "Pabo")
        #short password and last name too long
        auth_register("besthearthstoneplayer@gmail.com", "b", "Pabo", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf")
        #invalid email
        auth_register("besthearthstoneplayer.com", "bigpabo", "Big", "Pabo")
        #invalid email and first name too long
        auth_register("besthearthstoneplayer.com", "bigpabo", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf", "Pabo")
        #invalid email and last name too long
        auth_register("besthearthstoneplayer.com", "bigpabo", "Big", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf")
        #special expression invalid email
        auth_register("Message.To.Daniel.Kanggmail.com", "jihyo", "Big", "Pabo")
        #numerical invalid email
        auth_register("rank87legend.com", "bigpabo", "Big", "Pabo")
        #short password and invalid email
        auth_register("besthearthstoneplayer.com", "b", "Big", "Pabo")
        #short password, invalid email and first name too long
        auth_register("besthearthstoneplayer.com", "b", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf", "Pabo")
        #short password, invalid email and last name too long
        auth_register("besthearthstoneplayer.com", "b", "Pabo", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf")
        #short password, invalid email, last name too long and first name too long
        auth_register("besthearthstoneplayer.com", "b", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf", "asldakdhfakjhdfrkalfhrgakljdhgfalkhgfakldhgfkalhgfdlkjhgflkhagklsdgfahsdgfaljkhdgfajkldhsgfjkahdgfkajlgf")
        
        
        
        
        
        
        
        
        
        
        
        
        
        

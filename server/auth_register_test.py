# Function name: auth_register()
# Parameters: (email, password, name_first, name_last)
# Return type: { u_id, token }
# Exception: ValueError when:
# - Email entered is not a valid email.
# - Email address is already being used by another user
# - Password entered is not a valid password
# - name_first is more than 50 characters
# - name_last is more than 50 characters
# Description: Given a user's first and last name, email address, and password, 
# create a new account for them and return a new token for authentication in their session
#

import pytest
import f_auth_register
import json_functions
from myexcept import ValueError

def test_unit_auth_register():
	json_functions.data_test_initiate()

	# Testing for the first user who registers with auth_register

	data = json_functions.getData()
	print(data)

	authRegisterDic = f_auth_register.auth_register("valid1@email.com", "valid1password", "first1name", "last1name")
	token_one = authRegisterDic['token']
	u_id_one = authRegisterDic['u_id']

	json_functions

	# Checking that the data values have been input correctly
	# Checking that the first user's permission is set to Owner (permission_id = 1)

	user_found = False

	data = json_functions.getData()
	for user in data['users']:
		if user['email'] == "valid1@email.com":
			user_found = True
			assert user['token'] == token_one
			assert user['u_id'] == u_id_one
			assert user['permission_id'] == 1

	if user_found == False:
		raise ValueError('Error, user not found in data')

	# Testing for the second user who registers with auth_register

	authRegisterDicTwo = f_auth_register.auth_register("valid2@email.com", "valid2password", "first2name", "last2name")
	token_two = authRegisterDicTwo['token']
	u_id_two = authRegisterDicTwo['u_id']

	# Checking that the data values have been input correctly
	# Checking that the first user's permission is set to User (permission_id = 3)

	user_found = False

	data = json_functions.getData()
	for user in data['users']:
		if user['email'] == 'valid2@email.com':
			user_found = True
			assert user['token'] == token_two
			assert user['u_id'] == u_id_two
			assert user['permission_id'] == 3

	if user_found == False:
		raise ValueError('Error, user not found in data')

'''
def test_auth_register(): 
    jsonClean()
    # SETUP BEGIN

    authRegisterDic = auth_register("valid9@email.com", "valid9password", "first9name", "last9name")
    token = authRegisterDic['token']
    u_id = authRegisterDic['u_id']
    
    # SETUP END
    
    # Testing auth_logout function to check that I successfully registered
    auth_logout(token)
    
    # Testing auth_login function to check that the account was successfully registered
    assert auth_login("valid9@email.com", "valid9password") == { 'token' : token, 'u_id' : u_id }
'''   
   
def test_auth_register_bad(): 
	json_functions.data_test_initiate()

	data = json_functions.getData()

	authRegisterDic = f_auth_register.auth_register("valid1@email.com", "valid1password", "first1name", "last1name")
	token_one = authRegisterDic['token']
	u_id_one = authRegisterDic['u_id']

	invalid_name = 'a' * 51

	with pytest.raises(ValueError):
		# Testing function with invalid email 
		f_auth_register.auth_register("invalidemail", "validpassword1", "firstname1", "lastname1")
	with pytest.raises(ValueError):	
		# Testing function with already registered email
		f_auth_register.auth_register("valid1@email.com", "validpassword1", "firstname1", "lastname1") 
	with pytest.raises(ValueError):
		# Testing function with invalid password
		f_auth_register.auth_register("valid2@email.com", "ivp", "firstname1", "lastname1")
	with pytest.raises(ValueError):	
		# Testing function with invalid first_name
		f_auth_register.auth_register("valid3@email.com", "validpassword1", invalid_name, "lastname1")
	with pytest.raises(ValueError):	
		# Testing function with invalid last_name
		f_auth_register.auth_register("valid4@email.com", "validpassword1", "firstname1", invalid_name)

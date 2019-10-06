Assumptions

In iteration 1, we assumed that there were no databases included
For the functions that had no return value, we have made it to just return an empty dictionary and also when testing, we have asserted that it returns an empty dictionary
We assumed that, since the “thread” functionality in the Slack app is not mentioned in the assignment spec, we do not need to implement it in our test cases or as an actual function itself
We assumed that we are writing our test cases as if we are testing actual, implemented functions
We assumed that for Admin and Owner roles, they had the same permissions but an Admin cannot make other members an Owner, and the workspace hierarchy is Owner -> Admin -> Member, while the channel only has Owner -> Member
Since we were unable to test the output of some of the functions we assumed we could use other functions to test assuming that they are working correctly
We assumed that we are implementing the backend for Slackr to both an app and a website
We wrote our tests based on the assumption that we cannot reset our code
We assumed that all AccessErrors are ValueErrors for the first iteration
We assumed that dictionary[“all_members”] is a list of dictionaries that does not include Owners, only Admins and Members are included
We assumed that dictionary[“owner_members”] is a list of only Owners, where Admins and Members are not included

Function Assumptions

Assumed for all functions that passes “token” as an argument:
Assumed that all functions pass in a token, even though the specification did not state it
Assumed that the token is a unique, non-negative integer and matches the correct user
Assumed for all functions that passes “channel_id” as an argument:
Assumed that the channel ID is a non-negative integer and not a string
Assumed for all functions that passes “u_id” as an argument:
Assumed that the user ID is a non-negative integer and not a string
Assumed for all functions that pass “message_id” as an argument:
Assumed that the message_id is a valid, unique, and non-negative integer

Auth_login:
Assumed that the user is not logged in
Assumed that user is inputting english characters/integers only
Assumed that the returned user ID is a unique non-negative integer ID that matches the login credentials of that user
Assumed that the returned token value is a unique non-negative integer token and is not the same as another token currently in use
Auth_logout:
Assumed that the user is already logged in
Auth_register:
Assumed that user is inputting english characters/integers only
Assumed that the returned user ID is a unique non-negative integer ID that matches the login credentials of that user
Assumed that the returned token value is a unique non-negative integer token and is not the same as another token currently in use
Assumed that users can register under the same first and last names, but cannot register using the same email
Assumed that users can also register using the same password
Auth_passwordreset_request:
Assumed that the email address is valid and exists, as no exception is raised when it is invalid
Assumed that we couldn’t access the email to check if it was successfully sent
Auth_passwordreset_reset:
Assumed that user is inputting english characters/integers only
Channel_invite:
Assumed that the channel has at least one owner
Assumed that “channel_join” is the same as channel invite, whereby inviting them and setting them to a member
Channel_details:
Assumed that the return values for name, owner_members and all_members are correct and are all in the correct channel from the channel ID provided
Assumed that the “Owner” user is marked differently to the other members
Channel_messages:
Assumed that ‘start’ is a non-negative integer and not a string
Assumed that messages returned a valid dictionary and that each message was a string less than 1000 characters
Channel_leave:
Assumed that the channel has at least one other member
Assumed that if the owner leaves, the owner role is passed onto either another owner, or an admin, or another user
Channel_join:
Assumed that the channel has at least one owner
Assumed that “channel_invite” is the same as channel join, whereby setting their role as a member
Channel_addowner:
Assumed that the owner is not the only member of the channel
Assumed that the owner can make either a member or admin but not an owner, an owner
Channel_removeowner:
Assumed that the owner is not the only member of the channel
Channels_list:
Assumed that “channels” returns a valid dictionary
Assumed that this function shows every channel that the user is a part of
Channel_listall:
Assumed that “channels” returns a valid dictionary
Assumed that this function shows every channel in the workspace
Channels_create:
Assumed that “name” is a string and not an integer
Assumed that “is_public” is either True or False
Assumed that channel_id returns a valid, unique, and non-negative integer which corresponds to the correct channel that is being created
Assumed that two channels can not have the same channel name
Message_sendlater:
Assumed that message is a string and not an integer
Assumed that time_sent is of the correct datetime format “DD/MM/YYYY”
Assumed that since “channel_messages” returns messages, we found it too challenging to test the function with “channel_messages” to view the messages as messages requires:
{ message_id, u_id, message, time_created, is_unread }
Message_send:
Assumed that the message is a string and not an integer
Assumed that the correct message is sent to the correct channel
Assumed that since “channel_messages” returns messages, we found it too challenging to test the function with “channel_messages” to view the messages as messages requires:
{ message_id, u_id, message, time_created, is_unread }
Message_remove:
Assumed that the correct message is removed by the authorised user
Assumed that since “channel_messages” returns messages, we found it too challenging to test the function with “channel_messages” to view the messages as messages requires:
{ message_id, u_id, message, time_created, is_unread }
Message_edit:
Assumed that message is a string and not an integer
Assumed that the message is edited to the correct message
Assumed that since “channel_messages” returns messages, we found it too challenging to test the function with “channel_messages” to view the messages as messages requires:
{ message_id, u_id, message, time_created, is_unread }
Message_react:
Assumed that the react_id is a non-negative integer and not a string
Message_unreact:
Assumed that the react_id is a non-negative integer and not a string
Message_pin:
Assumed that there were no limits to the amount of pinned messages
Message_unpin:
Assumed that there was at least one message already pinned
User_profile:
Assumed that the returned strings are correct and match the correct user from the given user ID
User_profile_setname:
Assumed that “name_first” and “name_last” are strings and not integers
User_profile_setemail:
Assumed that the email is their own email
User_profile_sethandle:
Assumed that the user enters a string for “handle_str” and not an integer
Assumed that this function both updates or creates a handle if the handle does not exist 
User_profiles_uploadphoto:
Assumed that “img_url” is an actual URL string
Assumed that the image is of  .png, .jpg or .jpeg type
Standup_start:
Assumed that there were at least two people in the channel for the standup
Standup_send:
Assumed that the startup is still ongoing and hasn’t ended
Assumed that there were at least two people in the channel for the standup
Search:
Assumed that the “query_str” was valid, as there was no error checking
Assumed that the string cannot be an empty string
Admin_userpermission_change:
We assumed that the user inputs an integer between 1 and 3 for “permission_id”
We assumed that there were at least two users, the owner and an admin or a member to change user permissions
We also assumed that not any user could change the permissions of other users (not mentioned in the specification)
“Members in a channel have two permissions:
1) Owner of the channel (the person who created it, and whoever else that creator adds)
2) Members of the channel”

“Slackr user's have three permissions
1) Owners, which have the same privileges as an admin (permission_id 1)
2) Admins, who have special permissions that members don't (permission_id 2)
3) Members, who do not have any special permissions (permission_id 3)”

We assumed that this function is the only way to change a user’s role to Admin or Owner, where Admin is set in the workspace and Owner can be set in both the workspace or channel.
We assumed that this function changes the permission of a user in a workspace, since it is labelled “Admin_userpermission_change” and only the workspace has an Admin role
Additional function assumption: Auth_delete_account - We assumed that we will require this function as it would be unfeasible to write test functions using a large amount of emails

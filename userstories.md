COMP1531 ITERATION 1 Thom_Browne


EPIC STORY 1: User should be able to login to a unique profile from the website, and can simply logout


ID: US 1.1
Name: User unique login/authorization
User-Story Description: As a user, I want to be able to log in with an email and password so that I can access the user portal
Acceptance Criteria: 
Upon entering the correct combination, the user will be able to view their own portal, direct messages, channels etc.

Priority: Essential

Size: 4 Hours

ID US 1.2 
Name: Invalid login
User-Story Description: As a user, I want to restrict other individuals to be unable to access my portal so that it is more secure 
Acceptance Criteria: 
When entering the incorrect combination, a warning message will be presented and access will be denied

Priority: Essential

Size: 2 Hours



ID US 1.3 
Name: Register account
User-Story Description: As a user, I want to be able to register for a new account so that I can login to the website
Acceptance Criteria: 
User needs to provide the email, password, first name and last name

Priority: Essential

Size: 3 Hours


ID US 1.4
Name: Password reset
User-Story Description: As a user, I want to be able to reset my password so that I can reset my password if I forget it
Acceptance Criteria: 
After the user provides their email address, a safety code will be sent to the user’s email inbox
User needs to enter the correct safety code to reset password

Priority: Essential

Size: 3 Hours

ID US 1.5 
Name: User logout
User-Story Description: As a user, I want to be able to logout from portal so that I can easily exit my account
Acceptance Criteria: 
After the user click logout, the login page should be prompted

Priority: Essential

Size: 3 Hours

EPIC STORY 2: Users can access the functionality of the channels


ID: US 2.1
Name: View channels
User-Story Description: As a user, I would like to view the list of channels which I have already joined, so that I can easily choose channels to open
Acceptance Criteria: 
Users can find the list of channels at the left side of the panel
Users can click the “channels browser”, then the whole list of the channels will be shown

Priority: Essential

Size: 2 Hours


ID US 2.2
Name: Search channels
User-Story Description: As a user, I want to be able to find channels so that I can quickly open them
Acceptance Criteria:
At the “channels browser”, after the user enters the channel name, the certain channel will be prompted

Priority: Optional

Size: 3 Hours

ID US 2.3
Name: Create channels
User-Story Description: As a user, I want to be able to create new channels so that I can work or communicate with my partners
Acceptance Criteria: 
Users need to provide the channel name
Users can make new channel to be private or public
Private: the channel can only be viewed or joined by invitation

Priority: Essential

Size: 3 Hours

ID US 2.4
Name: View channel name
User-Story Description: As a user, I want to be able to see the channel name which is already open so that I know which channel I am using
Acceptance Criteria: 
After the user opens a channel, the name of the channel is placed at the top of the channel

Priority: Essential

Size: 1 Hour

ID US 2.5
Name: View channel members
User-Story Description: As a user, I want to be able to see the members in the channel which already opened so that I know who I am contacting with
Acceptance Criteria: 
After the user clicks the “About this channel” button, the list of the members who are in the channel should be shown
The list of the members should also mark who is the owner

Priority: Essential

Size: 3 Hours

ID US 2.6
Name: View and Send message
User-Story Description: As a user, I want to be able to see and send messages in the channel so that I can communicate with others efficiently
Acceptance Criteria: 
Users can type and send their messages to the channel
Channel panel shows all the messages which are sent by users

Priority: Essential

Size: 2 Hours

ID US 2.7
Name: Invite people
User-Story Description: As a user, I want to be able to invite my friend to the channel so that I can communicate with my friends
Acceptance Criteria: 
User can enter the name which is in the friend list, and add them to the channel  

Priority: Essential

Size: 3 Hours

ID US 2.8
Name: Leave or join channel
User-Story Description: As a user, I want to be able to leave or join the channel so that I can manage the channel easily
Acceptance Criteria: 
After user clicks the leave button, the panel will not show that channel
After user clicks the join button, the panel will show the new channel

Priority: Essential

Size: 2 Hours

ID US 2.9
Name:  Make channel owner
User-Story Description: As a user, I want to be able to make another channel owner so that I can manage my own channel easily
Acceptance Criteria: 
Owner can choose the member which is in the channel to be the other owner

Priority: Essential

Size: 3 Hours

ID US 2.9.1
Name: Edit messages
User-Story Description: As a user, I want to be able to edit messages which already send to the channel so that I can avoid some misunderstanding and make my messages unique
Acceptance Criteria: 
Users right click the certain message, and it will show:
Pin message: the message will be brought to the top
Remove pin: the message will go to the original place
React message: show a react emoji to the message
Remove react: the react emoji disappears 
Rewrite message: message can be rewritten to make changes
Delete message: message disappears from the channel

Priority: Desirable

Size: 3 Hours

ID US 2.9.2
Name: Send later
User-Story Description: As a user, I want to be able to send my message in a certain time so that I can send messages flexibly
Acceptance Criteria: 
Before the user sends their message, there will be a date option, where the user can choose the date and time, and the message will be sent at the chosen time

Priority: Optional

Size: 3 Hours

ID US 2.9.3
Name: Conclude messages
User-Story Description: As a user, I want to be able to view the summary messages so that I can have a clearly, summarised message as a conclusion
Acceptance Criteria: 
After user sends “/standup”, there will be a 15-min window to start whereby the following messages sent in that channel all get collected up by the server 
After 15-min, the summary messages will be shown in the threads

Priority: Desirable

Size: 5 Hours

ID US 2.9.4
Name: View profile
User-Story Description: As a user, I want to be able to view another member’s profile picture and name so that I can easily recognise the member
Acceptance Criteria: 
When the user right clicks another member’s name, it will show the profile picture and the name of that person

Priority: Essential

Size: 3 Hours

ID US 2.9.5
Name: Edit own profile
User-Story Description: As a user, I want to be able to edit my own profile so that other people can recognize me easily
Acceptance Criteria: 
When the user right clicks their own name, it will show the following profile settings:
User can upload a new profile picture
User can edit name
User can change default handle, which combines their first and last name
Add own email address

Priority: Essential

Size: 4 Hours

ID US 2.9.6
Name: Search messages
User-Story Description: As a user, I want to be able to search relevant messages so that if I forget some information, I am able to obtain more precise information from channel history
Acceptance Criteria: 
After the user enters the information to the search bar, there will be some relevant messages list under the search bar

Priority: Essential

Size: 5 Hours

ID US 2.9.7
Name: View channel detail
User-Story Description: As a user, I want to be able to view the details of the channel so that I can have a rough understanding of the channel
Acceptance Criteria: 
User can view the brief introduction of the group in the specific channel panel

Priority: Essential

Size: 3 Hours

EPIC STORY 3: As an admin, I want to manage the number of admins


ID: US 3.1
Name: Manage admins
User-Story Description: As an admin, I want to be able to make other users to be admin or not so that I can manage the admins
Acceptance Criteria: 
Admin can choose user to be admin
Admin can choose admin to be user

Priority: Optional

Size: 4 Hours

EPIC STORY 4: Admin should be able to login to a unique profile that is hidden from a user’s view. 


ID: US 4.1
Name: Admin login
User-Story Description: As an admin, I want to be able to log in with a username and password so that I can access the admin portal 
Acceptance Criteria: 
A unique admin ID and password will be provided to admin
Upon entering this combination admin will be able to view the admin-required information, admins list etc.

Priority: Desirable

Size: 4 Hours

ID US 4.2
Name: Invalid login
User-Story Description: As an admin, I want unauthorised individuals to be unable to access my portal so that it is more secure 
Acceptance Criteria: 
When entering the incorrect combination, a warning message will be presented and access will be denied 

Priority: Desirable

Size: 4 Hours

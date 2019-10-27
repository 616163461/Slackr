Assurance (Thom Browne)

Required:
Provide assurances that your backend implementation is fit for purpose. Consider both verification and validation when doing this. This will, at a minimum, require acceptance criteria for your user stories.

 - Demonstration of an understanding of the need for software verification and validation
 - Development of appropriate acceptance criteria based on user stories and requirements
 - Demonstration of appropriate tool usage for assurance (code coverage, linting, etc.)

Verification (Producer’s view of quality):
Verification is the process of evaluating software at intermediate stages when being developed to ensure that it will meet project requirements and specifications derived from user stories.  This means that we can ensure the customer that each part of the code will work exactly the way it was meant to work.  Sometimes this can be difficult since the most thorough verification process is formal verification.  This method involves proving in a mathematical style that the piece of software contains certain required properties that was specified before development started.  However, formal verification isn’t widely used and is not covered in this course due to its high cost in regards to manpower and time.  For Slackr we utilised various levels of testing instead such as unit testing and integration testing as a form of insurance that our functions all perform as per the system requirements.  Our unit tests were initially written using a black-box method since we didn’t have access to the functions, but were later updated and improved on using a white-box method after we had written all the functions.   Finally to confirm that our functions worked correctly in respect to each other we did white-box integration testing with a few related functions at the time.  Hence through thorough testing processes we can assure that our Slackr functions will satisfy all the acceptance criteria.

Validation (Consumer’s view of quality):
Validation is also extremely useful as it makes sure that the product meets the intended purpose. It is the process of evaluating the final product to check whether the software meets the business needs. The techniques that are included in validation are: Unit testing and User acceptance testing, whereby ensuring that the system is working according to the plan. 

Validation is the process of evaluating the overall software at the final stage with respect to the customer’s requirements so that it satisfies all the user requirements demonstrating an accurate interpretation of user stories.  This aspect focuses on the customers satisfaction and feedback.

Below is a list of our Iteration 1 Acceptance criteria:
Upon entering the correct combination, the user will be able to view their own portal, direct messages, channels etc.
When entering the incorrect combination, a warning message will be presented and access will be denied
User needs to provide the email, password, first name and last name to log in
After the user provides their email address, a safety code will be sent to the user’s email inbox
User needs to enter the correct safety code to reset password
After the user click logout, the login page should be prompted
Users can find the list of channels at the left side of the panel
Users can click the “channels browser”, then the whole list of the channels will be shown
At the “channels browser”, after the user enters the channel name, the certain channel will be prompted
Users need to provide the channel name
Users can make new channel to be private or public
Private: the channel can only be viewed or joined by invitation
After the user opens a channel, the name of the channel is placed at the top of the channel
After the user clicks the “About this channel” button, the list of the members who are in the channel should be shown
The list of the members should also mark who is the owner
Users can type and send their messages to the channel
Channel panel shows all the messages which are sent by users
User can enter the name which is in the friend list, and add them to the channel  
After user clicks the ‘leave’ button, the panel will not show that channel
After user clicks the join button, the panel will show the new channel
Owner can choose the member which is in the channel to be the other owner
Users right click the certain message, and it will show:
Pin message: the message will be brought to the top
Remove pin: the message will go to the original place
React message: show a react emoji to the message
Remove react: the react emoji disappears 
Rewrite message: message can be rewritten to make changes
Delete message: message disappears from the channel
Before the user sends their message, there will be a date option, where the user can choose the date and time, and the message will be sent at the chosen time
After user sends “/standup”, there will be a 15-min window to start whereby the following messages sent in that channel all get collected up by the server
After 15-min, the summary messages will be shown in the threads
When the user right clicks another member’s name, it will show the profile picture and the name of that person
When the user right clicks their own name, it will show the following profile settings:
User can upload a new profile picture
User can edit name
User can change default handle, which combines their first and last name
Add own email address
After the user enters the information to the search bar, there will be some relevant messages list under the search bar
User can view the brief introduction of the group in the specific channel panel
Admin can choose user to be admin
Admin can choose admin to be user
A unique admin ID and password will be provided to admin
Upon entering this combination admin will be able to view the admin-required information, admins list etc.
When entering the incorrect combination, a warning message will be presented and access will be denied

As we had written the acceptance criteria for Iteration 1, we would have to ensure that we have met those criterias. Our group had effectively worked off the list of criterias that we needed to meet, ticking off each point as we worked on the functions. At the end of our implementation of functions, we would go back and double check to see that we’ve met every single acceptance criteria. 

Tools used for assurance
For assurance, our team had used “coverage.py” to test our code coverage. Because code coverage is one of the core criteria for each milestone, we have also utilised unit tests coverage, and once they’ve met our standard requirement of 90% test and code coverage, we would then move to the next milestone. 

Before finalising all functions, we would first test every function against every “..._test.py” file for unit testing. As unit testing is more focused towards software engineering testing, we would each divide our functions and test them against their corresponding test file. Following on from unit testing, we would then test the functions that had required the functionality of other functions under integration testing. An example of this would be where “/standup/send” would require the functionality of “/standup/start”. This would ensure that there would be minimal error handling when we combine all the functions together. Once we had completed our functions, we would then compile all our functions into the “server.py” file. This stage is our systems testing step, where once we had completed our integration testing, we would then progress into testing our whole system. 

Our group had also used Python’s pylint to check our functions if they had any programmatic and stylistic errors. Our method of implementing the functions had comprised of: writing the code and compiling it, analyzing it with pylint, reviewing the bugs identified by the tool, followed by making changes to resolve the bugs, and then analyzing the functions again with pylint until there were no errors.


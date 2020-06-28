                            SKILLUP
Skillup is a learning management system designed to help users get up to speed in their different careers/disciplines. Users could sign up for a course and then learn at their own pace through video lectures. The application is programmed in python integrated with SQLite database.
The Application primarily features three panels:
1.	THE ANONYMOUS USER PANEL:  Features for this panel include:
a)	Ability to browse through courses either through their categories and subjects or through the site’s search engine.
b)	Ability to send contact messages to the admin for any enquiry of their choosing
c)	Ability to sign up and login to become a registered member.

2.	THE REGISTERED USER PANEL: Features for this panel include:
a)	Ability to login
b)	Ability to enroll for a course
c)	Ability to view the courses enrolled and take the video lessons
d)	Ability to view and edit personal profile information.

3.	THE ADMIN USER PANEL: Features for this panel include:
a)	Ability to manage courses (editing and updating the courses and the topics)
b)	Ability to view contact messages and decide on the action to take concerning those
c)	Ability to view and edit personal profile information.

Future additions could be:
a)	Ability for the admins to respond to contact messages through the email handles submitted by the user.
b)	Accepting external instructors and allowing them to upload courses that will be verified by the admin before being approved
c)	Capturing more learning fields and courses (Currently, the app captures only the architecture, computing, photography, and business fields)
d)	Monetizing the app by allowing users to pay for the courses they enroll through a payment gateway.

APP STRUCTURE: Currently there is only one app (skillup) which houses the following:
a)	The views.py (which houses all the different views for the entire application)
b)	Models.py (the file for all the database models)
c)	Urls.py (the file for all the url endpoints)
d)	Templates (the folder for all the front-end templates)
e)	Static (the folder for all the static files example: css, javascript, images etc)

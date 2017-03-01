Bootcamp Bit

https://github.com/GatorisGreater/bootcamp-bit

Description:

Everyday you pair program with a different cohort partner. By the time you graduate you'll pair multiples times with the same person and will have created more than 50 project folders. Keep track of your pairings and project folders with Bootcamp Bit.

User Experience:
Before kicking off your pair programming for the day query by cohort mate to see what projects you've worked on together throughout your bootcamp experience. This could jog your memory about things you meant to close the loop on or be good for a few laughs.

Tech Stack:

├ bootcamp-bit
├── run.py: server-side code and logic 
│ 
├── templates: HTML templates 
│ └── child.html
│ └── macros.html
│ └── parent.html

*Flask - implements API endpoints that serve resources to the app.

*Jinja2 - HTML templates for dynamic client-side rendering of the app.

Bootcamp Bit is designed with bootcamp students in mind.

Abbreviated MVP Implementation:

API - GET endpoints that serve the projects you've worked on with each cohort member. 

Front-End - Response presented within a dynamic HTML page customized for the cohort member you've queried.

Database - None. Data is stored within endpoints.

Future Improvements:

Dashboard integration to advance "native" experience.

GitHub integration that automatically detects repos and collaborators.

Database Implementation.

PUT endpoints that allow the user to update the database as they move along their bootcamp experience.
Bootcamp Bit

https://github.com/GatorisGreater/bootcamp-bit

Description:

Everyday you pair program with a different cohort partner. By the time you graduate you'll pair multiples times with the same person and will have created more than 50 assignment folders. Keep track of your pairings, assignments, and what you owe your program manager with Bootcamp Bit.

User Experience:
Before kicking off your pair programming for the day query by cohort mate to see which assignments you've worked on together throughout your bootcamp experience. This could jog your memory about an open item or remind you of how far you've come.

Tech Stack:

    ├ bootcamp-bit
    ├── run.py: server-side code and logic 
    │ 
    ├── templates: HTML templates 
    │ └── add_assignment.html
    │ └── child.html    
    │ └── delete_assignment.html    
    │ └── macros.html
    │ └── parent.html

* Flask - implements API endpoints that serve resources to the app.

* Jinja2 - HTML templates for dynamic client-side rendering of resources.

Bootcamp Bit is designed with bootcamp students in mind.

Abbreviated MVP Implementation:
* Hardcoded user experience for Spencer.

* API - GET endpoints that serve the assignments you've worked on with each cohort member. 

* Front-End - Response presented within a dynamic HTML page customized for the cohort member you've queried.

* Database - None. Data is stored within endpoints.

Future Improvements:

* Dashboard integration to advance "native" experience. It would also serve as an administrative tool for PMs (finish up delete assignment endpoint).

* GitHub integration that automatically detects repos and collaborators.

* Database Implementation.
# Enfy Server - Using fastApi & SQL Alchemy

Techs used in this project:

- Language: Python
- Framework: fastApi
- ORM: SQL Alchemy
- DB: postgres

Structure Plan:

Enfy-Server: - app 
                -- models
                -- router
                -- services
                -- database.py
                -- main.py


DEV-LOGS:

- 10 february 2026: 

    Today I added the basic structure of the app. I implemented the initial user endpoints, services, and schemas, set up the database connection, and created the user model.

- 11 February 2026:
    Today I implemented Login Endpoint and a Small fix in the Register Endpoint

- 12 february 2026:

    Today I implemented the event structure, models, endpoints, and services. My initial plan for this branch was to add all of that along with the search engine. However, the day is almost over and I was only able to complete the events part. I plan to finish the search engine tomorrow and then push the commits to the main branch.

- 13 february 2026:
    I implemented the search engine, it works nicely using the name or description for search in the events table and return the events that match with the name or the description, anyways, Maybe in a future i will add the user search or maybe not.

- 14 February 2026:
    Today I Implemented JWT to the Project for security

- 16 February 2026:
  Today I Implemented a new Endpoint for fetchEvents

- 19 February 2026: 
    Today I Implemented a Small fix for the token check and added the user fetch endpoints

- 20 February 2026:
    Today I Started the Fix of the create event Endpoint

- 21 February 2026:
    Today I finished the fix of the create event endpoint and fix another small problems

- 22 February 2026:
    Today I Fixed some minor details

- 24 February 2026:
    Today I implemented support for buy many Tickets by the same user.

- 25 February 2026:
    Today I implemented the endpoint for fetch tickets, so the user will know how many 
    tickets he have for an specific event

- 26 February 2026:
    Today I Implemented the endpoint for change an user profie picture, I plan to create the Recommended Events function and some functions for companies and admins tomorrow.

- 28 February 2026:
    Today I implemented the system to obtain recommended events for the user. First, when you create a user, you also create "categories" preferred by the user, previously selected on the frontend. After that, the user makes a request to obtain the recommended events every time they are on the home page.

- 1 March 2026:
    Implemented logout function

- 3 March 2026:
    I Fixed the recommended events fetch
# KoHack2022 
> App Name: MaimoMikdash

> Developers: Ephraim Fischer, Alon Baker, Roee Weglein

> Team/School: Maimonides
## This program runs on SQL and uses specialized software and files made specially for this project. You will not be able to run this locally on your computer, so I will be running it on mine to demonstrate the project
### Directory layout

    ├──Lib                                                     # This folder contains all of the packages that makes the site work
    ├──flask_session                                           # This folder contains some of the user session ID's (This will change as different users sign in)
    ├──Scripts                                                 # This folder contains different bash and bin scripts to activate and deactivate the VENV
    ├── Templates                                              # HTML files (frontend)
    │       ├── kohen_login.html                               # This file is the HTML site that is returned when the Kohen isn't logged in
    │       ├── kohen.html                                     # This file is the HTML site that has all of the Kohen raffle information
    │       ├── reservations.html                              # This file is the HTML site that contains the Korban reservation forms
    │       ├── sanhedrin.html                                 # This file is the HTML site that contains the Sanhedrin request forms
    │       ├── login.html                                     # This file is the HTML site that contains the standard user login
    │       ├── signup.html                                    # This file is the HTML site that contains the standard user sign up
    │       └── index.html                                     # This file is the HTML site that the user initially sees when going to the website
    ├── static                                                 # static Images, JS and CSS files (frontend)
    │       ├── landing.css                                    # This file contains all of the styling for index.html
    │       ├── k_login.css                                    # This file contains all of the styling for kohen_login.html
    │       ├── kohen.css                                      # This file contains all of the styling for kohen.html
    │       ├── login.css                                      # This file contains all of the styling for login.html
    │       ├── mikdash.png                                    # IMAGE file for the logo of the site
    │       ├── sanhedrin.css                                  # This file contains all of the styling for sanhedrin.html
    │       ├── signup.css                                     # This file contains all of the styling for signup.html
    │       └── reservations.css                               # This file contains all of the styling for reservations.html
    ├── app.py                                                 # This file is the Python code for the API itself and all of the backend algorithms
    ├──pyvenv.cfg                                              # This is a configuration file for the VENV
    ├──kohack2022.sql                                          # Sample database values and database table code. This is just a sample, and not the actual database
    ├──requirements.txt                                        # Packages needed for the code to run
    └── README.md                                              # You are here


### Features

    1: Korban Reservation System: The implementation for this is stored in the app.py file and in templates/reservations.html

    2: Kohen Automated Job Lottery: The implementation for this is stored in the app.py file, in templates/kohen_login.html, and in templates/kohen.html

    3: Sanhedrin Lawsuit Requesting System: The implementation for this is stored in the main.py file and in templates/sanhedrin.html

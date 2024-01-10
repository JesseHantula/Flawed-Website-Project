# Flawed-Website-Project


The following project was created for the Introduction to Cybersecurity course at the University of Helsinki. 
Provides 5 examples of security flaws and shows fixes for each of them. The 5 vulnerabilities in the project are:
1. Identification and Authentication Failures
2. Broken Access Control
3. Injection
4. CSRF Attacks
5. Security Logging and Monitoring Failures

In order to run the application, simply clone the repository and navigate to the manage.py file. Once there, run the following commands:

`python manage.py makemigrations`

`python manage.py migrate`

This initializes the SQL database. Once these commands have been run, the server can be started by running:

`python manage.py runserver`

The web server can be found with the following URL:
[localhost:8000](localhost:8000)

There are two ready-made accounts that can be used, with the following credentials:
User: alice Password: redqueen
User: bob Password: squarepants

The code is documented in order to showcase the security flaws. You can also read the report I made that explains the flaws and application in more details:

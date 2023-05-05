# Python - Week 5 Day 3 - Login & Registration 
        
## ******************************************

- Office Hours:  4:00 PM PST
- Lecture:       5:00 PM PST

## ******************************************

## Office Hour

- Troubleshooting

## Lecture

### Objectives

- Understand the process of authorization and authentication
- understand bcrypt and why we use it
- create a login and registration process

### Process

- start virtual environment
- pipenv install flask pymysql flask-bcrypt
- set up server.py
- modularize project
    - Main project folder
        - flask_app
            - config
            - controllers
            - models
            - templates
            - __init__.py
        - server.py

- create user table on mysql workbench
- setup mysql configuration
- Set up User Model
- Create login and registration forms on index.html
- validate data for User model
- use bcrypt to encrypt passwords before they are added to the database
- use bcrypt to compare against

### Bcrypt

- used to encrypt our passwords so they are more secure in our database

### User Model

    - first_name
    - last_name
    - email
    - password
    - created_at
    - updated_at

    create method
    get_by_id
    get_by_email



### Controller

- render index.html
- register
    - this is where we will encrypt our password
- login
    - this is where we will confirm that a user exists in the database
    - well compare the encrypted password with bcrypt
- logout



### Flash

- what are flash messages?
- displaying flash messages
- filtering flash messages for forms on the same page 
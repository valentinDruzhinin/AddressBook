# AddressBook
Address Book CRUD application utilizing Django and Python.

## Prerequisites

- python3.8

## Installation
- Setup virtualenv - `python3 -m venv env`
- Source virtualenv - `source env/bin/activate`
- Install dependencies - `pip install -r requirements.txt`

## Start app
- navigate to the addressbook dir - `cd addressbook`
- run app - `python manage.py runserver`

## Admin panel
- admin creds - login:`admin`, pass:`admin`

If you would like to add a new user and then work with his addresses firstly create the user in admin panel.
 - Login as admin here: `http://127.0.0.1:8000/admin`
 - Choose `Users` and then create a new user with the password.

 ## Work with the address records
 - Login to the swagger - `http://127.0.0.1:8000`, on the right top login as newly created user.
 - Click on `http://127.0.0.1:8000/address/` link to manage address records.
 - Now you can post new records/ update and delete an existing. To delete and update - add address record id to the url and refresh.

 ## Test creds
 Test users - `login:testUser password:P@ssw0rd123`, `login:admin password:admin`

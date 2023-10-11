# To Doo

## To Doo API Documentation

To Doo is a backend for a web application that provides various API endpoints for managing agendas and user accounts. This documentation will guide you through the available endpoints and their functionalities.

## Table of Contents
- [Installation](#installation)
- [Account Endpoints](#account-endpoints)
- [Agenda Endpoints](#agenda-endpoints)
- [Deployment](#deployment)

## Installation

To set up To Doo, follow these steps:

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Edit the `.example.env` file with the appropriate values for the MySQL database configuration and the secret key.
3. Rename the `.example.env` file to `.env`.
4. Run the `db_setup.py` script to initialize the database.
5. Finally, run `pip install -r requirements.txt` once again.

If you encounter any issues during the installation process, please refer to the project's documentation or seek further assistance.

Run the server locally by running the following command

```jsx
	$ python3 manage.py runserver
```

or if you went to deploy the application on cloud instance view the Deployment Section

## Account Endpoints

**POST /accounts/api/login**

This endpoint is used for user authentication. It requires the user's credentials and returns a token for further API requests.

- **POST /accounts/api/register**
    
    Use this endpoint to create a new user account. Provide the necessary details for registration.
    
- **POST /accounts/api/logout**
    
    This endpoint allows users to log out and invalidate their authentication token.
    

## Agenda Endpoints

- **GET /agenda/agendaList**
    
    After logging in and obtaining the authentication token, you can use this endpoint to view the list of agendas.
    It supports filtering, searching, sorting, and pagination.
    
    - **Filtering**
        
        You can filter tasks based on the status query parameter for example calling:
        
        ```jsx
        agenda/agendaList/?status=Pending
        ```
        
        returns
        
    
    ```jsx
    {
            "id": 1,
            "user": "test_user",
            "title": "Do homework",
            "description": "Calculus",
            "status": "Pending",
            "due_date": "2023-10-10",
            "updated": "2023-10-11T10:03:07.520748Z",
            "created": "2023-10-11T10:03:07.520748Z"
        }
    ```
    
    - **Sorting**
        
        You can sort tasks based on the sort_by query parameter for example running
        
        ```jsx
        agenda/agendaList/?sort_by=due_date
        
        ```
        
    - **Searching**
        
        You can search for tasks based on the search query parameter 
        
        ```jsx
        /agenda/agendaList/?search=important
        ```
        
    - **Pagination**
        
        Pagination is implemented using the page and page_size query parameters  It defaults to page 1 with a page size of 10.
        
        ```jsx
        /agenda/agendaList/?page=2&page_size=20
        
        ```
        

- **POST /agenda/create**
    
    Create a new agenda by sending a POST request to this endpoint. The request body should be in JSON format, including the title, description, status, and due date of the agenda.
    
    Example:
    
    ```json
    {
        "title": "Complete Homework",
        "description": "English",
        "status": "Completed",
        "due_date": "2023-10-10"
    }
    
    ```
    
- **GET /agenda/view_agenda/<int:agendaID>**
    
    Retrieve the details of a specific agenda by its agendaID. Use a GET request to this endpoint.
    
- **POST /agenda/view_agenda/<int:agendaID>**
    
    Update the details of a specific agenda by its agendaID. Send a POST request to this endpoint with the updated information in the request body.
    
- **DELETE /agenda/view_agenda/<int:agendaID>**
    
    Delete a specific agenda by its agendaID. Use a DELETE request to this endpoint.
    

## Deployment

Django is a **web framework**, not a web server, and its maintainers want to make that distinction clear. In this section, you’ll replace Django’s `runserver` command with [Gunicorn](https://gunicorn.org/). Gunicorn is first and foremost a Python WSGI app server, and a battle-tested one at that:

- It’s fast, optimized, and designed for production.
- It gives you more fine-grained control over the application server itself.
- It has more complete and configurable logging.
- It’s [well-tested](https://github.com/benoitc/gunicorn/tree/master/tests), specifically for its functionality as an application server.

You can install Gunicorn through `[pip](https://realpython.com/what-is-pip/)` into your virtual environment:

```jsx
$ pwd
#/home/ubuntu
```

```jsx
$ source env/bin/activate
```

```jsx
$ python -m pip install 'gunicorn==20.1.*'
```

Next, you need to do some level of configuration. The cool thing about a [Gunicorn config file](https://docs.gunicorn.org/en/latest/configure.html)
 is that it just needs to be valid Python code, with variable names 
corresponding to arguments. You can store multiple Gunicorn 
configuration files within a project subdirectory:

```jsx
$ cd ~/to-doo
```

```jsx
$ mkdir -pv config/gunicorn/
#mkdir: created directory 'config'
#mkdir: created directory 'config/gunicorn/
```

Next, open a development configuration file, `config/gunicorn/dev.py`, and add the following:

```jsx
"""Gunicorn *development* config file"""

# Django WSGI application path in pattern MODULE_NAME:VARIABLE_NAME
wsgi_app = "todoo.wsgi:application"
# The granularity of Error log outputs
loglevel = "debug"
# The number of worker processes for handling requests
workers = 2
# The socket to bind
bind = "0.0.0.0:8000"
# Restart workers when code changes (development only!)
reload = True
# Write access and error info to /var/log
accesslog = errorlog = "/var/log/gunicorn/dev.log"
# Redirect stdout/stderr to log file
capture_output = True
# PID file so you can easily fetch process ID
pidfile = "/var/run/gunicorn/dev.pid"
# Daemonize the Gunicorn process (detach & enter background)
daemon = True
```

Next, make sure that log and PID directories exist for the values set in the Gunicorn configuration file above:

```jsx
$ sudo mkdir -pv /var/{log,run}/gunicorn/
#mkdir: created directory '/var/log/gunicorn/'
#mkdir: created directory '/var/run/gunicorn/'
$ sudo chown -cR ubuntu:ubuntu /var/{log,run}/gunicorn/
#changed ownership of '/var/log/gunicorn/' from root:root to ubuntu:ubuntu
#changed ownership of '/var/run/gunicorn/' from root:root to ubuntu:ubuntu
```

With these commands, you’ve ensured that the necessary PID and log 
directories exist for Gunicorn and that they are writable by the `ubuntu` user.

With that out of the way, you can start Gunicorn using the `-c` flag to point to a configuration file from your project root:

```jsx
$ pwd
/home/ubuntu/to-doo
$ source .DJANGO_SECRET_KEY
$ gunicorn -c config/gunicorn/dev.py

```

You can access application after deployment 

```jsx
http://<your-public-ip-address>:8000/
```

This runs `gunicorn` in the background with the development configuration file `dev.py` that you specified above. Just as before, you can now monitor the output file to see the output logged by Gunicorn:

```jsx
$ tail -f /var/log/gunicorn/dev.log
```
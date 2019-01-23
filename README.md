# FEATURE REQUEST APPLICATION

A "feature request" is a request for a new feature that will be added onto an existing piece of software. Assume that the user is an employee at IWS who would be entering this information after having some correspondence with the client that is requesting the feature. 

## PROJECT FEATURES
1. Users can create an account, log in and logout.
2. Users can add new features from their clients.
3. Users can view all the features available. 
4. Features, of a particular client, are reasigned their priorities based on the priority of the newly added one.
5. Users can edit the features that have already been added. 

## TECH STACK

1. OS: Ubuntu
2. Server Side Scripting: Python 3.6+
3. Server Framework: Flask
4. ORM: Sql-Alchemy
5. JavaScript: JQuery

## DEVELOPMENT APPROACH
I used the MVC pattern of programming whose flow is outlined below. 

1. The user makes a request along a route, let’s say /index.
2. The controller receives this request and gives a specific set of orders that are related to that route. These instructions could either be for the view to update or serve a certain page, or for the model to perform specific logic. If this request has some logic associated with it, then the model carries out the logic, pulls from a database and sends back a consistent response based on the controller’s instructions. 
3. The controller then passes this data to the view to update the user interface.

## DEPLOYMENT STEPS

Used gcloud to deploy the project. Below are the steps taken. 


1. Create a google VM instance that runs Ubuntu 18.04 LTS
2. Update the local apt package index: `sudo apt-get update`

3. Install nginx, postgres, pip and additional libraries: 

`sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx`
`sudo apt-get install build-essential libssl-dev libffi-dev python-dev`

4. Install apache: `sudo apt install apache2`

5. Install and configure git
6. Generate ssh keys and add public key to github

7. Login into Postgres: `sudo -u postgres psql`

8. Create database called featureapp: `CREATE DATABASE featureapp;`

9. Create user for the database:`CREATE USER yourusername WITH PASSWORD 'yourpassword';` and then: `GRANT ALL PRIVILEGES ON DATABASE featureapp TO yourusername;`

10. Git clone: git clone https://github.com/sharonmalio/feature-request-app.git and change in to the project directory

11. Install python VENV from the terminal sudo apt-get install python3-venv

12. Delete the virtual env in the project folder. (look for a folder called featurequestenv within the root directory of the project): sudo rm -R featurequestenv

13. Create another venv called featurequestenv or a name of your choice. python3 -m venv featurequestenv

14. cd into the virtual environment: `cd featurequestenv`

15. Activate the virtual environment:`source featurequestenv/bin/activate`

16. Install dependencies (contained in a file called requirements.txt in the root directory of the project): `pip install -r requirements.txt`

17. Initialize the db `python manage.py db init` migrate the db: `python manage.py db migrate` and then run: `python manage.py db upgrade` to apply the upgrades

18. Create Gunicorn systemd service file: `sudo nano /etc/systemd/system/gunicorn.service`

19. Add the following to the file

```
[Unit]
Description=gunicorn daemon
After=network.target

[Unit]
Description=gunicorn daemon
After=network.target

[Service]
User=replace-user-here
Group=www-data
WorkingDirectory=/home/replace-user-here/myproject
ExecStart=/home/replace-user-here/your-project-name/your-env/bin/gunicorn --access-logfile - --workers 3 --bind unix:/home/replace-user-here/your-project-name/your-project-name.sock wsgi:app

[Install]
WantedBy=multi-user.target

```

20. Start and enable Gunicorn: `sudo systemctl start gunicorn` and run: `sudo systemctl enable gunicorn`

21. Configure Nginx: `sudo nano /etc/nginx/sites-available/project-name`

22. Add to the file

```
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/replace-user-here/project-name;
    }


    location / {
        include proxy_params;
        proxy_pass http://unix:/home/replace-user-here/project-name/project-name.sock;
    }
}
```

23. Enable file: `sudo ln -s /etc/nginx/sites-available/project-name /etc/nginx/sites-enabled`

24. Restart Nginx: `sudo systemctl restart nginx`

## PRERIQUISITES
1. **PYTHON**: Install python. To check whether you have python installed, run the command: `python3`
2. **PostgreSQL**:Install PostgreSQL :(https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04)
3. **PIP:** Install pip: `sudo apt install python3-pip` Verify the installation:`pip3 --version`

## RUNNING THE APPLICATION

### DEPLOYED APPLICATION

Gcloud public cloud deployment method used.
Follow this url to access the application in your browser: (http://35.240.3.36) 

### ON LOCAL ENVIRONMENT

#### WITHOUT DOCKER 

1. Git clone: `git clone https://github.com/sharonmalio/feature-request-app.git` and change in to the project directory
2. Install python VENV from the terminal
`sudo apt-get install python3-venv`
3. Delete the virtual env in the project folder. (look for a folder called featurequestenv within the root directory of the project): `sudo rm -R featurequestenv`
4. Create another venv called featurequestenv or a name of your choice.
`python3 -m venv featurequestenv`
5. cd into the virtual environment: `cd featurequestenv`
6. Activate the virtual environment:`source featurequestenv/bin/activate `
7. Install dependencies (contained in a file called requirements.txt in the root directory of the project):
`pip install -r requirements.txt`
8. Login into PostgreSQL in the terminal.
9. Create a database called featureapp: `CREATE DATABASE featureapp;Exit;`
10. Initialize the db `python manage.py db init` migrate the db: `python manage.py db migrate`and then run: `python manage.py db upgrade` to apply the upgrades
10. Start the application: `flask run -p 5000` or using gunicorn `gunicorn --bind 0.0.0.0:8000 wsgi:app`

11. Open your web browser and navigate to the address:(http://127.0.0.1:5000) or gunicorn: (http://0.0.0.0:8000)

#### WITH DOCKER
1. Install docker in your machine:
(https://docs.docker.com/install/linux/docker-ce/ubuntu/)

2. To verify that docker is up and running use the command below, you should get a hello from docker message
`sudo docker container run hello-world `

3. Install docker-compose:
`sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose` If you have issues with curl you could use pip:`pip install -U docker-compose`

4. Apply executable permissions to the binary:`sudo chmod +x /usr/local/bin/docker-compose`

5. You can also create a symbolic link to /usr/bin:`sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose`

6. Test the installation.`docker-compose --version`

7. Change the directory to the project folder: `cd feature-request-app` activate the virtual env: `source featurequestenv/bin/activate` build the docker image: `docker-compose build`

8. launch the application:`docker-compose up` 

9. Navigate to the address:(http://0.0.0.0:5000)
 
## SCREENSHOTS

### Register

I added register to ease the site interractio. Otherwise the IWS admin should be the one adding her employees to the system
1. In the navigation bar click on login
2. Below the login page there is a link that says "Click to Register"
3. Follow the link and fill the information as required. 
4. click on the register button when done. 
Below is a an image that shows the view of the register page.

![registration](https://user-images.githubusercontent.com/11241491/51083208-24cba500-1727-11e9-8139-0c772beda642.png)

### Login

This assumes that you already exist in the application and you got the login credentials.
1. In the navigation bar click on login.
2. Fill in the information as required. 
3. Click on the sign in button once done.

Below is a screenshot of the login view

![login](https://user-images.githubusercontent.com/11241491/51083206-1f6e5a80-1727-11e9-9b8a-545e5a6e55ea.png)

### Add New Feature

This step requires that you are logged in user. 
1. In the navigation bar click on New Feature. 
2. in the form presented fill in the details as required. 
3. Click on the submit button once done. 
4. A successful message will show. 


![add_feature](https://user-images.githubusercontent.com/11241491/51083204-1087a800-1727-11e9-81ff-fc898948c5dd.png)

### View all 

1. Click on the All Features in the navigation bar.
2. The features available in the database will show here.

Below is a screenshot of the view.

![view_features](https://user-images.githubusercontent.com/11241491/51083211-25fcd200-1727-11e9-8a61-3615fe0610ed.png)













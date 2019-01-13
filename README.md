# FEATURE REQUEST APPLICATION

A "feature request" is a request for a new feature that will be added onto an existing piece of software. Assume that the user is an employee at IWS who would be entering this information after having some correspondence with the client that is requesting the feature. 

## PROJECT FEATURES
1. Users can create an account, log in and logout.
2. Users can add new features from their clients.
3. Users can view all the features available. 
4. Features, of a particular client, are reasigned their priorities based on the priority of the newly added one.

## TECH STACK

1. OS: Ubuntu
2. Server Side Scripting: Python 3.6+
3. Server Framework: Flask
4. ORM: Sql-Alchemy
5. JavaScript: JQuery

## PRERIQUISITES
1. **PYTHON**: Install python. To check whether you have python installed, run the command: `python3`
2. **MySQL SERVER**:Install MySQL:`sudo apt-get install mysql-server mysql-client -y`configure security configurations for our MySQL server:`sudo mysql_secure_installation`
3. **PIP:** Install pip: `sudo apt install python3-pip` Verify the installation:`pip3 --version`

## RUNNING THE APPLICATION

### WITHOUT DOCKER 
1. Git clone: `git clone https://github.com/sharonmalio/feature-request-app.git`
2. Install python VENV from the terminal
`sudo apt-get install python3-venv`
3. Delete the virtual env in the project folder. (look for a folder called featurequestenv within the root directory of the project): `sudo rm -R featurequestenv`
4. Create another venv called featurequestenv or whatever name you choose to use.
`python3 -m venv featurequestenv`
5. Cd into the virtual environment: `cd featurequestenv`
6. Activate the virtual environment:`source featurequestenv/bin/activate `
7. Install dependencies (contained in a file called requirements.txt in the root directory of the project):
`pip install -r requirements.txt`
8. log in to mysql:`mysql -u root -p`;
9. Create a database called featureapp: `CREATE DATABASE featureapp;Exit;`
10. Start python in the terminal:`python3`
11. Import models in the models.py:`from featurequest import db, User, Feature, Client` then create tables:`db.create_all()` commit the tables and the onfigurations:`db.session.commit()` then exit python:`exit()`
12. Start the application: `flask run -p 5000`

13. Open your web browser and navigate to theaddress:(http://127.0.0.1:5000)


### WITH DOCKER
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

![Alt text](/Register.jpg?raw=true "Optional Title")

### Login

![Alt text](/login.jpg?raw=true "Optional Title")

### Add New Feature

![Alt text](/add_feature.jpg?raw=true "Optional Title")

### View all Features

![Alt text](/view_features.jpg?raw=true "Optional Title")








WITHOUT USING DOCKER

 1.If you do not have Python installed on your computer install it before continuing. 
To check whether you have python installed, run the command: python3
If it is installed it will bring its version and and a python shell.  

2. Ensure that you have MySQL installed in your machine. MySQL is the database that we shall use to connect our Flask app to a database. You can use this command to install: sudo apt-get install mysql-server mysql-client -y
configure a few security configurations for our MySQL server by running the command below:
sudo mysql_secure_installation
The prompt  that informs us that we need to set the root password for MySQL you should press yes on it and  Enter a good password and press Enter on your Keyboard verify the password. Go ahead and remove anonymous users.  Follow through the rest of the steps as required and choose yes on reload the privilege table step.
Finally mysql_secure_installation is complete and we can proceed now


3. Install pip by running the commands  below:  Pip is a package management system that simplifies installation and management of software packages written in Python 
sudo apt install python3-pip

  And verify the installation through this command
  pip3 --version

4. Now it's time to have the Project. Git clone the it  so as to have it locally in your machine by running the command below
git clone https://github.com/sharonmalio/feature-request-app.git
5. Launch VSCode and open your "feature-request-app" project folder, I used VSCode for the project, however you can use any source code editor of your choice that supports python language. 
6. Select the Terminal tab from the panel on the bottom of VSCode and do the following
Install python VENV
sudo apt-get install python3-venv
Delete the virtual env in the project folder. (look for a folder called featurequestenv ithin the root directory)
sudo rm -R featurequestenv
Create another venv called featurequestenv or whatever name you choose to use.
python3 -m venv featurequestenv
Cd into the virtual environment
cd featurequestenv
Activate the virtual environment by running the command below
source featurequestenv/bin/activate 
7. Installing the dependencies is the fourth  thing. We need some third party libraries for Python. These are all contained in a file called requirements.txt in the root directory of the project you cloned above(you can open up the project and find  the file). Run the commands below to install the dependencies.
pip install -r requirements.txt 
8. Now to launch the application rather to start our application enter the following into the terminal
flask run -p 5000  you should receive an error free response. 
9. Open your web browser and navigate enter the following address into the address field to view the Flask application:
http://127.0.0.1:5000
If you try logging in at this level, the application will throw an error that there is no database named featureapp
This is because you do not have the database created, (This is the step we will need mysql server installed. )
10.Now log in to mysql using the command below: This launches mysql 
mysql -u root -p;
11.Create a database called featureapp and Exit the shell using the command below
CREATE DATABASE featureapp;
Exit;
12. Now we can connect our application to our SQL database, to ensure that we post and retrieve data. Start python in the terminal by entering the following into the terminal and pressing the Enter key on your keyboard:
python3
10. Enter the following into the terminal to import the already available models in the models.py file within the project folder under the app directory. 
from featurequest import db, User, Feature, Client
11. Next, enter the following into the terminal to create our table and its configuration:
db.create_all()
12. The output of the previous command should show our table configurations
13. We must now commit our table and configuration to the feature database by entering the following into the terminal and pressing Enter on your keyboard:
db.session.commit()
14. We are now finished using the Python command line interface and can close it by entering the following into the terminal and pressing Enter on your keyboard:
exit()
15. Now start our application again by entering the following into the terminal
flask run -p 5000  
16. Open your web browser and navigate to the following address to view the Flask application:
http://127.0.0.1:5000
17. Start by creating a new user. That should work!!!

USING  DOCKER
1.Install docker in your machine by following the steps in the link below(For those that do not have docker)
https://docs.docker.com/install/linux/docker-ce/ubuntu/

To verify that docker is up and running use the command below, you should get a hello from docker message
sudo docker container run hello-world 

2. Install docker-compose by using the command below
sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose

If you have issues with curl you could use the command below with pip
pip install -U docker-compose

3. Apply executable permissions to the binary:
sudo chmod +x /usr/local/bin/docker-compose

4. You can also create a symbolic link to /usr/bin or any other directory in your path.
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose

5. Test the installation.
docker-compose --version

6. Using the Dockerfile in the project directory we are going to build it.. Change the directory to the project folder and activate the virtual env then use the command below to build the project image.
docker-compose build

7.Then run the following command to actually launch the application through docker. By default, flask uses port 5000
docker-compose up 

16. Open your web browser and navigate to the following address to view the Flask application:
http://0.0.0.0:5000
 











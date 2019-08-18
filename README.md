# Iowa Homes

This application was built to predict house prices of the popular Ames Housing Dataset. I am able to use a supervised Linear Regression
Model to achieve an 88~% accuracy using a training a testing split which had gone through various cleaning techniques to provide as much
valuable information as possible. A user is able to access the application through a django front-end application which will give them the
option to select the feauters of the house they want to recieve a prediction on.

I have also extended this to allow users to sign up and log in. For future work I would like to show the user a list of the predictions they 
have made and allow them to edit features on them.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

For this project to run you first need to install

```
sudo apt-get install python3
sudo apt-get install python3-pip
sudo apt-get install python3-venv
sudo apt install postgresql-11

```

### Installing

A step by step series of examples that tell you how to get a development env running

First clone the repository
```
git clone https://github.com/THelsby/IowaHomes.git
cd iowaHomes/
```

Create a virtual environment
```
python3 -m venv venv
. ./venv/bin/activate
```

Install the dependency of the project
```
pip3 install -r requirements.txt
```
Secondly open up postgresql and use the default user with password admin and a database named IowaHomes
```
sudo -u postgres psql
ALTER USER postgres PASSWORD 'admin';
CREATE DATABASE "IowaHomes";
```


Finally use djangos built in functions to auto-generate the database and run the server.
```
python manage.py runserver
```

Head to the address
```
http://127.0.0.1:8000/prediction/
```
![alt text](https://i.imgur.com/yaLqNfM.png)

## Built With

* [Django](https://www.djangoproject.com/)
* [Python](https://www.python.org/) 
* [Scikit-Learn](https://scikit-learn.org/stable/)
* [Postgres](https://www.postgresql.org/)

## Authors

* **Thomas Helsby** - *Initial work* - [THelsby](https://github.com/THelsby)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

# Chest X-Ray Covid-19 Detection

## Technology Stack

**Frontend:** HTML, CSS(+ Bootstrap 4)  
**Backend:** Python/Django  
**Database:** SQLite3  

And additional requirements are in [**requirements.txt**](https://github.com/jkrlr/chest-x-ray-covid-19-detection/blob/main/requirements.txt)

## Getting Started

### Setting-up the project

- Download and install Python 3.9
- Download and install Git.
- Fork the Repository.
- Clone the repository to your local machine `$ git clone https://github.com/<your-github-username>/chest-x-ray-covid-19-detection.git`
- Change directory to chest-x-ray-covid-19-detection `$ cd chest-x-ray-covid-19-detection`
- Install virtualenv `$ pip3 install virtualenv`
- Create a virtual environment `$ virtualenv env -p python3.9`  
- Activate the env: `$ source env/bin/activate` (for linux) `> ./env/Scripts/activate` (for Windows PowerShell)
- Install the requirements: `$ pip install -r requirements.txt`
- Make migrations `$ python manage.py makemigrations`
- Migrate the changes to the database `$ python manage.py migrate`
- Create admin `$ python manage.py createsuperuser`
- Run the server `$ python manage.py runserver`

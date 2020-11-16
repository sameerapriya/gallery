For this project python3.8, Django , Pillow has been used.

To see the working of the Repository :
STEP 1: In your CLI go to the folder you desire to save this repository. Clone the Repository with the following command.

    `git clone <url of the repository>`

STEP 2: After the clone , create a virtual environment using the command:

    `virtualenv -p python3.8 venv`

STEP 3: Activate the virtual environment

    if Windows use ,
        `venv\Scripts\activate`
    if Linux use,
        `source venv/bin/activate`

STEP 4 : Create a MYSQL DB or any db of your choice , with all the privileges of the database to the user. And add this to the settings. 
 
 `'default': {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "db_name",
        "USER": "username",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "3306",
        }
    }`

STEP 5: To install the required packages

    `pip install -r requirements.txt`

STEP 6: To register the models run the following commands.

    `python3 manage.py makemigrations`
    `python3 manage.py migrate`

STEP 7: To see the working of the project, go to the localhost:8000 homepage or Run the command

    `python3 manage.py runserver`    

Note :
    To view the album go to "album/" url.
    To view the upload option go to "upload" url.

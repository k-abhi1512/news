# For Docker #
1. Need to run the pgAdmin4 application for postgres sql port 5432
2. Just go the the asses folder path and run the "docker-compose build" comand and wait till process completes.
3. Then execute "docker-compose up" command
<!-->

# Steps for running the project in locale machine without docker #

1. Install python in your system using the link "python.org/downloads/" [version 3.9]
2. Install a virtual environment based on your OS. so that the packages are not installed in the entire machine.
3. Load the virtual environment.
4. install django on the environment using command "pip install django" [version 3.1]
5. install widget tweaks for using widgets in the form using command "pip install django-widget-tweaks"
6. install Pillow using command "pip install Pillow".
7. In the terminal or command line losd the project path "asses".
8. type the command "python manage.py runserver".
9. Install packages if asked any.
10. Load the localhost url with port 8080 mentioned in the command line or terminal after running server.
11. Install postgres connector psycopg2 using command "pip install psycopg2".
12. In settings file change database host to 'localhost' instead of 'db'.


# Requirements #

1. Django
2. Pg-admin4
3. Python
4. postgressql

# Admin/Login Credentials #
username: news
password: 123news
<--!>
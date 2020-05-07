# django-assignment
#############################################################################################
Being new to django, i could able to give a partial solution to the assignment, which was given to me. I have learned this 
django rest framework within these three days of time.

IMPLEMENTAIONS:
	1) I have used django.rest_framework to make api calls to GET/POST request
	2) I have used routers to route the urls to the specific page
	3) I have used mysql DB to store and retieve the data
	4) I have used Serialization Models to Retrieve the data in JSON format from class Models.

STEPS AND INSTALLATIONS:
  1) create a database in mysql and add it in the settings.py file
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_db',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'localhost',
        'PORT':'3306',
    }
  2) open command prompt
      1) navigate to your project folder, say: D:NewApp/
      2) D:NewApp/python manage.py makemigrations
      3) go to migrations folder, note name of the last updated file
      4) D:NewApp/python manage.py sqlmigrate <AppName> <Migrations_file_name>
      5) D:NewApp/python manage.py migrate
      6) D:NewApp/python manage.py runserver
      7) go to localhost:8080/member
      8) click on the link --> u will navigated to localhost:8000/member/users
          1) scroll down the page, you will find a form to Real name, tz, PhoneNumber as POST request
          2) after adding the member, again call the url "localhost:8000/member/users"
          3) you will find the datas, what you have entered will render in JSON format.
      
  

#################################################################################

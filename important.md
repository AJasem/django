python -m venv ./venv  
<!-- to init the ve  -->
.\venv\Scripts\Activate.ps1
<!-- to activate the ve -->
deactivate 
<!-- to deactivate the ve -->
 django-admin startproject btre .
 <!-- to start a project btre in the correct dir -->
 gitignore.io
 <!-- to git ignore for a frame work -->
 python manage.py runserver  
 <!-- to run the server -->
 python manage.py startapp pages
 <!-- to create an app -->
 after we init an app we make a urls.py file and make the view for it and then include it in the main project urls.py


 use the {% url '' %} tag to link pages 


 pip install psycopg2
 pip install psycopg2-binary
 this is for postgresql 
 then we change the databases in setting.py to postgresql and our db with host and pass


 <!-- this ins for migration  -->
 python manage.py migrate
 <!-- we have to install pillow when we use imagefield -->
 pip install Pillow
 <!-- to make migrations after making the models  -->
 python manage.py makemigrations
 then python manage.py migrate

 <!-- to create a super user  -->
  python manage.py createsuperuser
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
  <!-- to add the model to the admin area we use this -->
  from .models import Listing

admin.site.register(Listing)
<!-- for the media files we shoud add this to the main settings.py -->
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
MEDIA_URL = '/media/'
<!-- we should also add this to the main urls.py -->
+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) and import settings and static from the django.conf

<!-- to customize the admin page  -->
make a admin folder inside the template
make a html file base_site.html
extend the admin/base.html
make a block branding
for the css make a block with extrastyle
then we make admin.css file inside the main pro static css 

<!-- to customaize the admin area for listing or realtor  -->
make a class called ListingAdmin and pass it with the register
this class takes a param of admin.modelAdmin
then we can use list_
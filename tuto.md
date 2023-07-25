# Tutorial - Setup python virtual environment

A virtual environment enables an abstract separation from other python environments.
Each environment has separate python and pip instances.

## Create environment.

This command creates a new virtual environment at the 'virtual' folder.

```bash
python3 -m venv virtual
```
## Activate the virtual environment

```bash
.\virtual\Scripts\activate
```

## Save pip dependencies - libraries

Inside the virtual environment in order to save the dependencies for use on another system use this

```bash
pip freeze > .\requirements.txt
```

## Load dependencies from requirements.txt

```bash
pip install $(cat .\requirements.txt)
```


##

# Django

## Start

To create a project use this

```bash
python -m django startproject insertName
```

## Start the server

To start the server enter the root of the server/folder with the cd command, next use this

```bash
python .\manage.py runserver
```

The server will be at your localhost:8000 

## Template

To create a template you need a folder to save them, create a folder called templates, next go to the settings.py and import os, next in the TEMPLATES part change the DIR:[] to DIR:[os.path.join(BASE_DIR,'insertName/templates')]

## Apps

Apps in Django are Web applications that do stuff, like a Weblog system or a database of public records. To create one go to the directory where you want it to be created (in cmd or your terminal), then write:

```bash
python .\manage.py startapp insertName
```

The name of the app can be whatever you want.

## Views

Now we want to see if its working, in the templates folder create a new html file, then in the app file go to views.py and write:

```bash
def home(request):
    return render(request, 'insertName.html') ~
```

After that go to the urls.py, first import views next create a path for the view home, you can do that with this:

```bash
urlpatterns = [
    path('', views.home, name ='insertName')
]
```

the ' ' being empty means in the browser in the url it would be localhost:8000, if you had it like this:

```bash
urlpatterns = [
    path('home', views.home, name ='insertName')
]
```

then it would be localhost:8000/home


Next run the server and go to your localhost:8000 to see it.

# Static Files

## How to save them

Static files are a bit tricky to use but its a one time thing, set it up and you won't have to do it again, for this project atleast.

First you are going to need a folder for the static files, create a static folder in your project directory name "static".

Next go to settings.py and go to:

```bash
    STATIC_URL = "/static/"
```
Now we need to tell Django where the static files are, for that write:

```bash
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'projectName/static')
    ]
```
Django likes to have a place to save his static files himself, so lets creat a root for files where Django will save them:

```bash
    STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
```

The name can be assets, static, whatever you want, just keep it easy to read and logical.

When you have your static files in the static folder you created, we need to tell Django to grab them and store them in his own folder, for that, in the terminal, use:

```bash
    python .\manage.py collectstatic
```

Now we have a folder that has all the static files we are using.To call it now we need to inform the file we are working on about some specific file being a static file, for that we are going to use an example of an html file needing a css file for formating.
We have a html file and a css file, the html file will be in the templates and the css file will be in the static folder. To tell the html file to use the css file we need to do:

```bash
    {% load static %}

...

<header>
    ...
    <link rel="stylesheet" href="{% static 'cssFile.css' %}">
</header>
```

With this we tell the html file to load the static folder and then we tell him that the css file IS a static file and so will be in the static folder, next we tell the name of the css file and Django will know where to get it.

## Browser

Sometimes the static files might not get updated in the browser because of the browser's cache, to fix it reload page with ctrl-F5.

# Database

## Introduction

The database being used is a relational database, that means there are relations between data and so it has some limitations. I expect you to learn about database on your own, search the web for more information.

## Django - Database

Django has his own database, but that is just for development; for Django to be able to access the database you need to let it know where to do it, you can do that in the settings.py file:

```bash
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME' : 'DatabaseName',
            'USER' : 'UserName',
            'PASSWORD' : 'UserPassword',
            'HOST' : 'DatabaseIp',
            'PORT' : 'DatabasePort' 

        }
    }
```
## Django - ORM

Now that Django is able to access the database it can help you interact with it. Django has an inbuilt API-ORM (Object Relational Mapper), this lets you insert data and/or extract. Now how you work with it is the key.

I recommend looking into Django's ORM documentation.

## Django - Insert data

A way to insert data is to create an endpoint, for that you need to create a path in the urls.py:

```bash
urlpatterns = [
    path('insertData/',views.insertClass,name='insertData')
]
```
The path will do the insertClass in the views.py. Again, look at more about this in the web, with Django you can do a big amount of different stuff.

## Django - Search

Now that you have data in your database, you can do a search in it to see specific information, for that you need to create another path and in the corresponding class in the views.py you need to have a filter set up. Search the web for specific coding, really, do it.

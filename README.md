# Project

Welcome to the OGAUC website project!

## Starting

To start working in the project please use the python virtual enviroment provided, for that make sure you are in the correct directory:
```bash
 X:\...\Projeto_estagio_OGAUC>
```
After that do:
```bash
.\virtual\Scripts\activate
```
Last, enter the django_OGAUC directory:
```bash
cd .\django_OGAUC\ 
```

## Organization

This project is organized to be easy to work on. You can see that there it is divided into 6 divisions:

```bash
-main_body
-geomagnetic_data
-meteorologic_data
-seismologic_data
-solar_data
-outreach
``` 
With this you can work on separate divisions, for an example, if you were to work on solar_data then you would only program in the solar_data folder and the main_body if necessary. This way work can be compartmentalized.

The admin user/password is: ogaucsuperuser/H1iu7#ft

## Urls

Each division has its own urls.py file, they all connect to the main_body's urls.py file, keep that in mind. When you are making paths they will be a subsection of the initial path in the main_body's urls.py file!   
Example: In solar_data, you create a path that looks for 'EXAMPLE1', the total url would be 'solarData/EXAMPLE1' since it would look for the solarData first and then look for the paths in the solar_data's urls.py file.   
  
The paths have been created in a basic level, while working on them keep them updated and polished.

## Static Files / Templates / CSS

Static files, Templates and CSS have already been setup, if you want to add a template, please add it on the templates folder, if you want to add a static file (Images/CSS/JavaScript) add it on the static folder and after that do the command:

```bash
python manage.py collectstatic
```
Each site has its own template/css (for now), if in the future you find it to be excessive and are able to cut down, please do it, for now this was made because I can't predict the future.  
All the templates use the baseTP.html/baseCSS.css as a base, this way you only need to work on the actual content of the page, without having to worry about the rest.

## CSRF Tokens

Csrf tokens area bit tricky, you need to have the html have the csrf token tag, then you need to ask for it in the program that is going to connect with Django, then send it with the POST request. Look at the done example on the "insert24h" in the meteorologic views.py.

## Graphs

Graphs are made with chart.js, its a javascript package, its recommended to look at the documentation (https://www.chartjs.org/docs/latest/).

# TO-DO

List of potential work (please keep this updated):

-Search with modular keywords   
-Create Dark Mode in the HTML with the corresponding changes to the header image and text color
-Seismology
-Outreach

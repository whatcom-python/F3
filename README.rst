********************
Project Introduction
********************

F3 is an abbreviation for Food and Farm Finder. It is a project of the 
`Whatcom Python Users Group`_ to create a Web based version of the 
Food and Farm Finder pamphlet available from `Sustainable Connections`_ as 
a `PDF`_.  The Python Web framework Django is being used. The original
inspiration for the project came from a `talk`_ given by Sean Boisen at 
LinuxFest 2010 

.. _Whatcom Python Users Group: http://whatcompython.org/
.. _Sustainable Connections: http://sustainableconnections.org/
.. _PDF: http://sustainableconnections.org/foodfarming/guidetoeatinglocal/fff-2010/wfff-listing-details/at_download/file
.. _talk: http://semanticbible.com/other/talks/2010/linuxfestnw/main.html
         

********
Setup
********

Prerequisites
=============

* Python 2.5-2.7. Versions 3.0+ not supported
* Django Current release
* Database options.
    * Sqlite. Included in the above versions of Python. Default
    * Postgres. Some assembly required. 
    * MySQL. Some assembly required

General Notes
============= 

As mentioned above the project is using Django as its Web framework. Before
starting the set up a general idea of the layout is in order. In the Django
world the root of the site is known as the project. Within the project there are
one or more applications. This repository represents the F3 project and its
associated application f3_final. 

Django uses a database(s) to store information. For this project the default
database is Sqlite. The primary reason being that it is included with Python
2.5+. The other reasons are that it is a single file and has simple 
administrative needs. MySQL and Postgres have also been used. See the F3 section
below for more information.

Django
=========
* To install Django follow the instructions here `install`_. For our purposes
  you only need to be concerned with the section titled 'Install Django'.
 
* To test that Django has been installed do::
    
    $ python
    Python 2.6.5 (r265:79063, Apr 16 2010, 13:09:56) 
    [GCC 4.4.3] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import django
    >>> 

* Proceed to the F3 section below.

.. _install: http://docs.djangoproject.com/en/1.2/intro/install/

  
F3 project
==========
* This repository is the F3 project.

* Either use Git to clone the repository to your machine or use the Downloads
  button. If you choose the Downloads option you will be presented with a
  choice of having the repository rolled up into either a \*.zip or \*.tar.gz
  file. 

* If you downloaded one of the compressed file formats, uncompress the archive
  into a suitable location. **NOTE:** The download process creates a unique
  directory name for the project. Now is good time to rename that directory to
  F3
  
* If you plan on using Sqlite as the database skip to the next step. If not,
  there is some housekeeping to be done. Using the appropriate database tool
  create a database; suggested name-f3. Also create a user with a password that
  has sufficient rights to administer the database. You will then need to make
  changes to the settings.py  file in the project root(F3/). Shown below is the
  database setting method for Django 1.2+, where you can have more than one 
  database for a project. If you are using Django version 1.2, your settings.py
  file probably still has the old style. Just comment out the DATABASE_* 
  settings and cut and paste the setting below::
      
    DATABASES ={
    'default': {
        'ENGINE': '',
        'NAME': '',
        'USER': '',
        'PASSWORD':'',
        'HOST':'',
        'PORT':''
        }
    }
    
    Where:
    ENGINE =    
    'django.db.backends.postgresql_psycopg2'
    'django.db.backends.postgresql'
    'django.db.backends.mysql'
    'django.db.backends.sqlite3'
    'django.db.backends.oracle'
    NAME = Or path to database file if using sqlite3.
    
  Fill in the appropriate settings.
  
* Change directories to the root of the project F3/. From there run::
    
    python manage.py syncdb
  
  This will populate the database with the application tables. Also when run the
  first time, it will ask to create the the Django authorization system. You 
  want to say 'yes' to this. The script will prompt you for information and then
  create the authorization tables.
  
* Load data for project. To get the initial data into the database do::
    
    python manage.py loaddata f3_final
    
  At successful completion you should see something like:: 
  
    Installed XXX object(s) from Y fixture(s)

* Run built in Web server. Django has its own Web server that is sufficient for
  development work. It should not be used in production. To start the server, 
  from the project root do::
      
      python manage.py runserver
      Validating models...

      0 errors found
      Django version 1.3 rc 1 SVN-15770, using settings 'f3.settings'
      Development server is running at http://127.0.0.1:8000/
      Quit the server with CONTROL-C.

* Verify site is working. In Web browser enter http://127.0.0.1:8000/f3/
  You should see "this is the Hello world from f3"
  
* Congratulations you are up and running.


Future Use
==========
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
=========
  * This repository is the F3 project.
  
  * Either use Git to clone the repository to your machine or use the Downloads
    button. If you choose the Downloads option you will be presented with a
    choice of having the repository rolled up into either a *.zip or *.tar.gz
    file. 
    
  * If you downloaded one of the compressed file formats, uncompress the archive
    into a suitable location. NOTE: The download process creates a unique
    directory name for the project. Now is good time to rename that directory to
    F3 or f3.
  

    
  
  



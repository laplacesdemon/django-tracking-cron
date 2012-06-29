Django Tracking Cron
====================

tracking_cron is a django app which extends the functionality of another django app called 'tracking' https://github.com/codekoala/django-tracking . tracking app allows to track visitors of the web site and clears the visitor data from the database in regular intervals. 'tracking_cron' app helps to run a crontab to save the total visitor count and page views.

This app includes a helper management command and admin interface


Installation
------------

Add 'tracking_cron' to the applictions list on the settings.py
Make sure that you create db tables via running 'python manage.py syncdb'

Usage
-----

All you have to do is to run 'python manage.py ' command. That creates a record on the db includes the total visitor and page view counts for that moment. You will most likely create a crontab (for unix like operating systems) or a scheduled task for windows.

There is a sample crontab script included in the source code.
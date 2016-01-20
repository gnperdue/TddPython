# Getting Django Set Up Using a Functional Test

## Obey the Testing Goat!

The first step is always: _write a test_.

    TddPySite$ python3 functional_tests.py
    Traceback (most recent call last):
      File "functional_tests.py", line 6, in <module>
    assert 'Django' in browser.title
    AssertionError

## Getting Django Up and Running

    TddPySite$ which django-admin.py
    /Library/Frameworks/Python.framework/Versions/3.4/bin/django-admin.py
    TddPySite$ django-admin.py startproject superlists
    TddPySite$ tree
    .
    ├── functional_tests.py
    └── superlists
        ├── manage.py
        └── superlists
            ├── __init__.py
            ├── settings.py
            ├── urls.py
            └── wsgi.py

We can run a test server:

    superlists$ python3 manage.py runserver
    Performing system checks...
    
    System check identified no issues (0 silenced).
    
    You have unapplied migrations; your app may not work properly until they are applied.
    Run 'python manage.py migrate' to apply them.
    
    January 20, 2016 - 00:03:45
    Django version 1.7, using settings 'superlists.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.

Now `python3 functional_tests.py` works.

## Starting a Git Repository

Let's work one level higher than recommended so we can keep our notes in the
repo.

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

    TddPython$ git init
    Initialized empty Git repository in /Users/gnperdue/Dropbox/Programming/Programming/Python/TestDriven/TddPython/.git/
    TddPython$ echo TddPySite/superlists/db.sqlite3 >> .gitignore
    TddPython$ git add .
    TddPython$ git status
    On branch master
    
    Initial commit
    
    Changes to be committed:
      (use "git rm --cached <file>..." to unstage)
    
    new file:   .gitignore
    new file:   TddPySite/superlists/functional_tests.py
    new file:   TddPySite/superlists/manage.py
    new file:   TddPySite/superlists/superlists/__init__.py
    new file:   TddPySite/superlists/superlists/settings.py
    new file:   TddPySite/superlists/superlists/urls.py
    new file:   TddPySite/superlists/superlists/wsgi.py
    new file:   tddpyCha01/tddpy_notes_cha01.markdown
    TddPython$ git commit -m "start tracking notes in Test Driven Development with Python by Harry Percival"
    [master (root-commit) 207e9c0] start tracking notes in Test Driven Development with Python by Harry Percival
     8 files changed, 173 insertions(+)
     create mode 100644 .gitignore
     create mode 100644 TddPySite/superlists/functional_tests.py
     create mode 100755 TddPySite/superlists/manage.py
     create mode 100644 TddPySite/superlists/superlists/__init__.py
     create mode 100644 TddPySite/superlists/superlists/settings.py
     create mode 100644 TddPySite/superlists/superlists/urls.py
     create mode 100644 TddPySite/superlists/superlists/wsgi.py
     create mode 100644 tddpyCha01/tddpy_notes_cha01.markdown


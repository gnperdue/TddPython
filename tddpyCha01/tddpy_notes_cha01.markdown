# Getting Django Set Up Using a Functional Test

https://www.obeythetestinggoat.com/book/chapter_01.html

## Obey the Testing Goat!

```
superlists$ py3goat
(py3goat) superlists$ django-admin.py startproject superlists .
(py3goat) superlists$ ll
total 8
-rwxrwxr-x  1 perdue  staff   808B Jan 26 08:53 manage.py*
drwxr-xr-x  6 perdue  staff   192B Jan 26 08:53 superlists/
(py3goat) superlists$ pwd
/Users/perdue/Dropbox/Programming/Programming/Python/TestDriven/TddPython/superlists
...
(py3goat) superlists$ python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have 13 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.

January 26, 2019 - 14:56:11
Django version 1.11.10, using settings 'superlists.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

## Starting a Git Repository

Using a slightly different repo structure, etc.

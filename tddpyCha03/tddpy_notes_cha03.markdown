# Testing a Simple Home Page with Unit Tests

It is about to get real!

## Our First Django App, and Our First Unit Test

    superlists$ pwds
    ...TddPySite/superlists/
    superlists$ ls
    db.sqlite3           functional_tests.py  manage.py*           superlists/
    superlists$ python3 manage.py startapp lists
    superlists$ tree
    .
    ├── db.sqlite3
    ├── functional_tests.py
    ├── lists
    │   ├── __init__.py
    │   ├── admin.py
    │   ├── migrations
    │   │   └── __init__.py
    │   ├── models.py
    │   ├── tests.py
    │   └── views.py
    ├── manage.py
    └── superlists
        ├── __init__.py
        ├── __pycache__
        │   ├── __init__.cpython-34.pyc
        │   ├── settings.cpython-34.pyc
        │   ├── urls.cpython-34.pyc
        │   └── wsgi.cpython-34.pyc
        ├── settings.py
        ├── urls.py
        └── wsgi.py
    
    4 directories, 17 files

## Unit Tests, and How They Differ from Functional Tests

1. we start with a _functional test_, from the user's point of view
2. once the functional test fails, we think about code to make it pass and write
unit tests
3. once we have a failing unit test, we write minimal application code to get a
passing test
4. then rerun functional tests

## Unit Testing in Django

Will our tests even run?

    superlists$ python3 manage.py test
    Creating test database for alias 'default'...
    F
    ======================================================================
    FAIL: test_bad_maths (lists.tests.SmokeTest)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
      File "/Users/gnperdue/Dropbox/Programming/Programming/Python/TestDriven/TddPython/TddPySite/superlists/lists/tests.py", line 7, in test_bad_maths
          self.assertEqual(1 + 1, 3)
    AssertionError: 2 != 3
    
    ----------------------------------------------------------------------
    Ran 1 test in 0.001s
    
    FAILED (failures=1)
    Destroying test database for alias 'default'...

## Django's MVC, URLs, and View Functions



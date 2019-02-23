# Testing a Simple Home Page with Unit Tests

https://www.obeythetestinggoat.com/book/chapter_unit_test_first_view.html

## Our First Django App, and Our First Unit Test

```
(py3goat) superlists$ pwd
/Users/perdue/Dropbox/Programming/Programming/Python/TestDriven/TddPython/superlists
(py3goat) superlists$ ll
total 32
-rw-r--r--@ 1 perdue  staff    12K Jan 26 08:56 db.sqlite3
-rwxr-xr-x@ 1 perdue  staff   808B Jan 26 17:58 manage.py*
drwxr-xr-x@ 7 perdue  staff   224B Jan 26 17:58 superlists/
(py3goat) superlists$ python manage.py startapp lists
(py3goat) superlists$ ls
db.sqlite3  lists/      manage.py*  superlists/
```

## Unit Tests, and How They Differ from Functional Tests

Functional tests test from the outside, from the perspective of the user, and
unit tests test from the inside, from the perspective of the programmer.

Workflow:

1. Start by writing a _functional test_, describing the new functionality from
the user's point of view.
2. Once we have a failing functional test, we start writing one or more
_unit tests_ to define how the code should behave. Each line of production code
should be tested by at least one of our unit tests.
3. Once we have a failing unit test, we write the _smallest_ amount of
application code we can to get the unit test to pass.
4. If this moves our functional test along, we repeat 2 and 3 as needed, and
eventually once the functional test passes, go back to 1.

So, functional tests drive development at a high level and unit tests drive
development at a low level.

## Unit Testing in Django

```
(py3goat) superlists$ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
F
======================================================================
FAIL: test_bad_maths (lists.tests.SmokeTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/perdue/Dropbox/Programming/Programming/Python/TestDriven/TddPython/superlists/lists/tests.py", line 7, in test_bad_maths
    self.assertEqual(1 + 1, 3)
AssertionError: 2 != 3

----------------------------------------------------------------------
Ran 1 test in 0.001s

FAILED (failures=1)
Destroying test database for alias 'default'...
```

## Django's MVC, URLs, and View Functions

Django's main job is to decide what to do when a user requests a URL. The
workflow goes like:

1. An HTTP request comes in for a particular URL.
2. Django uses some rules to decide which view function should deal with the
request ("resolving the URL").
3. The view function processes the request and returns an HTTP response.

## At Last! We Actually Write Some application Code!

One line at a time...

## urls.py

Django uses `urls.py` to map URLs to view functions. There is main `urls.py`
for the whole site in `superlists/urls.py`. A `url` entry starts with a regular
expression that defines which URLs it applies to, and goes on to say where it
should send requests.

## Unit Testing a View

Add a new test method...

## The Unit-Test/Code Cycle

We can start to settle into the TDD unit-test/code cycle now:

1. In the terminal, run the unit tests and see how they fail.
2. In the editor, make a minimal code change to address the current failure.

And repeat!

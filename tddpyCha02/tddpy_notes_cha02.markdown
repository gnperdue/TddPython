# Extending Our Functional Test Using the `unittest` Module

## Using a Functional Test to Scope Out a Minimum Viable App

Functional tests tend to track _user stories_.

    superlists$ setupdjango
    superlists$ ls
    db.sqlite3           functional_tests.py  manage.py*           superlists/
    superlists$ python3 functional_tests.py
    Traceback (most recent call last):
      File "functional_tests.py", line 9, in <module>
        assert 'To-Do' in browser.title
    AssertionError

## The Python Standard Library's `unittest` Module

    superlists$ python3 functional_tests.py
    F
    ======================================================================
    FAIL: test_can_start_a_list_and_retrieve_it_later (__main__.NewVisitorTest)
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File "functional_tests.py", line 17, in test_can_start_a_list_and_retrieve_it_later
    self.assertIn('To-Do', self.browser.title)
    AssertionError: 'To-Do' not found in 'Welcome to Django'
    
    ----------------------------------------------------------------------
    Ran 1 test in 4.171s
    
    FAILED (failures=1)

## Implicit waits

Implicit waits are standrd in Selenium tests. Later, we will need to be more
sophisticated about our waiting...

## Commit

Git.

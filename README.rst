BDD-style Rest API testing tool

It uses python's `requests <https://pypi.python.org/pypi/requests/>`_ for performing HTTP requests, `nose <https://pypi.python.org/pypi/nose/1.3.7>`_ for most assertions, `trafaret <https://github.com/Deepwalker/trafaret>`_ for json validation and `behave <https://pypi.python.org/pypi/behave/1.2.5>`_ for BDD style of tests.

Installation
------------
Clone `project <https://github.com/amreshQA/APITest_Python>`_

Run 
::

  pip install -r requirements.txt # install required dependencies



Running
-------

::

    # to execute all feature files (all tests)
    behave
    

    # to see printed output add --no-capture
    behave --no-capture
    



More about behave tool you can read here https://pythonhosted.org/behave/index.html



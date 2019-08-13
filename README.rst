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

Sample Run
------------

E:\python\python.exe E:/python/Lib/site-packages/behave/__main__.py --no-capture -i test1
Feature: Test CRUD methods in Sample REST API testing framework # test1.feature:1

  Background:   # test1.feature:3

  Scenario: POST post example                                           # test1.feature:6
    Given I set sample REST API "http://jsonplaceholder.typicode.com"   # __init__.py:11
    Given I Set POST posts api endpoint                                 # __init__.py:16
url :http://jsonplaceholder.typicode.com/posts
    When I Set HEADER param request content type as "application/json." # __init__.py:21
    And Set request Body                                                # __init__.py:26
    And Send POST HTTP request                                          # __init__.py:31
post response :{
  "id": 101
}
    Then I receive valid HTTP response code 201                         # __init__.py:43
Post rep code ;201
    And Response BODY "POST" is non-empty                               # __init__.py:71
request_name: POST
{'POST': '{\n  "id": 101\n}'}

  Scenario: GET posts example                                           # test1.feature:15
    Given I set sample REST API "http://jsonplaceholder.typicode.com"   # __init__.py:11
    Given I Set GET posts api endpoint "1"                              # __init__.py:50
url :http://jsonplaceholder.typicode.com/posts/1
    When I Set HEADER param request content type as "application/json." # __init__.py:21
    And Send GET HTTP request                                           # __init__.py:56
    Then I receive valid HTTP response code 200 for "GET"               # __init__.py:66
Get rep code for GET:200
    And Response BODY "GET" is non-empty                                # __init__.py:71
request_name: GET
{'POST': '{\n  "id": 101\n}', 'GET': '{\n  "userId": 1,\n  "id": 1,\n  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",\n  "body": "quia et suscipit\\nsuscipit recusandae consequuntur expedita et cum\\nreprehenderit molestiae ut ut quas totam\\nnostrum rerum est autem sunt rem eveniet architecto"\n}'}

  Scenario: UPDATE posts example                                      # test1.feature:23
    Given I set sample REST API "http://jsonplaceholder.typicode.com" # __init__.py:11
    Given I Set PUT posts api endpoint for "1"                        # __init__.py:79
url :http://jsonplaceholder.typicode.com/posts/1
    When I Set Update request Body                                    # __init__.py:84
    And Send PUT HTTP request                                         # __init__.py:88
update response :{
  "id": 1
}
    Then I receive valid HTTP response code 200 for "PUT"             # __init__.py:66
Get rep code for PUT:200
    And Response BODY "PUT" is non-empty                              # __init__.py:71
request_name: PUT
{'POST': '{\n  "id": 101\n}', 'GET': '{\n  "userId": 1,\n  "id": 1,\n  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",\n  "body": "quia et suscipit\\nsuscipit recusandae consequuntur expedita et cum\\nreprehenderit molestiae ut ut quas totam\\nnostrum rerum est autem sunt rem eveniet architecto"\n}', 'PUT': '{\n  "id": 1\n}'}

  Scenario: DELETE posts example                                      # test1.feature:30
    Given I set sample REST API "http://jsonplaceholder.typicode.com" # __init__.py:11
    Given I Set DELETE posts api endpoint for "1"                     # __init__.py:101
url :http://jsonplaceholder.typicode.com/posts/1
    When I Send DELETE HTTP request                                   # __init__.py:106
DELETE response :{}
    Then I receive valid HTTP response code 200 for "DELETE"          # __init__.py:66
Get rep code for DELETE:200

1 feature passed, 0 failed, 0 skipped
4 scenarios passed, 0 failed, 0 skipped
23 steps passed, 0 failed, 0 skipped, 0 undefined
Took 0m0.953s

Process finished with exit code 0
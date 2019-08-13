Feature: Test CRUD methods in Sample REST API testing framework

Background:
	Given I set sample REST API "http://jsonplaceholder.typicode.com"


Scenario: GET posts example
  Given I Set GET posts api endpoint "1"
  When I Set HEADER param request content type as "application/json."
  And Send GET HTTP request
  Then I receive valid HTTP response code 200 for "GET"
  And Response BODY "GET" is non-empty


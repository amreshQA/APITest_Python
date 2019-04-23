import json

import jpath
import nose
import requests
from behave import *
from nose.tools import assert_equal

use_step_matcher("parse")


@given('I set base URL to "{base_url}"')
def set_base_url(context, base_url):
    if base_url.startswith("context"):
        context.base_url = getattr(context, base_url[8:])
    else:
        context.base_url = base_url.encode('ascii')


@when('I make a {request_verb} request to "{url_path_segment}"')
def get_request(context, request_verb, url_path_segment):
    if not hasattr(context, 'verify_ssl'):
        context.verify_ssl = True

    url = context.base_url+ url_path_segment

    context.r = getattr(requests, request_verb.lower())(url, headers=context.headers, verify=context.verify_ssl)

    log_full(context.r)

    return context.r




@step('the status code should be equal to {expected_http_status_code}')
def status_code_validation(context, expected_http_status_code):
    nose.tools.assert_equal(context.r.status_code, int(expected_http_status_code))


@step('the response status code should not equal {invalid_http_status_code}')
def status_code_validation(context, invalid_http_status_code):
    nose.tools.assert_not_equal(context.r.status_code, int(invalid_http_status_code))


@step('the response status message should be equal to {expected_http_status_codes}')
def status_code_array_validation(context, expected_http_status_codes):
    expected_codes_list = [int(x) for x in expected_http_status_codes.split(',')]
    nose.tools.assert_in(context.r.status_code, expected_codes_list)


@step('the response status message should equal "{expected_http_status_message}"')
def status_message_validation(context, expected_http_status_message):
    nose.tools.assert_equal(context.r.reason, str(expected_http_status_message))


@step('the response parameter "{parameter_name}" should equal {expected_parameter_value}')
def parameter_validation(context, parameter_name, expected_parameter_value):
    data = context.r.json()

    if expected_parameter_value.startswith("context"):
        expected_parameter_value = getattr(context, expected_parameter_value[8:])
        nose.tools.assert_equal(data[parameter_name], expected_parameter_value)
    else:
        converted_value = json.loads(expected_parameter_value)
        nose.tools.assert_equal(data[parameter_name], converted_value)


@step('the body content matches {expected_json_value}')
def json_object_validation(context, json_path, expected_json_value):
    data = context.r.json()
    actual_json_value = jpath.get(json_path, data)

    if expected_json_value.startswith("context"):
        expected_json_value = getattr(context, expected_json_value[8:])
        nose.tools.assert_equal(actual_json_value, expected_json_value)

    else:
        converted_value = json.loads(expected_json_value)
        nose.tools.assert_equal(actual_json_value, converted_value)



from behave import *

@given('my scenarios and features are stored in the AssertThat plugin')
def step_impl(context):
    pass

@when('we implement some test code')
def step_impl(context):
    assert True is not False

@then('my test results will be uploaded to Jira so I can view my user story status')
def step_impl(context):
    assert False
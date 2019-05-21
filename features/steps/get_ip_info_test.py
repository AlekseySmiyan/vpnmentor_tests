from behave import *


@given(u'open page "{url}"')
def step_impl(context, url):
    context.browser.get(url)
    title = 'What Is My IP Address – 100% Accuracy Free IP Lookup Tool'
    assert context.browser.title == title


@then('view my IP address')
def step_impl(context):
    view_ip = context.browser.find_element_by_class_name('ip').text
    assert view_ip == context.my_ip


@then('view location IP address')
def step_impl(context):
    location = context.browser.find_element_by_id('dCountry').text
    assert location == 'Ukraine'


@then('input ip address "{ip_address}" in lookup field')
def step_impl(context, ip_address):
    field = context.browser.find_element_by_id('iplookup')
    field.clear()
    field.send_keys(ip_address)
    context.browser.find_element_by_id('cmdSubmit').click()
    view_ip = context.browser.find_element_by_class_name('ip').text
    assert view_ip == ip_address




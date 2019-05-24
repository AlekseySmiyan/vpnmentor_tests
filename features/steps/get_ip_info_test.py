from behave import *
from pages.ip_info_page import IpInfoPage


@given(u'open page "{url}"')
def step_impl(context, url):
    context.ip_info_page.go(url)
    assert context.ip_info_page.get_title() == context.ip_info_page.TITLE


@then('view my IP address')
def step_impl(context):
    view_ip = context.ip_info_page.get_view_ip()
    assert view_ip == context.my_ip


@then('view location IP address')
def step_impl(context):
    location = context.ip_info_page.get_view_location()
    assert location == 'Ukraine'


@then('input ip address "{ip_address}" in lookup field')
def step_impl(context, ip_address):
    context.ip_info_page.lookup_ip(ip_address)
    view_ip = context.ip_info_page.get_view_ip()
    assert view_ip == ip_address




from behave import *

@when('I type "{product_name}" in the search input box and press enter')
def step_impl(context,product_name):
    context.search_page.insert_input(product_name)

@when('I sort by "{sort_option}" descending')
def step_impl(context, sort_option):
    context.search_page.sort_by(sort_option)

@then('The sorting is done correctly')
def step_impl(context):
    context.search_page.validate_sort_results_descending()
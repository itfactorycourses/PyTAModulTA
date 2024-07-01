Automation Project Unit Testing Magento


1. Project Structure

a) Tests: 
- test_login -> contains all the tests that are covering the validation of the login module
- test_search -> contains all the tests that are covering the validation of the search module

b) Suite
Contains a grouping of the tests that were creating, offering a single point of entry
        for the test run

It is implemented through a class which inherits TestCase class from unittest library
Inside it we instantiated an object from the class TestSuite
    which was used to call the method addTests

Through this we created a list of tests that will be run through the
        HTML test runner implemented into the same class

c) base_data -> contains all the common data that will be used in multiple places   
        inside the project. Example: selectors, common methods, setup

2. Running

In order to run this test automation framework the following steps need to be followed:
a) clone the project locally: git clone https://github.com/itfactorycourses/PyTA_ModulTA
b) open the project in pycharm (with the project as root)
c) open the suite.py file and run it

The results will be found inside the folder reports.
Any report will follow the following name structure:
- report name_date_hour.html
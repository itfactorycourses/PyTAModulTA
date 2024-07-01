Feature: Feature will validate the login module of the magento application

#   un scenario este un test pe care il facem cu scopul de a valida o anumita functionalitate
#  un scenario in general contine in titlu un test condition
#    test condition = conditia care trebuie indeplinita pentru ca un test case sa fie considerat passed
#    precondition = conditia care trebuie indeplinita pentru ca un test case sa poata fi executat

#  un scenario in general este format din cativa pasi de executie
#  pasii de executie sunt mapati de urmatoarele keyword-uri:
#  - GIVEN -> reflecta contextul in care se executa test case-ul
#  - WHEN -> reflecta actiunea pe care trebuie sa o executam ca sa putem sa ajungem in punctul unde se face validarea
#  - THEN -> momentul in care evaluam daca testul este passed sau failed

#  In general putem sa avem oricati pasi de given, when si then cati avem nevoie

#  Exista in feature file si un pas mai special cu keyword-ul AND
#  Daca acest pas se va pune dupa GIVEN va avea functionalitate de GIVEN
#  Daca acest pas se va pune dupa WHEN va avea functionalitate de WHEN
#  Daca acest pas se va pune dupa THEN va avea functionalitate de THEN

#  Exemplu:
#  Given I am logged into the magento software testing application
#  And I have at least one product in the shopping cart (GIVEN I have at least one product in the shopping cart)
#  When I click on the shopping cart button
#  And I fill in all the valid data (WHEN I fill in all the valid data)
#  And I press Submit (WHEN I press Submit)
#  Then the order is created
#  And I can see the order in order history (THEN I can see the order in order history)

  Scenario: Verify that the user can log into the application with valid username and password
    Given I am on the magento software testing homepage
    When I click on the sign in link
    When I insert username "rogoduhu.abujefe@gotgel.org" and password "test1234#"
    When I click the login button
    Then I am logged into the application

#  scenario outline se foloseste atunci cand vrem sa executam acelasi set de pasi de executie, dar cu inputuri diferite
  Scenario Outline: Verify that the user cannot log into the application if no proper credentials are provided
    Given I am on the magento software testing homepage
    When I click on the sign in link
    When I insert username "<username>" and password "<password>"
    When I click the login button
    Then I receive error message: "<error_message>"
    Examples:
      | username                  | password     | error_message                                                                                             |
      |test@gmail.com             | fenrvrnbg    | The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.|
      |rogoduhu.abujefe@gotgel.org| vbhrbvrjbvrt | The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.|
      |   N/A                     | N/A          | This is a required field.                                                                                 |
      |   test                    | N/A          | Please enter a valid email address (Ex: johndoe@domain.com).                                              |




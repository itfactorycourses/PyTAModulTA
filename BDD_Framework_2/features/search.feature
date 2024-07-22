Feature: Validate product search results

  @search
Scenario: Search and sort by price in descending order
  Given I am on the magento software testing homepage
  When I type "capri" in the search input box and press enter
  And I sort by "Price" descending
  Then The sorting is done correctly
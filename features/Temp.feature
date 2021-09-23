# -- FILE: features/example.feature
Feature: Showing off behave

    @one
    Scenario: Run a simple test1
        Given user navigates to the site
        When user enters "Sachin Tendulkar" in the search box
        And user clicks on the search button
        Then user validates "Sachin RameshTendulkar" on landing page
        And user validates "Sachin Tendulkar" in header section

    @two
    Scenario: Run a simple test2
        Given user navigates to the site
        When user enters "Selenium" in the search box
        And user clicks on the search button
        Then user lands on search page

    @three
    Scenario: Run a simple test3
        Given user navigates to the site
        When user enters "Cucumber" in the search box
        And user clicks on the search button
        Then user lands on search page

    @four
    Scenario: Run a simple test4
        Given user navigates to the site
        When user enters "python" in the search box
        And user clicks on the search button
        Then user lands on search page
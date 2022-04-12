# -- FILE: features/example.feature
@all
Feature: Cricket1

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
        When user enters "Dilip Vengsarkar" in the search box
        And user clicks on the search button
        Then user validates "Dilip Balwant Vengsarkar" on landing page
        And user validates "Dilip Vengsarkar" in header section


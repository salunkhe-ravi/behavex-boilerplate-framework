# -- FILE: features/example.feature
Feature: Cricket2

    @three
    Scenario: Run a simple test3
        Given user navigates to the site
        When user enters "Sunil Gavaskar" in the search box
        And user clicks on the search button
        Then user validates "Sunil Manohar Gavaskar" on landing page
        And user validates "Sunil Gavaskar" in header section

    @four
    Scenario: Run a simple test4
        Given user navigates to the site
        When user enters "Rahul Dravid" in the search box
        And user clicks on the search button
        Then user validates "RahulSharad Dravid" on landing page
        And user validates "Rahul Dravid" in header section
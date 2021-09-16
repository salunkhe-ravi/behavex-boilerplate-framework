@web @duckduckgo
Feature: DuckDuckGo Web Browsing2
  As a web surfer,
  I want to find information online,
  So I can learn new things and get tasks done.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: Basic sachin Search
    Given the DuckDuckGo home page is displayed
    When the user searches for "sachin"
    Then results are shown for "sachin"

  Scenario: Basic tendulkar Search
    Given the DuckDuckGo home page is displayed
    When the user searches for "tendulkar"
    Then results are shown for "tendulkar"
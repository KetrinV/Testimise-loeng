Feature: Ametikool homepage

Scenario: homepage is opened
    When I open URL
    Then I check homepage is opened

Scenario: search testing
    Given I open URL
    When I search for testing
    Then testing is found

Scenario: search eriala
    Given I open URL
    When I search for eriala
    When eriala is found
    
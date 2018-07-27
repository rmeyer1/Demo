# Created by rmeyer at 7/25/18
@local
Feature: Virtru Test Exam

  Scenario: Email Validation
    Given the browser is open to GMAIL
    When the user is logged in as Test User
    Then Locate and Validate Email
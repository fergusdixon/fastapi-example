Feature: Testing Endpoints

  Scenario: Create a user, 2 addresses and link them
    Given a user's id, and 2 addresses ids
      When we we link them
      Then we see the entities are linked

Feature: Account registry
Scenario: User is able to create 2 accounts
    Given Account registry is empty
    When I create an account using name: "kurt", last name: "cobain", pesel: "89092909246"
    And I create an account using name: "tadeusz", last name: "szcześniak", pesel: "79101011234"
    Then Number of accounts in registry equals: "2"
    And Account with pesel "89092909246" exists in registry
    And Account with pesel "79101011234" exists in registry
Scenario: User is able to update surname of already created account
    Given Acoount registry is empty
    And I create an account using name: "nata", last name: "haydamaky", pesel:
    "95092909876"
    When I update "surname" of account with pesel: "95092909876" to "filatov"
    Then Account with pesel "95092909876" has "surname" equal to "filatov"

Scenario: User is able to update name of already created account
    Given Account registry is empty
    And I create an account using name: "jan", last name: "kowalski", pesel: "12345678901"
    When I update "name" of account with pesel: "12345678901" to "piotr"
    Then Account with pesel "12345678901" has "name" equal to "piotr"

Scenario: Created account has all fields correctly set
    Given Account registry is empty
    When I create an account using name: "adam", last name: "nowak", pesel: "11111111111"
    Then Account with pesel "11111111111" has "name" equal to "adam"
    And Account with pesel "11111111111" has "surname" equal to "nowak"
    And Account with pesel "11111111111" has "balance" equal to "0"

Scenario: User is able to delete created account
    Given Account registry is empty
    And I create an account using name: "parov", last name: "stelar", pesel:
    "01092909876"
    When I delete account with pesel: "01092909876"
    Then Account with pesel "01092909876" does not exist in registry
    And Number of accounts in registry equals: "0"

Scenario: User is able to perform an incoming transfer
    Given Account registry is empty
    And I create an account using name: "jan", last name: "kowalski", pesel: "12345678901"
    When I perform "incoming" transfer for account "12345678901" with amount: "500"
    Then Account with pesel "12345678901" has "balance" equal to "500"

Scenario: User is able to perform an outgoing transfer
    Given Account registry is empty
    And I create an account using name: "jan", last name: "kowalski", pesel: "12345678901"
    And I perform "incoming" transfer for account "12345678901" with amount: "1000"
    When I perform "outgoing" transfer for account "12345678901" with amount: "400"
    Then Account with pesel "12345678901" has "balance" equal to "600"
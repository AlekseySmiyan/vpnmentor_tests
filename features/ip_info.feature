Feature: IP info

  Scenario: Auto detect my IP address and location info
    Given open page "https://www.vpnmentor.com/tools/ipinfo/"
    Then view my IP address
    Then view location IP address "Ukraine"

  Scenario: Lookup IP address and location info
    Given open page "https://www.vpnmentor.com/tools/ipinfo/"
    Then input ip address "37.73.233.95" in lookup field
    Then view location IP address "Ukraine"
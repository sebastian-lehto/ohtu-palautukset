*** Settings ***
Resource  resource.robot

*** Test Cases ***
Register With Valid Username And Password
    Input  new
    Input Credentials  ville  ville123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input  new
    Input Credentials  ville  ville123
    Input  new
    Input Credentials  ville  ville456
    Output Should Contain  User with username ville already exists

Register With Too Short Username And Valid Password
    Input  new
    Input Credentials  vi  ville456
    Output Should Contain  Username is too short

Register With Enough Long But Invalid Username And Valid Password
    Input  new
    Input Credentials  vi223  ville456
    Output Should Contain  Username does not contain only letters

Register With Valid Username And Too Short Password
    Input  new
    Input Credentials  ville  vil2
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input  new
    Input Credentials  ville  villllellle
    Output Should Contain  Password must not contain only letters
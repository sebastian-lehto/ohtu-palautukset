*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  na
    Set Password  nalle123
    Set Password Confirmation  nalle123
    Submit Credentials
    Register Should Fail With Message  Username is too short

Register With Valid Username And Invalid Password
    Set Username  nalle
    Set Password  nallenalle
    Set Password Confirmation  nallenalle
    Submit Credentials
    Register Should Fail With Message  Password must not contain only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle456
    Submit Credentials
    Register Should Fail With Message  Password and password confirmation do not match

Login After Successful Registration
    Set Username  nalle
    Set Password  nalle123
    Set Password Confirmation  nalle123
    Submit Credentials

    Go To Login Page
    Set Username  nalle
    Set Password  nalle123
    Submit Login
    Login Should Succeed

Login After Failed Registration
    Set Username  na
    Set Password  nalle123
    Set Password Confirmation  nalle123
    Submit Credentials
    
    Go To Login Page
    Set Username  na
    Set Password  nalle123
    Submit Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login
    Click Button  Login

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_c}
    Input Password  password_confirmation  ${password_c}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}



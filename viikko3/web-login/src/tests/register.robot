*** Settings ***
Resource  resource.robot
Resource    login.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  salaatti
    Set Password  salde987
    Set Password Confirmation  salde987
    Submit Information
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  sa
    Set Password  salde987
    Set Password Confirmation  salde987
    Submit Information
    Register Should Fail With Message  Username has to be more than 2 characters  

Register With Valid Username And Too Short Password
    Set Username  salaatti
    Set Password  salde1
    Set Password Confirmation  salde1
    Submit Information
    Register Should Fail With Message  Password has to be more than 7 characters 

Register With Valid Username And Invalid Password
    Set Username  salaatti
    Set Password  saldesalde
    Set Password Confirmation  saldesalde
    Submit Information
    Register Should Fail With Message  Password has to have a special character

Register With Nonmatching Password And Password Confirmation
    Set Username  salaatti
    Set Password  salde987
    Set Password Confirmation  saldesalde
    Submit Information
    Register Should Fail With Message  Password has to match with password confirmation

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  saldesalde1
    Set Password Confirmation  saldesalde1
    Submit Information
    Register Should Fail With Message  This username is already taken

Login After Successful Registration
    Set Username  salaatti
    Set Password  salde987
    Set Password Confirmation  salde987
    Submit Information
    Go To Login Page
    Set Username  salaatti
    Set Password  salde987
    Submit Credentials
    Main Page Should Be Open

Login After Failed Registration
    Set Username  salaatti
    Set Password  salde987
    Set Password Confirmation  salde987
    Submit Information
    Go To Login Page
    Set Username  salaatti
    Set Password  salde9878
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Information
    Click Button  Register

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User    kalle    kalle123
    Go To Register Page
    Register Page Should Be Open

Submit Credentials
    Click Button    Login

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
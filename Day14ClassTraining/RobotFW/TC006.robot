*** Settings ***
Library    SeleniumLibrary
Library    DataDriver    file=testdata.xlsx    sheet_name=Sheet1
Test Template    Register And Login With Excel
Suite Setup    Open TutorialsNinja
Suite Teardown    Close Browser

*** Variables ***
${URL}       https://tutorialsninja.com/demo/
${BROWSER}   chrome

*** Keywords ***
Open TutorialsNinja
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window

Register And Login With Excel
    [Arguments]    ${firstname}    ${lastname}    ${email}    ${telephone}    ${password}

    Click Element    xpath=//span[text()='My Account']
    Click Element    xpath=//a[text()='Register']

    Wait Until Element Is Visible    name=firstname    15s
    Input Text    name=firstname    ${firstname}
    Input Text    name=lastname     ${lastname}
    Input Text    name=email        ${email}
    Input Text    name=telephone    ${telephone}
    Input Text    name=password     ${password}
    Input Text    name=confirm      ${password}

    Click Element    name=agree
    Click Button     xpath=//input[@value='Continue']
    Capture Page Screenshot

    # -------- LOGOUT AFTER REGISTER --------
    Logout From TutorialsNinja

    # -------- LOGIN --------
    Click Element    xpath=//span[text()='My Account']
    Click Element    xpath=//a[text()='Login']

    Wait Until Element Is Visible    name=email    10s
    Input Text    name=email       ${email}
    Input Text    name=password    ${password}
    Click Button   xpath=//input[@value='Login']
    Capture Page Screenshot

    Logout From TutorialsNinja


Logout From TutorialsNinja
    Click Element    xpath=//span[text()='My Account']
    Wait Until Element Is Visible    xpath=//a[text()='Logout']    10s
    Click Element    xpath=//a[text()='Logout']


*** Test Cases ***
Register Login Using Excel
    Log    Executed via DataDriver
*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    foodie    http://127.0.0.1:5000

*** Test Cases ***

1 Register Restaurant
    ${body}=    Create Dictionary    name=Robot Hub    category=Veg    location=Hyderabad    contact=99999
    ${res}=    POST On Session    foodie    /api/v1/restaurants    json=${body}
    Status Should Be    201    ${res}

2 Update Restaurant
    ${body}=    Create Dictionary    location=Bangalore
    ${res}=    PUT On Session    foodie    /api/v1/restaurants/1    json=${body}
    Status Should Be    200    ${res}

3 Disable Restaurant
    ${res}=    PUT On Session    foodie    /api/v1/restaurants/1/disable
    Status Should Be    200    ${res}

4 View Restaurant Profile
    ${res}=    GET On Session    foodie    /api/v1/restaurants/1
    Status Should Be    200    ${res}
*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    foodie    http://127.0.0.1:5000

*** Test Cases ***

13 User Registration
    ${body}=    Create Dictionary    name=Abhi    email=abhi@gmail.com    password=1234
    ${res}=    POST On Session    foodie    /api/v1/users/register    json=${body}
    Status Should Be    201    ${res}

14 Search Restaurants
    ${body}=    Create Dictionary    name=Search Hotel
    POST On Session    foodie    /api/v1/restaurants    json=${body}

    ${params}=    Create Dictionary    name=Search
    ${res}=    GET On Session    foodie    /api/v1/restaurants/search    params=${params}
    Status Should Be    200    ${res}
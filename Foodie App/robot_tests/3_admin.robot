*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    foodie    http://127.0.0.1:5000

*** Test Cases ***

9 Approve Restaurant
    ${body}=    Create Dictionary    name=Admin Hotel
    POST On Session    foodie    /api/v1/restaurants    json=${body}

    ${res}=    PUT On Session    foodie    /api/v1/admin/restaurants/1/approve
    Status Should Be    200    ${res}

10 Admin Disable Restaurant
    ${res}=    PUT On Session    foodie    /api/v1/admin/restaurants/1/disable
    Status Should Be    200    ${res}

11 View Feedback
    ${res}=    GET On Session    foodie    /api/v1/admin/feedback
    Status Should Be    200    ${res}

12 View Order Status
    ${res}=    GET On Session    foodie    /api/v1/admin/orders
    Status Should Be    200    ${res}
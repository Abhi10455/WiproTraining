*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    foodie    http://127.0.0.1:5000

*** Test Cases ***

15 Place Order
    ${user}=    Create Dictionary    name=OrderUser    email=order@gmail.com    password=1234
    POST On Session    foodie    /api/v1/users/register    json=${user}

    ${rest}=    Create Dictionary    name=Order Hotel
    POST On Session    foodie    /api/v1/restaurants    json=${rest}

    ${body}=    Create Dictionary    user_id=1    restaurant_id=1    dish=Pizza
    ${res}=    POST On Session    foodie    /api/v1/orders    json=${body}
    Status Should Be    201    ${res}

16 Give Rating
    ${body}=    Create Dictionary    order_id=1    rating=5    comment=Excellent Taste
    ${res}=    POST On Session    foodie    /api/v1/ratings    json=${body}
    Status Should Be    201    ${res}

17 View Orders By Restaurant
    ${res}=    GET On Session    foodie    /api/v1/restaurants/1/orders
    Status Should Be    200    ${res}

18 View Orders By User
    ${res}=    GET On Session    foodie    /api/v1/users/1/orders
    Status Should Be    200    ${res}
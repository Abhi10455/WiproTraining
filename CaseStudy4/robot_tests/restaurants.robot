*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    foodie    http://127.0.0.1:5000


*** Variables ***
${BASE}    http://127.0.0.1:5000


*** Test Cases ***

#RESTAURANT MODULE
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


#DISH MODULE
5 Add Dish
    ${body}=    Create Dictionary    name=Pizza    price=200
    ${res}=    POST On Session    foodie    /api/v1/restaurants/1/dishes    json=${body}
    Status Should Be    201    ${res}

    ${data}=    Evaluate    json.loads($res.text)    json
    Set Suite Variable    ${DISH_ID}    ${data["id"]}


6 Update Dish
    ${body}=    Create Dictionary    price=250
    ${res}=    PUT On Session    foodie    /api/v1/dishes/${DISH_ID}    json=${body}
    Status Should Be    200    ${res}


7 Enable Disable Dish
    ${body}=    Create Dictionary    enabled=${False}
    ${res}=    PUT On Session    foodie    /api/v1/dishes/${DISH_ID}/status    json=${body}
    Status Should Be    200    ${res}


8 Delete Dish
    ${res}=    DELETE On Session    foodie    /api/v1/dishes/${DISH_ID}
    Status Should Be    200    ${res}

#ADMIN MODULE
9 Approve Restaurant
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


#USER MODULE
13 User Registration
    ${body}=    Create Dictionary    name=Abhi    email=abhi@gmail.com    password=1234
    ${res}=    POST On Session    foodie    /api/v1/users/register    json=${body}
    Status Should Be    201    ${res}


14 Search Restaurants
    ${params}=    Create Dictionary    name=Robot
    ${res}=    GET On Session    foodie    /api/v1/restaurants/search    params=${params}
    Status Should Be    200    ${res}


15 Place Order
    ${body}=    Create Dictionary    user_id=1    restaurant_id=1    dish=Pizza
    ${res}=    POST On Session    foodie    /api/v1/orders    json=${body}
    Status Should Be    201    ${res}


16 Give Rating
    ${body}=    Create Dictionary    order_id=1    rating=5    comment=Excellent Taste
    ${res}=    POST On Session    foodie    /api/v1/ratings    json=${body}
    Status Should Be    201    ${res}

#ORDER MODULE
17 View Orders By Restaurant
    ${res}=    GET On Session    foodie    /api/v1/restaurants/1/orders
    Status Should Be    200    ${res}


18 View Orders By User
    ${res}=    GET On Session    foodie    /api/v1/users/1/orders
    Status Should Be    200    ${res}

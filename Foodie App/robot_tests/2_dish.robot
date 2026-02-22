*** Settings ***
Library    RequestsLibrary
Suite Setup    Create Session    foodie    http://127.0.0.1:5000


*** Test Cases ***

5 Add Dish
    ${rest}=    Create Dictionary    name=Dish Hotel    category=Veg
    ${rres}=    POST On Session    foodie    /api/v1/restaurants    json=${rest}
    Status Should Be    201    ${rres}

    ${rdata}=    Evaluate    json.loads($rres.text)    json
    ${RID}=    Set Variable    ${rdata["id"]}

    ${body}=    Create Dictionary    name=Pizza    price=200
    ${res}=    POST On Session    foodie    /api/v1/restaurants/${RID}/dishes    json=${body}
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
### Submit Product API

#### API
* Domain: 127.0.0.1:8000
* Path: /api/v1/escrow_account/products/submit/
* Method: POST

#### Request Body
1. name*: Name(title) of the product
2. description*: Description of the submitting product
3. price*: Price of the submitting product in Toman
4. imageN: You can add up to 5 images in every name you want, in File type of form-data 

Note: All starred parameters are required.

#### Headers
* Authorization: JWT user token generated via login API

#### Response
* 201: Successful product creation. Example response body:
<p>{<br>
    "success": true,<br>
    "id": "c9475d3b-ad4c-4209-b179-b253c105296e",<br>
    "data": {}<br>
}</p>
* 400: Client error, could not create product. Example response body:
<p>
{<br>
    "success": false,<br>
    "id": null,<br>
    "data": {<br>
        "price": [<br>
            "A valid number is required."<br>
        ]<br>
    }
}
</p>

### Create User API
#### API
* Domain: 127.0.0.1:8000
* Path: /api/v1/escrow_account/identity/user/create/
* Method: POST

#### Request Body
1. email*: Registering user email
2. password*: Registering user password 
2. repeat_password*: repeat password

Note: All starred parameters are required.

#### Response
* 201: Successful user registration. Example response body:
<p>{<br>
    "success": true,<br>
    "id": "c6ebfa1a-f737-44dd-a1f5-8a96e27cc23f",<br>
    "data": {}<br>
}</p>
* 400: Client input error. Example response body:
<p>
{<br>
    "success": false,<br>
    "id": null,<br>
    "data": {<br>
        "email": [<br>
            "A user with this email already exists."<br>
        ]<br>
    }
}
</p>

### Login API
Login is done via JWT access token in this project.
#### API
* Domain: 127.0.0.1:8000
* Path: /api/v1/escrow_account/jwt/create/
* Method: POST

#### Request Body
1. email*: User email
2. password*: User password 

Note: All starred parameters are required.

#### Response
* 200: Successful login. Example response body:
<p>{<br>
    "refresh": "some_refresh_token",<br>
    "access": "some_access_token"<br>
}</p>
* 401: Unauthorized. Example response body:
<p>
{<br>
    "detail": "No active account found with the given credentials"<br>
}<br>
</p>


### Create Refresh Token API

#### API
* Domain: 127.0.0.1:8000
* Path: /api/v1/escrow_account/jwt/refresh/
* Method: POST

#### Request Body
1. refresh*: Refresh token that was obtained from login API

Note: All starred parameters are required.

#### Response
* 200: Successful access token obtain. Example response body:
<p>{<br>
    "access": "some_access_token"<br>
}</p>
* 401: Invalid refresh token. Example response body:
<p>
{<br>
    "detail": "Token is invalid or expired",<br>
    "code": "token_not_valid"<br>
}
</p>


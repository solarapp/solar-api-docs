



# **Login**

A set of endpoint that allow for login of the maintainers, with the returned token it's possible to gain access to the 
POST, PATCH and DELETE endpoints

## <span class="get method">get</span> **check**

Checks if it is a valid token

`https://api.solarnews.ga/v1/check`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|Authorization|`string`|header|True|

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
"OK"
```
<span class="delete round"></span> **401: Unauthorized**

```json
"Unauthorized"
```


</details>

## <span class="get method">get</span> **verify**

Sends a 2fa authentication code to the user's discord dms

`https://api.solarnews.ga/v1/verify`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|mail|`string`|header|True|
|password|`string`|header|True|

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
"OK"
```
<span class="delete round"></span> **400: Bad Request**

```json
{
    "message": "\"mail\" is not allowed"
}
```
<span class="delete round"></span> **401: Unauthorized**

```json
{
    "message": "\"User not found\" is not allowed"
}
```


</details>

## <span class="get method">get</span> **verify**

Sends a 2fa authentication code to the user's discord dms

`https://api.solarnews.ga/v1/verify`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|mail|`string`|header|True|
|password|`string`|header|True|
|authcode|`number`|header|True|

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
    "token": "a valid api token"
}
```
<span class="delete round"></span> **400: Bad Request**

```json
{
    "message": "\"mail\" is not allowed"
}
```
<span class="delete round"></span> **401: Unauthorized**

```json
{
    "message": "\"User not found\" is not allowed"
}
```


</details>

## <span class="get method">get</span> **hash**

returns an hashed password

`https://api.solarnews.ga/v1/hash`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|password|`string`|header|True|

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
    "hash": "hashed password"
}
```


</details>

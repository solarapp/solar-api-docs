



# **Launch**

A launch objects rapresent the event that will happen, this uses an agency object to let users know who will launch the 
rocket

## <span class="get method">get</span> **List agencies**

`https://api.solarnews.ga/v1/launch`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|limit|`number`|query|False|
|offset|`number`|query|False|
|agency|`string`|query|False|

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
    "result": {
        "_id": "610acd67d0196ee0a17a841a",
        "agency": "{ agency_object }",
        "created_at": 1630221276000,
        "description": "First flight of the new Firefly Alpha small sat launcher developed by Firefly Aerospace.",
        "image": "https://www.com",
        "infographic": "",
        "last_edited": 1630221276000,
        "launch_time_utc": 1630221276000,
        "name": "Firefly Alpha",
        "summary": "First flight of the new Firefly Alpha launcher.",
        "webcast": ""
    }
}
```


</details>

## <span class="post method">post</span> **Add launch**

`https://api.solarnews.ga/v1/launch`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|Authorization|`string`|header|True|
|created_at|`string`|body|True|
|last_edited|`string`|body|True|
|name|`string`|body|True|
|launch_time_utc|`number`|body|True|
|image|`string`|body|True|
|agency|`string`|body|True|
|summary|`string`|body|True|
|description|`string`|body|True|
|webcast|`string`|body|True|
|infographic|`string`|body|True|

<details>
<summary>Response</summary>

<span class="get round"></span> **201: Created**

```json
{
    "inserted_id": "610acd67d0196ee0a17a841a"
}
```
<span class="delete round"></span> **400: Bad Request**

```json
{
    "message": "\"name\" is required"
}
```
<span class="delete round"></span> **401: Unauthorized**

```json
"Unauthorized"
```


</details>

## <span class="patch method">patch</span> **Edit launch**

`https://api.solarnews.ga/v1/launch/:id`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|id|`string`|params|True|
|Authorization|`string`|header|True|
|created_at|`string`|body|False|
|last_edited|`string`|body|False|
|name|`string`|body|False|
|launch_time_utc|`string`|body|False|
|image|`string`|body|False|
|agency|`string`|body|False|
|summary|`string`|body|False|
|description|`string`|body|False|
|webcast|`string`|body|False|
|infographic|`string`|body|False|

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
    "edited_id": "610acd67d0196ee0a17a841a"
}
```
<span class="delete round"></span> **400: Bad Request**

```json
{
    "message": "\"title\" is not allowed"
}
```
<span class="delete round"></span> **404: Not Found**

```json
{
    "message": "item not found"
}
```
<span class="delete round"></span> **401: Unauthorized**

```json
"Unauthorized"
```


</details>

## <span class="delete method">delete</span> **Delete launch**

`https://api.solarnews.ga/v1/launch/:id`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|id|`string`|params|True|
|Authorization|`string`|header|True|

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
    "deleted_id": "610acd67d0196ee0a17a841a"
}
```
<span class="delete round"></span> **404: Not Found**

```json
{
    "message": "item not found"
}
```
<span class="delete round"></span> **401: Unauthorized**

```json
"Unauthorized"
```


</details>

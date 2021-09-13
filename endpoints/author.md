



# **Author**

An author is someone how writes news and/or insights.

## <span class="get method">get</span> **List authors**

`https://api.solarnews.ga/v1/author`

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
    "result": {
        "_id": "610acd67d0196ee0a17a841a",
        "description": "Elon Musk",
        "logo": "https://www.com",
        "name": "Elon"
    }
}
```


</details>

## <span class="post method">post</span> **Add author**

`https://api.solarnews.ga/v1/author`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|Authorization|`string`|header|True|
|name|`string`|body|True|
|logo|`string`|body|True|
|description|`string`|body|True|

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

## <span class="patch method">patch</span> **Edit author**

`https://api.solarnews.ga/v1/author/:id`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|id|`string`|params|True|
|Authorization|`string`|header|True|
|name|`string`|body|False|
|logo|`string`|body|False|
|description|`string`|body|False|

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

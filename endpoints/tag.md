



# **Tag**

Tags are used to classify news and insights, they can be used to summarize the content explained in the article.

## <span class="get method">get</span> **List tags**

`https://api.solarnews.ga/v1/tag`

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
    "result": {
        "_id": "610acd67d0196ee0a17a841a",
        "color": "ff0000",
        "description": "Tag for launch news",
        "name": "launch"
    }
}
```


</details>

## <span class="post method">post</span> **Add tag**

`https://api.solarnews.ga/v1/tag`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|Authorization|`string`|header|True|
|name|`string`|body|True|
|color|`string`|body|True|
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

## <span class="patch method">patch</span> **Edit tag**

`https://api.solarnews.ga/v1/tag/:id`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|id|`string`|params|True|
|Authorization|`string`|header|True|
|name|`string`|body|False|
|color|`string`|body|False|
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

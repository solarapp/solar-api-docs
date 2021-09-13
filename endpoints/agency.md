



# **Agency**

An agency represents an organization which is involved in the development and launch of rockets. It is used to sort 
launches.

## <span class="get method">get</span> **List agencies**

`https://api.solarnews.ga/v1/agency`

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
    "result": {
        "_id": "610acd67d0196ee0a17a841a",
        "description": "an independent agency of the U.S. federal government",
        "founding_year": 1958,
        "image": "https://www.com/",
        "logo": "https://www.com/",
        "name": "NASA"
    }
}
```


</details>

## <span class="post method">post</span> **Add agency**

`https://api.solarnews.ga/v1/agency`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|Authorization|`string`|header|True|
|name|`string`|body|True|
|description|`string`|body|True|
|logo|`string`|body|True|
|founding_year|`string`|body|True|
|image|`string`|body|True|

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

## <span class="patch method">patch</span> **Edit agency**

`https://api.solarnews.ga/v1/agency/:id`

|name|type|in|required|
| :---: | :---: | :---: | :---: |
|id|`string`|params|True|
|Authorization|`string`|header|True|
|name|`string`|body|False|
|description|`string`|body|False|
|logo|`string`|body|False|
|founding_year|`string`|body|False|
|image|`string`|body|False|

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

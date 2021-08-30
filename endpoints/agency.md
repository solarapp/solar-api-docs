# **Agency**

<style>
    .method {text-transform: uppercase; padding:6px; border-radius: 10px; font-weight: 700; color: white;}
    .get  {background-color: #6bbd5b;}
    .post {background-color: #268fb2;}
    .patch {background-color: #e09d43;}
    .delete {background-color: #d96367;}
    .round {padding: 0 9px; margin-right: 5px;}
</style>

## <span class="get method">Get</span> **List agencies**

`https://api.solarnews.ga/v1/agency`

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
{
  "result": [
    {
      "_id": "610acd67d0196ee0a17a841a",
      "name": "NASA",
      "description": "an independent agency of the U.S. federal government",
      "logo": "https://www.com/",
      "founding_year": 1958,
      "image": "https://www.com/"
    }
  ]
}
```

</details>

## <span class="post method">post</span> **Add agency**

`https://api.solarnews.ga/v1/agency`

| Name          | type     | in     | description  |
| ------------- | -------- | ------ | ------------ |
| Authorization | `string` | header | Bearer Token |
| name          | `string` | body   |              |
| logo          | `string` | body   |              |
| description   | `string` | body   |              |
| founding_year | `int`    | body   |              |
| image         | `string` | body   |              |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **201: Created**

```json
{
  "inserted_id": "610acd67d0196ee0a17a841a"
}
```

<span class="delete method round"></span> **400: Bad Request**

```json
{
  "name": "ValidationError",
  "message": "Validation Failed",
  "details": [
    {
      "name": "\"name\" is required"
    }
  ]
}
```

<span class="delete method round"></span> **401: Unauthorized**

```json
Unauthorized
```

</details>

## <span class="patch method">patch</span> **Edit agency**

`https://api.solarnews.ga/v1/agency/:id`

| Name          | type     | in     | description  |
| ------------- | -------- | ------ | ------------ |
| id            | `string` | param  | agency id    |
| Authorization | `string` | header | Bearer Token |
| name          | `string` | body   | not required |
| logo          | `string` | body   | not required |
| description   | `string` | body   | not required |
| founding_year | `int`    | body   | not required |
| image         | `string` | body   | not required |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
{
  "edited_obj": {
    "_id": "610acd67d0196ee0a17a841a",
    "name": "NASA",
    "description": "an independent agency of the U.S. federal government",
    "logo": "https://www.com/",
    "founding_year": 1958,
    "image": "https://www.com/"
  }
}
```

<span class="delete method round"></span> **400: Bad Request**

```json
{
  "name": "ValidationError",
  "message": "Validation Failed",
  "details": [
    {
      "title": "\"title\" is not allowed"
    }
  ]
}
```

<span class="delete method round"></span> **404: Not Found**

```json
{
  "message": "agency not found"
}
```

<span class="delete method round"></span> **401: Unauthorized**

```json
Unauthorized
```

</details>

# **News**

<style>
    article .method {text-transform: uppercase; padding:6px; border-radius: 10px; font-weight: 700; color: white;}
    ul .method {text-transform: uppercase; padding:4px; border-radius: 8px; font-weight: 700; font-size: 11px; color: white;}
    .get  {background-color: #6bbd5b;}
    .post {background-color: #268fb2;}
    .patch {background-color: #e09d43;}
    .delete {background-color: #d96367;}
    .round {padding: 0 9px; margin-right: 5px;}
</style>

## <span class="get method">Get</span> **List News**

`https://api.solarnews.ga/v1/news`

| Name    | type     | in    | description  |
| ------- | -------- | ----- | ------------ |
| limit   | `string` | query |              |
| insight | `bool`   | query |              |
| offset  | `string` | query | not required |
| tag     | `string` | query | not required |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
{
  "result": [
    {
      "_id": "610ef0cd756e0a9ad5013416",
      "created_at": 1625485221763,
      "last_edited": 1628494652588,
      "image": "https://www.com",
      "tags": [
        {
          "_id": "610ae608613feab861302c70",
          "name": "Exploration",
          "color": "00ff00",
          "description": "Tag for exploration news"
        }
      ],
      "summary": "...",
      "description": "...",
      "insight": false
    }
  ]
}
```

<span class="delete method round"></span> **400: Bad Request**

```json
{
  "name": "ValidationError",
  "message": "Validation Failed",
  "details": [
    {
      "limi1t": "\"limi1t\" is not allowed"
    }
  ]
}
```

```json
{
  "message": "insight query is missing"
}
```

</details>

## <span class="post method">Post</span> **Add news**

`https://api.solarnews.ga/v1/news`

| Name          | type     | in     | description  |
| ------------- | -------- | ------ | ------------ |
| Authorization | `string` | header | Bearer Token |
| name          | `string` | body   |              |
| image         | `string` | body   |              |
| tags          | `list`   | body   | max len = 4  |
| summary       | `string` | body   |              |
| description   | `string` | body   |              |
| insight       | `bool`   | body   |              |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **201: Created**

```json
{
  "inserted_id": "612a99defb13e96397347c06"
}
```

<span class="delete method round"></span> **400: Bad Request**

```json
{
  "name": "ValidationError",
  "message": "Validation Failed",
  "details": [
    {
      "agency": "\"agency\" is required"
    }
  ]
}
```

<span class="delete method round"></span> **401: Unauthorized**

```json
Unauthorized
```

</details>

## <span class="patch method">Patch</span> **Edit news**

`https://api.solarnews.ga/v1/news/:id`

| Name          | type     | in     | description  |
| ------------- | -------- | ------ | ------------ |
| id            | `string` | param  | news id      |
| Authorization | `string` | header | Bearer Token |
| name          | `string` | body   |              |
| image         | `string` | body   |              |
| tags          | `list`   | body   | max len = 4  |
| summary       | `string` | body   |              |
| description   | `string` | body   |              |
| insight       | `bool`   | body   |              |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
{
  "edited_obj": {
    "_id": "610ef0cd756e0a9ad5013416",
    "created_at": 1625485221763,
    "last_edited": 1628494652588,
    "image": "https://www.com",
    "tags": [
      {
        "_id": "610ae608613feab861302c70",
        "name": "Exploration",
        "color": "00ff00",
        "description": "Tag for exploration news"
      }
    ],
    "summary": "...",
    "description": "...",
    "insight": false
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
  "message": "news not found"
}
```

<span class="delete method round"></span> **401: Unauthorized**

```json
Unauthorized
```

</details>

## <span class="delete method">Delete</span> **Delete news**

`https://api.solarnews.ga/v1/news/:id`

| Name          | type     | in     | description  |
| ------------- | -------- | ------ | ------------ |
| id            | `string` | param  | news id      |
| Authorization | `string` | header | Bearer Token |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
{
  "deleted_obj": {
    "_id": "610ef0cd756e0a9ad5013416",
    "created_at": 1625485221763,
    "last_edited": 1628494652588,
    "image": "https://www.com",
    "tags": [
      {
        "_id": "610ae608613feab861302c70",
        "name": "Exploration",
        "color": "00ff00",
        "description": "Tag for exploration news"
      }
    ],
    "summary": "...",
    "description": "...",
    "insight": false
  }
}
```

<span class="delete method round"></span> **404: Not Found**

```json
{
  "message": "news not found"
}
```

<span class="delete method round"></span> **401: Unauthorized**

```json
Unauthorized
```

</details>

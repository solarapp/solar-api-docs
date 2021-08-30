# **Launch**

<style>
    article .method {text-transform: uppercase; padding:6px; border-radius: 10px; font-weight: 700; color: white;}
    ul .method {text-transform: uppercase; padding:4px; border-radius: 8px; font-weight: 700; font-size: 11px; color: white;}
    .get  {background-color: #6bbd5b;}
    .post {background-color: #268fb2;}
    .patch {background-color: #e09d43;}
    .delete {background-color: #d96367;}
    .round {padding: 0 9px; margin-right: 5px;}
</style>

## <span class="get method">Get</span> **List launches**

`https://api.solarnews.ga/v1/launch`

| Name   | type     | in    | description  |
| ------ | -------- | ----- | ------------ |
| limit  | `string` | query |              |
| offset | `string` | query | not required |
| agency | `string` | query | not required |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
{
  "result": [
    {
      "_id": "612647c160a74d16148b51c2",
      "created_at": 1630221276000,
      "last_edited": 1630221276000,
      "name": "Firefly Alpha",
      "launch_time_utc": null,
      "image": "https://www.com",
      "agency": {agency_object},
      "summary": "First flight of the new Firefly Alpha launcher.",
      "description": "First flight of the new Firefly Alpha small sat launcher developed by Firefly Aerospace.",
      "webcast": "",
      "infographic": ""
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

</details>

## <span class="post method">Post</span> **Add launch**

`https://api.solarnews.ga/v1/launch`

| Name            | type     | in     | description  |
| --------------- | -------- | ------ | ------------ |
| Authorization   | `string` | header | Bearer Token |
| name            | `string` | body   |              |
| launch_time_utc | `int`    | body   |              |
| image           | `string` | body   |              |
| agency          | `string` | body   | agency id    |
| summary         | `string` | body   |              |
| description     | `string` | body   |              |
| target          | `string` | body   |              |
| webcast         | `string` | body   | not required |
| infographic     | `string` | body   | not required |

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

## <span class="patch method">Patch</span> **Edit launch**

`https://api.solarnews.ga/v1/launch/:id`

| Name            | type     | in     | description  |
| --------------- | -------- | ------ | ------------ |
| id              | `string` | param  | launch id    |
| Authorization   | `string` | header | Bearer Token |
| name            | `string` | body   |              |
| launch_time_utc | `int`    | body   |              |
| image           | `string` | body   |              |
| agency          | `string` | body   | agency id    |
| summary         | `string` | body   |              |
| description     | `string` | body   |              |
| target          | `string` | body   |              |
| webcast         | `string` | body   |              |
| infographic     | `string` | body   |              |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
{
  "edited_obj": {
    "_id": "612647c160a74d16148b51c2",
    "created_at": 1630221276000,
    "last_edited": 1630221276000,
    "name": "Firefly Alpha",
    "launch_time_utc": null,
    "image": "https://www.com",
    "agency": "61099de37731bd5d74f34eff",
    "summary": "First flight of the new Firefly Alpha launcher.",
    "description": "First flight of the new Firefly Alpha small sat launcher developed by Firefly Aerospace.",
    "webcast": "",
    "infographic": ""
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
  "message": "launch not found"
}
```

<span class="delete method round"></span> **401: Unauthorized**

```json
Unauthorized
```

</details>

## <span class="delete method">Delete</span> **Delete launch**

`https://api.solarnews.ga/v1/launch/:id`

| Name          | type     | in     | description  |
| ------------- | -------- | ------ | ------------ |
| id            | `string` | param  | launch id    |
| Authorization | `string` | header | Bearer Token |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
{
  "deleted_obj": {
    "_id": "612647c160a74d16148b51c2",
    "created_at": 1630221276000,
    "last_edited": 1630221276000,
    "name": "Firefly Alpha",
    "launch_time_utc": null,
    "image": "https://www.com",
    "agency": "61099de37731bd5d74f34eff",
    "summary": "First flight of the new Firefly Alpha launcher.",
    "description": "First flight of the new Firefly Alpha small sat launcher developed by Firefly Aerospace.",
    "webcast": "",
    "infographic": ""
  }
}
```

<span class="delete method round"></span> **404: Not Found**

```json
{
  "message": "launch not found"
}
```

<span class="delete method round"></span> **401: Unauthorized**

```json
Unauthorized
```

</details>

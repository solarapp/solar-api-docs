# **Launch**

## <span class="get method">Get</span> **List launches**

`https://api.solarnews.ga/v1/launch`

| Name   | type     | in    | description  |
| ------ | -------- | ----- | ------------ |
| limit  | `string` | query |              |
| offset | `string` | query | not required |
| agency | `string` | query | not required |

<details>
  <summary>Response</summary>

<span class="get round"></span> **200: OK**

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

<span class="delete round"></span> **400: Bad Request**

```json
{
	"message": "\"limi1t\" is not allowed"
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

<span class="get round"></span> **201: Created**

```json
{
	"inserted_id": "612a99defb13e96397347c06"
}
```

<span class="delete round"></span> **400: Bad Request**

```json
{
	"message": "\"agency\" is required"
}
```

<span class="delete round"></span> **401: Unauthorized**

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

<span class="get round"></span> **200: OK**

```json
{
	"edited_id": "612647c160a74d16148b51c2"
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
	"message": "launch not found"
}
```

<span class="delete round"></span> **401: Unauthorized**

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

<span class="get round"></span> **200: OK**

```json
{
	"deleted_id": "612647c160a74d16148b51c2"
}
```

<span class="delete round"></span> **404: Not Found**

```json
{
	"message": "launch not found"
}
```

<span class="delete round"></span> **401: Unauthorized**

```json
Unauthorized
```

</details>

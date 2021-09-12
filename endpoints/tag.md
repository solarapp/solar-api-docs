# **Tag**

## <span class="get method">Get</span> **List all tags**

`https://api.solarnews.ga/v1/tag`

<details>
  <summary>Response</summary>

<span class="get round"></span> **200: OK**

````json
{
  "result": [
    {
      "_id": "612b965352be8d8ccda8c87a",
      "name": "launch",
      "color": "ff0000",
      "description": "Tag for launch news"
    }
  ]
}</code></pre>

</details>

## <span class="post method">post</span> **Add tag**

`https://api.solarnews.ga/v1/tag`

| Name          | type     | in     | description  |
| ------------- | -------- | ------ | ------------ |
| Authorization | `string` | header | Bearer Token |
| name          | `string` | body   |              |
| color         | `string` | body   |              |
| description   | `string` | body   |              |

<details>
  <summary>Response</summary>

<span class="get round"></span> **201: Created**

```json
{
	"inserted_id": "612b849528ea7d0035cada2c"
}
````

<span class="delete round"></span> **400: Bad Request**

```json
{
	"message": "\"name\" is required"
}
```

<span class="delete round"></span> **401: Unauthorized**

```json
Unauthorized
```

</details>

## <span class="patch method">patch</span> **Edit tag**

`https://api.solarnews.ga/v1/agency/:id`

| Name          | type     | in     | description  |
| ------------- | -------- | ------ | ------------ |
| id            | `string` | param  | tag id       |
| Authorization | `string` | header | Bearer Token |
| name          | `string` | body   | not required |
| color         | `string` | body   | not required |
| description   | `string` | body   | not required |

<details>
  <summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
	"edited_id": "612b849528ea7d0035cada2c"
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
Unauthorized
```

</details>

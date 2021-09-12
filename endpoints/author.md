# **Author**

## <span class="get method">Get</span> **List authors**

`https://api.solarnews.ga/v1/author`

<details>
  <summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
	"result": [
		{
			"_id": "612f7903e8c0aff51deeffe6",
			"name": "Elon",
			"logo": "https://www.com",
			"description": "Elon Musk"
		}
	]
}
```

</details>

## <span class="post method">post</span> **Add author**

`https://api.solarnews.ga/v1/author`

| Name          | type     | in     | description  |
| ------------- | -------- | ------ | ------------ |
| Authorization | `string` | header | Bearer Token |
| name          | `string` | body   |              |
| logo          | `string` | body   |              |
| description   | `string` | body   |              |

<details>
  <summary>Response</summary>

<span class="get round"></span> **201: Created**

```json
{
	"inserted_id": "612f7903e8c0aff51deeffe6"
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
Unauthorized
```

</details>

## <span class="patch method">patch</span> **Edit author**

`https://api.solarnews.ga/v1/author/:id`

| Name          | type     | in     | description  |
| ------------- | -------- | ------ | ------------ |
| id            | `string` | param  | author id    |
| Authorization | `string` | header | Bearer Token |
| name          | `string` | body   | not required |
| logo          | `string` | body   | not required |
| description   | `string` | body   | not required |

<details>
  <summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
	"edited_id": "612f7903e8c0aff51deeffe6"
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
	"message": "agency not found"
}
```

<span class="delete round"></span> **401: Unauthorized**

```json
Unauthorized
```

</details>

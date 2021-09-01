# **Author**

<style>
    article .method {text-transform: uppercase; padding:6px; border-radius: 10px; font-weight: 700; color: white;}
    ul .method {text-transform: uppercase; padding:4px; border-radius: 8px; font-weight: 700; font-size: 11px; color: white;}
    .get  {background-color: #6bbd5b;}
    .post {background-color: #268fb2;}
    .patch {background-color: #e09d43;}
    .delete {background-color: #d96367;}
    .round {padding: 0 9px; margin-right: 5px;}
</style>

## <span class="get method">Get</span> **List authors**

`https://api.solarnews.ga/v1/author`

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

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

<span class="get method round"></span> **201: Created**

```json
{
	"inserted_id": "612f7903e8c0aff51deeffe6"
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

<span class="get method round"></span> **200: OK**

```json
{
	"edited_obj": {
		"_id": "612f7903e8c0aff51deeffe6",
		"name": "Elon",
		"logo": "https://www.com",
		"description": "Elon Musk"
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

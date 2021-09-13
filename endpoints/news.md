# **News**

A news objects rapresent an article writte by one of the authors and classified by some tags

## <span class="get method">get</span> **List agencies**

`https://api.solarnews.ga/v1/news`

|  name   |   type   |  in   | required |
| :-----: | :------: | :---: | :------: |
| insight |  `bool`  | query |   True   |
|  limit  | `number` | query |  False   |
| offset  | `number` | query |  False   |
|   tag   | `string` | query |  False   |

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
	"result": {
		"_id": "610ef0cd756e0a9ad5013416",
		"created_at": 1625485221763,
		"description": "...",
		"image": "https://www.com",
		"insight": false,
		"last_edited": 1628494652588,
		"summary": "...",
		"tags": ["tags object"]
	}
}
```

</details>

## <span class="post method">post</span> **Add launch**

`https://api.solarnews.ga/v1/news`

|     name      |   type   |   in   | required |
| :-----------: | :------: | :----: | :------: |
| Authorization | `string` | header |   True   |
|  created_at   | `string` |  body  |   True   |
|  last_edited  | `string` |  body  |   True   |
|     image     | `string` |  body  |   True   |
|     tags      |  `list`  |  body  |   True   |
|    summary    | `string` |  body  |   True   |
|  description  | `string` |  body  |   True   |
|    insight    |  `bool`  |  body  |   True   |

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

## <span class="patch method">patch</span> **Edit launch**

`https://api.solarnews.ga/v1/news/:id`

|     name      |   type   |   in   | required |
| :-----------: | :------: | :----: | :------: |
|      id       | `string` | params |   True   |
| Authorization | `string` | header |   True   |
|  created_at   | `string` |  body  |  False   |
|  last_edited  | `string` |  body  |  False   |
|     image     | `string` |  body  |  False   |
|     tags      | `string` |  body  |  False   |
|    summary    | `string` |  body  |  False   |
|  description  | `string` |  body  |  False   |
|    insight    | `string` |  body  |  False   |

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

## <span class="delete method">delete</span> **Delete launch**

`https://api.solarnews.ga/v1/news/:id`

|     name      |   type   |   in   | required |
| :-----------: | :------: | :----: | :------: |
|      id       | `string` | params |   True   |
| Authorization | `string` | header |   True   |

<details>
<summary>Response</summary>

<span class="get round"></span> **200: OK**

```json
{
	"deleted_id": "610acd67d0196ee0a17a841a"
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

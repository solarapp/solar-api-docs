# **Login**

<style>
    article .method {text-transform: uppercase; padding:6px; border-radius: 10px; font-weight: 700; color: white;}
    ul .method {text-transform: uppercase; padding:4px; border-radius: 8px; font-weight: 700; font-size: 11px; color: white;}
    .get  {background-color: #6bbd5b;}
    .post {background-color: #268fb2;}
    .patch {background-color: #e09d43;}
    .delete {background-color: #d96367;}
    .round {padding: 0 9px; margin-right: 5px;}
</style>

## <span class="get method">get</span> **Check**

`https://api.solarnews.ga/v1/verify`

Checks if it is a valid token

| Name  | type     | in     | description |
| ----- | -------- | ------ | ----------- |
| token | `string` | header |             |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
ok
```

<span class="delete method round"></span> **401: Unauthorized**

```json
Unauthorized
```

</details>

## <span class="get method">get</span> **Verify**

`https://api.solarnews.ga/v1/verify`

Sends a 2fa authentication code to the user's discord dms

| Name     | type     | in     | description |
| -------- | -------- | ------ | ----------- |
| mail     | `string` | header |             |
| password | `string` | header |             |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
{
	"message": "OK"
}
```

</details>

## <span class="get method">Get</span> **Login**

`https://api.solarnews.ga/v1/login`

| Name     | type     | in     | description |
| -------- | -------- | ------ | ----------- |
| mail     | `string` | header |             |
| password | `string` | header |             |
| authcode | `string` | header |             |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
{
	"token": "a valid api token"
}
```

</details>

## <span class="get method">get</span> **Hash**

`https://api.solarnews.ga/v1/hash`

| Name     | type     | in     | description |
| -------- | -------- | ------ | ----------- |
| password | `string` | header |             |

<details>
  <summary>Response</summary>

<span class="get method round"></span> **200: OK**

```json
{
	"hash": "hashed password"
}
```

</details>

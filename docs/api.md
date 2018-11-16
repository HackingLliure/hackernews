# sheet_api

Hackernews and Google Sheets integration API

## api
```python
api(self, creds_path, sheet_name)
```

The main API class.

### auth
```python
api.auth(self)
```

Authorize a session with the given credentials and sheet name.

__Returns__

`(class)`: Session.

### open
```python
api.open(self)
```

Opens the `sheet_name` google sheet.

__Returns__

`(class)`: The google sheet.

### get_pd
```python
api.get_pd(self)
```

Reads the opened sheet and stores the information in a DataFrame.

__Returns__

`(pd.DataFrame)`: The sheet data with columns `id` and `content`.

### get
```python
api.get(self, get_id)
```

Gets the post with the given id.

__Arguments__

- __get_id (id, str)__: The id form the post you are requesting.

__Returns__

`(json)`: The requested post.

__Todo__

Handle the exception for no existing ids.

### post
```python
api.post(self, data)
```

Stores a given post in the opened google sheet.

__Arguments__

- __data (json, dict)__: The post.

__Returns__

True

__Todo__

Handle the exception when the data could not be stored.


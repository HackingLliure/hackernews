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

:return: Session object.

### open
```python
api.open(self)
```

Opens the `sheet_name` google sheet.

:return: The google sheet object.

### get_pd
```python
api.get_pd(self)
```

Reads the opened sheet and stores the information in a DataFrame.

:return: A pandas DataFrame with the sheet data.

### get
```python
api.get(self, get_id)
```

Gets the post with the given id.

:param get_id: The id form the post you are requesting.
:return: The post information in JSON format.

:todo: Handle the exception for no existing ids.

### post
```python
api.post(self, data)
```

Stores a given post in the opened google sheet.

:param data: The post in dict/JSON format.
:return: True

:todo: Handle the exception when the data could not be stored.


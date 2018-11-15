# hackernews

## Google Sheets

### Requirements

- gspread: `pip install --upgrade gspread`
- oauth2client: `pip install --upgrade oauth2client` 
- An OAuth2 credential from Google Developer Console. You can get it [here](https://gspread.readthedocs.io/en/latest/oauth2.html).
- Rename the credential file to `creds.json` and put it in the main directory (won't be tracked by git).

### Basic usage

Let `creds_path` the ath to the `creds.json` file and `sheet_name` the google sheet name.
To init a `api` session just `api(creds_path, sheet_name)`.

#### `api.get_pd()`

- Takes no parameters.
- Return a pandas `DataFrame` containing the sheet.

#### `api.get(id)`

- Takes as parameter the `id` of the post.
- Returns the post JSON.

#### `api.post(data)`

- Takes as parameter a JSON/dict (the post).
- Returns `True` if was added succesfully or `False` if already exists/error.

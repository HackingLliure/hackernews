# hackernews

## Google Sheets

### Requirements

- gspread: `pip install --upgrade gspread`
- oauth2client: `pip install --upgrade oauth2client` 
- An OAuth2 credential from Google Developer Console. You can get it [here](https://gspread.readthedocs.io/en/latest/oauth2.html).
- Rename the credential file to `creds.json` and put it in the main directory (won't be tracked by git).

### Basic usage

Got to the [docs](docs/api.md).

### Docs generation

Used [pydoc-markdown](https://github.com/NiklasRosenstein/pydoc-markdown): 

```shell
pydocmd simple sheet_api++ > docs/api.md
```

# FastAPI Inventory workshow 2022

## Config and Setup tools
### Python ENV
* config python env
    `python -m venv env`
* Activate env
    `.\env\Scripts\activate`

### How to run server
`uvicorn main:app --reload`

### Libraries
* fastapi `pip install fastapi`
* uvicorn `pip install "uvicorn[standard]"`
* sqlalchemy `pip install sqlalchemy`
* decouple `pip install python-decouple`
* psycopg2 `pip install psycopg2`
* passlib `pip install passlib`
* bcrypt `pip install bcrypt`
* python-multipart `pip install python-multipart`
* python-jose `pip install python-jose`
    * [Ref](https://github.com/mpdavis/python-jose)
## Sqlalchemy
* [Docs](https://docs.sqlalchemy.org/en/14/orm/quickstart.html)

## Generate key by openssl
* cli `openssl rand -hex 32`

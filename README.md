
# Fastapi Scraper(realpython)

Scraping articles from realpython website



## Run Locally

Clone the project


Go to the project directory

```bash
  cd real-python-web-scaping
```

build and run docker

```bash
  docker-compose up --build
```



## Running Tests

To run tests, run the following command

```bash
  docker-compose run fastapi-web pytest
```


## API Reference

#### Get all items

```http
  GET /
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `title` | `string` | **not Required** |

#### scraping data from realpython

```http
  GET /update
```


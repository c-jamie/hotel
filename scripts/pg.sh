docker run --name postgres-db -e POSTGRES_PASSWORD=postgres -e POSTGRES_USER=postgres -e POSTGRES_DB=scraper -d -p 5432:5432 postgres:14-alpine

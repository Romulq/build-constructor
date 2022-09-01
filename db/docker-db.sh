docker run \
    --name genh-db \
    -p 55332:5432 \
    -e POSTGRES_PASSWORD=genhimp \
    -d postgres
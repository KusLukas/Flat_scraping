Scraping of sreality.cz with scrapy framework and saving the data into postgres database. Followingly, the scraped data are put on a simple html server on localhost:8080. 

The general structure will be improved in the future, as of now the dockerfile for scraping is next to the docker-compose file, and the dockerfile for html server is located in the subfolder "server". Also use of flask would be better in this case instead of http.server. Will be improved in the future.

To start the app simply type `docker compose up` in the flat_crawler subfolder and after initial setup, you can access the results on localhost:8080. It might be necessary to use `sudo`, docker compose sometimes fails because of denied permission, not sure why as of now. Usually works without sudo.

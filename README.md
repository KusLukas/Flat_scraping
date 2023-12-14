Scraping of sreality.cz with scrapy framework and saving the data into postgres database. Followingly, the scraped data are put on simple html server on localhost:8080. 


To start the app simple type `docker compose up` in flat_crawler subfolder and after initial setup you can acces the results on localhost:8080. It might be necesery to use `sudo`, docker compose sometimes fails because of denied permission, not sure why as of now. Usually works without sudo.

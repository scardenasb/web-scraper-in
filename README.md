# Web scraper for Linkedin's python jobs in different countries.

### Description
> A Python3 based web scraper made with [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), includes a full integration with Postgresql using [Psycopg2](https://www.psycopg.org/) and a [Heroku scheduler add-on](https://devcenter.heroku.com/articles/scheduler#:~:text=Scheduler%20is%20a%20free%20add,is%20expected%20but%20not%20guaranteed.), so every day the app is executed and sends the parsed data to the related sqlDB. It is only necessary to create env vars with the DATABASE_URL, LinkedIn USER, and LinkedIn PASSWORD. urllib will parse the url and extract authentication data.

<br></br>

### Format of the main function
> ![image](https://user-images.githubusercontent.com/84429399/178416417-d43bbd71-f13d-421d-9c10-c540553eff7e.png)

<br></br>
### PGAdmin4 output
> ![image](https://user-images.githubusercontent.com/84429399/176588599-e2f81d84-4c6c-44cf-9038-8dc520b3f99e.png)

# Web scrapper to look for Linkedin python jobs in different countries.
>
<br></br>
### Description
> A Python3 based web scrapper made with [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/doc/), includes a full integration with Postgresql using [Psycopg2](https://www.psycopg.org/) and a [Heroku scheduler add-on](https://devcenter.heroku.com/articles/scheduler#:~:text=Scheduler%20is%20a%20free%20add,is%20expected%20but%20not%20guaranteed.), so every day the app is executed and sends the parsed data to the related sqlDB. It is only necessary to create a ```database.ini``` file with this format:
```ini
[postgresql]
host=yourhost
user=yourdbuser
password=yourdbpassword
database=yourdbname
port=yourdbport
```
<br></br>

### Format of the main function
> ![image](https://user-images.githubusercontent.com/84429399/176589350-2aa6e3eb-7865-4883-a9c5-bd0f5d09e5b6.png)

<br></br>
### PGAdmin4
> ![image](https://user-images.githubusercontent.com/84429399/176588599-e2f81d84-4c6c-44cf-9038-8dc520b3f99e.png)

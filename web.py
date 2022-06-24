import requests
from bs4 import BeautifulSoup
import csv
from datetime import date


# TODO: Make dicts and lists to deal more countries and iterate only one URL, it would be more readable.
COUNTRIES = []
COUNTRIES_GEOLOC = {''}


URL = [
        'https://www.linkedin.com/jobs/search?keywords=Python&location=Japan&geoId=101355337&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=python&location=Netherlands&geoId=102890719&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=Python&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=Python&location=South%20Korea&geoId=105149562&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=Python&location=chile&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=Python&location=United%20Kingdom&geoId=101165590&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=Python&location=Finland&geoId=100456013&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=Python&location=Sweden&geoId=105117694&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=Python&location=germany&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=Python&location=Denmark&geoId=104514075&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        ]


def scrap():
    today = date.today()
    for i in URL:
        page = requests.get(i)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(class_="results-context-header")

        python_jobs = results.find_all("h1", class_="results-context-header__context")

        for job in python_jobs:
            jobs = job.find("span", class_="results-context-header__job-count")
            country = job.find("span", class_="results-context-header__query-search")
            new_jobs = job.find("span", class_="results-context-header__new-jobs")
            print(jobs.text.strip()[:-1], country.text.strip(), new_jobs.text.strip())

            # FIXME: Csv writer is appending ^M in eof, look for a way to grep and remove it.
            with open('/home/scardenasb/workspace/web-scrapper-in/counter.csv', 'w', encoding='UTF8') as f:
                writer = csv.writer(f)

                writer.writerow(jobs) 
                writer.writerow(country) 
                writer.writerow(new_jobs)

    print('----------------------------------------------')
    print('DATE: ', today)
    print('-----')


if __name__ == "__main__":
    scrap()

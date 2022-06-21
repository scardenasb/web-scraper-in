import requests
from bs4 import BeautifulSoup
import os


URL = [
        'https://www.linkedin.com/jobs/search?keywords=Python&location=Japan&geoId=101355337&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=python&location=Netherlands&geoId=102890719&trk=homepage-jobseeker_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=Python&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        'https://www.linkedin.com/jobs/search?keywords=Python&location=South%20Korea&geoId=105149562&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0',
        ]

def scrap():
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

        # os.system('python3 web.py > counter.cvc')


if __name__ == "__main__":
    scrap()

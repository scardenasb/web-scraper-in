import requests
from requests.auth import HTTPBasicAuth
import os
from bs4 import BeautifulSoup
from datetime import date


LOCATION_NAMES = {
    "Japan": "101355337",
    "Netherlands": "102890719",
    "United%20States": "103644278",
    "South%20Korea": "105149562",
    "Chile": "104621616",
    "United%20Kingdom": "101165590",
    "Finland": "100456013",
    "Sweden": "105117694",
    "Germany": "101282230",
    "Denmark": "104514075",
    "Scotland": "100752109",
    "Estonia": "102974008",
    "Canada": "101174742",
    "Brazil": "106057199",
    "China": "102890883",
    "Taiwan": "104187078",
    "France": "105015875",
    "Spain": "105646813",
    "Portugal": "100364837",
    "Italy": "103350119",
    "Luxembourg": "104042105",
    "Switzerland": "106693272",
    "Ireland": "104738515",
    "India": "102713980",
}


URL = []
url_filler = ""

# NOTE: The query seems to only need the location name, geoId is optional and can be set to "".
for key in LOCATION_NAMES:
    url_filler = f"https://www.linkedin.com/jobs/search?keywords=Python&location={key}&geoId={LOCATION_NAMES[key]}&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    URL.append(url_filler)


def scrap():
    today = date.today()
    object = {"jobs": [], "country": [], "new_jobs": [], "date": []}
    try:
        authentication = requests.get(
            "https://www.linkedin.com/login/user,",
            auth=HTTPBasicAuth(os.environ.get("USER"), os.environ.get("PASSWORD")),
        )
        print("try:", authentication)
    except:
        pass

    for i in URL:

        page = requests.get(i)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find(class_="results-context-header")

        python_jobs = results.find_all("h1", class_="results-context-header__context")

        for job in python_jobs:
            jobs = job.find("span", class_="results-context-header__job-count")
            country = job.find("span", class_="results-context-header__query-search")
            new_jobs = job.find("span", class_="results-context-header__new-jobs")

            jobs = int((jobs.text.strip()[:-1]).replace(",", ""))
            country = str(country.text.strip())[15:]
            new_jobs = str(new_jobs.text.strip()).replace(",", "")
            new_jobs = int(new_jobs[1 : new_jobs.index("n")])
            today = str(today)

            object["jobs"].append(jobs)
            object["country"].append(country)
            object["new_jobs"].append(new_jobs)
            object["date"].append(today)

    return object


if __name__ == "__main__":
    scrap()

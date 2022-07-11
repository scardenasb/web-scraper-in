import requests
from bs4 import BeautifulSoup
from datetime import date


LOCATION_NAMES = [
    "Japan",
    "Netherlands",
    "United%20States",
    "South%20Korea",
    "Chile",
    "United%20Kingdom",
    "Finland",
    "Sweden",
    "Germany",
    "Denmark",
    "Scotland",
    "Estonia",
    "Canada",
    "Brazil",
    "China",
    "Taiwan",
    "France",
    "Spain",
    "Portugal",
    "Italy",
    "Luxembourg",
    "Switzerland",
    "Ireland",
]


URL = []
url_filler = ""

# NOTE: The query seems to only need the location name, geoId is optional and can be set to "".
for i in LOCATION_NAMES:
    url_filler = f"https://www.linkedin.com/jobs/search?keywords=Python&location={i}&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0"
    URL.append(url_filler)


def scrap():
    today = date.today()
    object = {"jobs": [], "country": [], "new_jobs": [], "date": []}
    for i in URL:
        page = requests.get(i)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find("div", class_="results-context-header")

        python_jobs = results.find_all("h1", class_="results-context-header__context")
        print(python_jobs)

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

    print(object)
    return object


if __name__ == "__main__":
    scrap()

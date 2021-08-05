import requests
import bs4
from bs4 import BeautifulSoup
import re

import pandas as pd
import time

url = "https://www.indeed.com/jobs?q=sql&l=Plano%2C%20TX&vjk=4f00ab261a80c44f"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

def extract_job_title(soup):
    jobs = []
    for td in soup.find_all(name = "td", attrs = {"class" : "resultContent"}):
        for h2 in td.find_all(name = "h2", attrs = {"class": "jobTitle"}):
            for span in h2.find_all(name = "span", attrs = {"title" : re.compile("")}):
                jobs.append(span.text)
    return(jobs)


print(extract_job_title(soup))
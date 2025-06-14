from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd
import re
import datetime
import schedule
import time
import sys

def dailytask():
    if len(sys.argv) < 2:
        print("Please provide key word for searching....")
    else:
        with open(f"freelance_{sys.argv[1]}.csv",'w', newline = '') as csv_file:
            data = {
                'Date Scraped' : [],
                'Title' : [],
                'Budget': [],
                'Skills': [],
                'Link' : []
            }
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['Date Scraped','Title','Budget','Skills','Link'])

            count = 1
            nexpages = True
            while(nexpages):
                source = requests.get(f'https://www.truelancer.com/freelance-jobs?page={count}').text 
                soup = BeautifulSoup(source, 'lxml')
                nexpages = False
                match = soup.find_all('button',class_="MuiButtonBase-root MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-colorPrimary MuiButton-root MuiButton-outlined MuiButton-outlinedPrimary MuiButton-sizeMedium MuiButton-outlinedSizeMedium MuiButton-colorPrimary mui-9l2jk9")
                for mat in match:
                    if mat.text == "Next":
                        count += 1
                        nexpages = True
            

                jobs = soup.find_all('div', class_="MuiGrid-root MuiGrid-container freelancerListItem mui-1d3bbye")
                for job in jobs:
                    Skills = ""
                    match = job.find('div',class_="MuiBox-root mui-ws0b07") 
                    title = match.h3.text
                    link = match.a.get('href','')

                    skills = match.find_all('a',class_="MuiButtonBase-root MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButton-colorPrimary MuiButton-disableElevation mui-12pqbcj")
                    for skill in skills:
                        Skills = Skills + skill.text
                        if(skills[len(skills)-1].text != skill.text):
                            Skills = Skills + ", "

                    match = job.find('div',class_="MuiBox-root mui-1a7p4v5") 
                    budget = match.h6.text
                    skill_list = re.split(", ",Skills)
                    if (sys.argv[1] in skill_list):
                        csv_writer.writerow([str(datetime.date.today())+" - "+str(datetime.datetime.now().strftime("%H:%M:%S")),title,budget,Skills,link])
                        data['Date Scraped'].append(datetime.date.today())
                        data['Title'].append(title)
                        data['Budget'].append(budget)
                        data['Skills'].append(Skills)
                        data['Link'].append(link)
                df= pd.DataFrame(data)
                df.to_excel(f'freelance_{sys.argv[1]}.xlsx')
                
schedule.every().day.at("16:35").do(dailytask())
while True:
    schedule.run_pending()
    time.sleep(1)

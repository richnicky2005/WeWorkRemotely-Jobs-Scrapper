import requests
from bs4 import BeautifulSoup

# URL for the WWR
url = 'https://weworkremotely.com/'

response = requests.get(url)


soup = BeautifulSoup(response.text, 'lxml')

# Full Stack Programming jobs
full_stack_section = soup.find('section', id="category-2")

# Job listings within the section
jobs = full_stack_section.find_all('li', class_="feature")

job_list = []

# Loop through each job listing and extract details
for job in jobs:
    # Job title
    job_title = job.find('span', class_='title').text.strip()
    
    # Company name
    company = job.find('span', class_='company').text.strip()
    
    # Job link
    job_link = job.find('a')['href']
    full_link = f"https://weworkremotely.com{job_link}"  # Add base URL

    # Append job details to the list
    job_list.append({
        'Job Title': job_title,
        'Company': company,
        'Link': full_link
    })

# Print jobs
for job in job_list:
    print(f"Job Title: {job['Job Title']}")
    print(f"Company: {job['Company']}")
    print(f"Link: {job['Link']}")
    print("-" * 40)

# Optional: Save the data to a CSV file
# import csv

# with open('full_stack_jobs.csv', 'w', newline='', encoding='utf-8') as csvfile:
#     fieldnames = ['Job Title', 'Company', 'Link']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#     writer.writeheader()
#     writer.writerows(job_list)

# print("Jobs have been saved to full_stack_jobs.csv")

from bs4 import BeautifulSoup
import requests, os

os.system("clear")

URL = "https://github.com/"
username = ""

while len(username) < 3:
    username = input("Enter github username: ").strip().lower()

webpage = requests.get(URL + username)
soup = BeautifulSoup(webpage.content, 'html.parser')

try:
    name = soup.find("span", attrs={'class': 'p-name vcard-fullname d-block overflow-hidden'}).string
    image_url = soup.find("img", attrs={'class': 'avatar avatar-user width-full border bg-white'})['src']

    repos = []
    webpage = requests.get(URL + username + '?tab=repositories')
    repo_soup = BeautifulSoup(webpage.content, 'html.parser')

    for repo_html in repo_soup.find_all("a", attrs={'itemprop': 'name codeRepository'}):
        repos.append(repo_html.string.replace(' ', '').replace('\n', ''))

    print(f"Name: {name}\nImage url: {image_url}\n")
    print("Repositories: \n", "\n".join(repos), sep="") if len(repos) > 0 else print("Repositories: None")

except AttributeError:
    print("Cant scrape:", username)
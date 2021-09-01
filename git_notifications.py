import requests

headers = { 'Accept': 'application/vnd.github.v3+json'}


req = requests.get("https://api.github.com/users/SolJCam/repos", headers=headers, auth=("username","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"))
# req = requests.get("https://api.github.com/users/SolJCam/repos", headers=headers)
# print(req.json())

list_of_portfolio_projects = [
    'python_website',
    'React-Search-Pics',
    'React-Search-Videos',
    'react-songs',
    'react-twitch-clone',
    'React-Widgets',
    'socket.io'
]

list_of_repos = req.json()
for repo in list_of_repos:
    if repo['name'] in list_of_portfolio_projects:
        commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits" )
        # print(commits_by_project.json()[0]['commit']['message'])
        # print(repo['name'])
        # print(f"https://api.github.com/repos/SolJCam/#{repo['name']}/commits")

        project = repo['name']
        message = commits_by_project.json()[0]['commit']['message']
        date = commits_by_project.json()[0]['commit']['author']['date']
        # print(project/nmessage/ndate/n/n)
        print(project+'\n'+message+'\n'+date+'\n')


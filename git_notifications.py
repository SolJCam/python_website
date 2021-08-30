import requests

headers = { 'Accept': 'application/vnd.github.v3+json'}
# headers = { 
#     'Accept': 'application/vnd.github.v3+json',
#     'username': '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'
# }

# r = requests.get("https://api.github.com/repos/SolJCam/React-Search-Videos/commits", headers=headers, auth=("username","SolJCam")  )
# r = requests.get("https://api.github.com/repos/SolJCam/python_website/commits", auth=("username","SolJCam") )

# project = ''
# message = r.json()[0]['commit']['message']
# date = r.json()[0]['commit']['author']['date']
# print(message/ndate/n/n)


# print(r)
# print(r.text[0])

# print(r.json()[0]['name'])
# print(r.json()[0].keys())
# print(r.json())


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
for name in list_of_repos:
    if name['name'] in list_of_portfolio_projects:
        commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{name['name']}/commits" )
        # print(commits_by_project.json()[0]['commit']['message'])
        # print(name['name'])
        # print(f"https://api.github.com/repos/SolJCam/#{name['name']}/commits")

        project = name['name']
        message = commits_by_project.json()[0]['commit']['message']
        date = commits_by_project.json()[0]['commit']['author']['date']
        # print(project/nmessage/ndate/n/n)
        print(project+'\n'+message+'\n'+date+'\n')


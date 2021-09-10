from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import date, datetime
import requests

sched = BlockingScheduler()

# @sched.scheduled_job('interval', hour=8)
@sched.scheduled_job('interval', minutes=8)
def git_api():
  print("Something")
# def git_api():
#     # if (datetime.now().strftime("%X%p") >= "12:00:00PM" and datetime.now().strftime("%X%p") <= "1:00:00PM" or
#     #   datetime.now().strftime("%X%p") >= "8:00:00PM" and datetime.now().strftime("%X%p") <= "9:00:00PM" or
#     #   datetime.now().strftime("%X%p") >= "4:00:00AM" and datetime.now().strftime("%X%p") <= "5:00:00M"):

#   headers = { 'Accept': 'application/vnd.github.v3+json'}

#   req = requests.get("https://api.github.com/users/SolJCam/repos", headers=headers, auth=("username","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"))
#   # req = requests.get("https://api.github.com/users/SolJCam/repos", headers=headers)
#   # print(req.json())

#   list_of_portfolio_projects = [
#       'python_website',
#       'React-Search-Pics',
#       'React-Search-Videos',
#       'react-songs',
#       'react-twitch-clone',
#       'React-Widgets',
#       'socket.io'
#   ]

#   list_of_repos = req.json()

#   project = ''
#   message = ''
#   dates = ''

#   dictionary_of_repos = {}
  
#   pdb.set_trace()
#   for repo in list_of_repos:
#     if repo['name'] in list_of_portfolio_projects:
#       # commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits", headers=headers, auth=("username","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") )
#       # commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits?since={date.today().isoformat()}T00:00:00Z", headers=headers, auth=("username","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") )
#       commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits?until={date.today().isoformat()}T00:00:00Z", headers=headers, auth=("username","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") )

#       # pdb.set_trace()
#       for ec in range(len(commits_by_project.json())):
#         # pdb.set_trace()
#         project = repo['name']
#         message = commits_by_project.json()[ec]['commit']['message']
#         dates = commits_by_project.json()[ec]['commit']['author']['date']

#         # dictionary_of_repos[repo['name']] = [project,message,dates]
#         dictionary_of_repos[dates] = [project,message]
      
#   # pdb.set_trace()
#   return dictionary_of_repos

# sched.start()
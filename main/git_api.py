import requests, os, csv, pdb
from datetime import date, datetime
# from 

d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

def git_api():

  headers = { 'Accept': 'application/vnd.github.v3+json'}
  
                                                                                      # if receiving 401 error Bad credentials, check OAuth token
  # req = requests.get("https://api.github.com/users/SolJCam/repos", headers=headers, auth=("SolJCam",os.environ["GIT_OAUTH"]))
  req = requests.get("https://api.github.com/users/SolJCam/repos", headers=headers, auth=("SolJCam",os.environ["GIT_OAUTH"]))

  list_of_portfolio_projects = [
      'animal_shelter',
      'python_website',
      'React-Search-Pics',
      'React-Search-Videos',
      'react-songs',
      'react-twitch-clone',
      'React-Widgets',
      'socket.io'
  ]

  list_of_repos = req.json()
  
  
  if req.status_code == 200:
      
    with open(os.path.join(d, "git_api_results.csv"), 'w') as file:
  
      dictionary_of_repos = {}
      writer = csv.DictWriter(file, fieldnames=["Repo"])
      
      for repo in list_of_repos:
        if repo['name'] in list_of_portfolio_projects:
          # commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits?until={date.today().isoformat()}T00:00:00Z", headers=headers, auth=("SolJCam",os.environ["GIT_OAUTH"]))
          # commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits?since={date.today().isoformat()}T00:00:00Z", headers=headers, auth=("SolJCam",os.environ["GIT_OAUTH"]))
          commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits?since=2021-9-12T00:00:00Z", headers=headers, auth=("SolJCam",os.environ["GIT_OAUTH"]))

          for ec in range(len(commits_by_project.json())):
            project = repo['name']
            message = commits_by_project.json()[ec]['commit']['message']
            date = commits_by_project.json()[ec]['commit']['author']['date']           
            
            dictionary_of_repos["Repo"] = [date,project,message]           
            writer.writerow(dictionary_of_repos)  
  
    # pdb.set_trace()
    return "success"

  return req.json()['message']
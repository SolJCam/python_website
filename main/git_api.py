import requests, os, csv, pdb
from datetime import date, datetime, timedelta

today = date.today()

d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

def git_api():

  headers = { 'Accept': 'application/vnd.github.v3+json'}

  list_of_portfolio_projects = [
      'animal_shelter',
      'python_website',
      'React-Search-Videos',
      'socket.io'
  ]

  week_ago_datetime = today - timedelta(days=7)
  week_ago_date = week_ago_datetime.isoformat()
  all_dates = []
  dictionary_of_repos = {}

  for repo in list_of_portfolio_projects:
    try:
                                                                                      # if receiving 401 error Bad credentials, check OAuth token
      # commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo}/commits?since=2021-8-1T00:00:00Z", headers=headers, auth=("SolJCam",os.environ["GIT_OAUTH"]))
      commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo}/commits?since={week_ago_date}T00:00:00Z", headers=headers, auth=("SolJCam",os.environ["GIT_OAUTH"]))
    except Exception as e:
      return e.__str__()

    for ec in range(len(commits_by_project.json())):
      all_dates.append(commits_by_project.json()[ec]['commit']['author']['date']) 

      project = repo
      message = commits_by_project.json()[ec]['commit']['message']
      date = commits_by_project.json()[ec]['commit']['author']['date']   

      dictionary_of_repos[date] = [date,project,message]
        
  all_dates.sort(reverse=True)
  last_five_dates = all_dates[:5]
  # pdb.set_trace()
  git_commits = {}
    
  with open(os.path.join(d, "git_api_results.csv"), 'w') as file:
    writer = csv.DictWriter(file, fieldnames=["Repo"])
    for date in last_five_dates:           
      git_commits["Repo"] = dictionary_of_repos[date]
      writer.writerow(git_commits)  

  return "success"
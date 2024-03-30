import requests, os, csv, pdb, boto3
from datetime import date, datetime, timedelta

today = date.today()

d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

s3_resource = boto3.resource('s3')

def git_api():

  headers = { 'Accept': 'application/vnd.github.v3+json'}

  list_of_portfolio_projects = [
      'animal_shelter',
      'python_website',
      'React-Search-Videos',
      'socket.io',
  ]

  week_ago_datetime = today - timedelta(days=7)
  week_ago_date = week_ago_datetime.isoformat()
  all_dates = []
  dictionary_of_repos = {}

  for project in list_of_portfolio_projects:
    try:
                                                                                      # if receiving 401 error Bad credentials, check OAuth token
      commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{project}/commits?since=2021-10-1T00:00:00Z", headers=headers, auth=("SolJCam",os.environ["GIT_OAUTH"]))
      # commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{project}/commits?since={week_ago_date}T00:00:00Z", headers=headers, auth=("SolJCam",os.environ["GIT_OAUTH"]))
    except Exception as e:
      return e.__str__()

    for ec in range(len(commits_by_project.json())):
      commit_notification_data = commits_by_project.json()[ec].get('commit')
      all_dates.append(commit_notification_data.get('author').get('date')) 
      message = commit_notification_data.get('message')
      dictionary_of_repos[all_dates[-1]] = [all_dates[-1],project,message]
        
  all_dates.sort(reverse=True)
  last_five_dates = all_dates[:5]
  # pdb.set_trace()
  git_commits = {}
    
  with open(os.path.join(d, "git_api_results.csv"), 'w') as file:
    writer = csv.DictWriter(file, fieldnames=["Repo"])
    for date in last_five_dates:           
      git_commits["Repo"] = dictionary_of_repos[date]
      writer.writerow(git_commits) 

  s3_resource.meta.client.upload_file(Filename=os.path.join(d, "git_api_results.csv"),Bucket="py-scraper",Key="git_api_results.csv")

  return "success"
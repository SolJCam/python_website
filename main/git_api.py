import requests, pdb, os, csv
from datetime import date, datetime

d = os.path.dirname(__file__) if "__file__" in locals() else os.getcwd()

def git_api():
    # if (datetime.now().strftime("%X%p") >= "12:00:00PM" and datetime.now().strftime("%X%p") <= "1:00:00PM" or
    #   datetime.now().strftime("%X%p") >= "8:00:00PM" and datetime.now().strftime("%X%p") <= "9:00:00PM" or
    #   datetime.now().strftime("%X%p") >= "4:00:00AM" and datetime.now().strftime("%X%p") <= "5:00:00M"):

  headers = { 'Accept': 'application/vnd.github.v3+json'}
                                                                                        # if receiving 401 error Bad credentials, check OAuth token
  req = requests.get("https://api.github.com/users/SolJCam/repos", headers=headers, auth=("SolJCam","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"))
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

  dictionary_of_repos = {}
  
  # if req.status_code == 200:
  #   with open(os.path.join(d, "git_api_results.txt"), 'w') as file:
  #     for repo in list_of_repos:
  #       if repo['name'] in list_of_portfolio_projects:
  #         # commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits?since={date.today().isoformat()}T00:00:00Z", headers=headers, auth=("SolJCam","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") )
  #         commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits?until={date.today().isoformat()}T00:00:00Z", headers=headers, auth=("SolJCam","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") )

  #         for ec in range(len(commits_by_project.json())):
  #           project = repo['name']
  #           message = commits_by_project.json()[ec]['commit']['message']
  #           dates = commits_by_project.json()[ec]['commit']['author']['date']

  #           dictionary_of_repos[dates] = [project,message]
      
  #     file.write(dictionary_of_repos)
  #     return "success"
    
  # return req.json()['message']
  

  
  writer = ''
  repos = {}

  if req.status_code == 200:
      
    with open(os.path.join(d, "git_api_results.csv"), 'w') as file:
  
      writer = csv.DictWriter(file, fieldnames=["Repo"])
      for repo in list_of_repos:
        if repo['name'] in list_of_portfolio_projects:
          # commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits?since={date.today().isoformat()}T00:00:00Z", headers=headers, auth=("SolJCam","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") )
          commits_by_project = requests.get(f"https://api.github.com/repos/SolJCam/{repo['name']}/commits?since={2021-9-10}T00:00:00Z", headers=headers, auth=("SolJCam","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") )

          for ec in range(len(commits_by_project.json())):
            project = repo['name']
            message = commits_by_project.json()[ec]['commit']['message']
            date = commits_by_project.json()[ec]['commit']['author']['date']           
            
            repos["Repo"] = [date,project,message]           # can't use the below here; fields are already set in the first loop
            writer.writerow(repos)  
            
            # pdb.set_trace()
    
    return "success"

  return req.json()['message']
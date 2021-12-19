web: gunicorn python_portfolio_site.wsgi --preload --timeout 20 --log-file -
worker: python worker.py msnbc cnn fox
clock: python main/git_api_scheduler.py
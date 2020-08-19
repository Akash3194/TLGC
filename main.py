from flask import Flask, render_template, request
import requests
from os.path import join 
from config import username, password, fork_username, fork_repo

app = Flask(__name__)


@app.route('/follow', methods=['POST'])
def follow():

    if username == "":
        return '<h1 style="color: red;">Please add you github credentials in config.py</h1>'

    # print(dir(request))
    user = request.form.get('username')
    follow_url = join(api_url, follow_endpoint.format(user))
    res = requests.put(follow_url, auth=requests.auth.HTTPBasicAuth(username, password))

    if int(res.status_code) == 204:
        return f'<p style="text-align: center;">Now following <b>{user}</b></p>'
    else:
        return '<h1 style="color: red;">Success</h1>'



@app.route('/')
def start():

    fb_endpoint = forks_endpoint.format(fork_username, fork_repo)
    forks = requests.get(join(api_url, fb_endpoint))
    
    return render_template("index.html", data= {"forks":forks.json(), "Username": "akash3194", "Password": "j@@p@@9c#ina"})


if __name__ == '__main__':

    api_url = "https://api.github.com/"
    forks_endpoint = "repos/{}/{}/forks"
    follow_endpoint = "user/following/{}"

    app.run(debug=True)
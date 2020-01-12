# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask, Markup, render_template
import pymongo


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""

    client = pymongo.MongoClient(
        "mongodb+srv://Cizor:best123@cluster0-wazd4.gcp.mongodb.net/test?retryWrites=true&w=majority")

    b = client.list_database_names()

    c = client.sample_mflix
    d = c.comments
    response = "<h1>These are sample comments</h1><br>"
    for i in d.find():
        response += f"<h4>By {i['name']}</h4><h5>{i['text']}</h5><br>"

    return render_template("index.html", response=Markup(response))


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]

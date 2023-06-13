from flask import Flask,render_template
import requests
from post import Post

app = Flask(__name__)
data = requests.get(url='https://api.npoint.io/e6e3e542f753dcc98791').json()

objs = []
for resp in data:
    new_obj = Post(resp["id"],resp["title"],resp["subtitle"],resp["body"])
    objs.append(new_obj)


@app.route('/')
def home():
    return render_template('index.html',blogs=objs)

@app.route('/about')
def get_about():
    return render_template('about.html')

@app.route('/contact')
def get_contact():
    return render_template('contact.html')

@app.route('/<post_id>')
def get_post(post_id):
    return render_template('post.html',post_id=int(post_id),blogs=objs)

if __name__ == '__main__':
    app.run(debug=True)

    
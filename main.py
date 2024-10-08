from flask import Flask, render_template
import requests as rq

app = Flask(__name__)

@app.route('/')
def home():
    response = rq.get('https://api.npoint.io/c790b4d5cab58020d391')
    blog_posts = response.json() #Type dict
    return render_template('index.html', posts=blog_posts)

@app.route('/blog/<int:post_id>')
def blog(post_id):
    response = rq.get('https://api.npoint.io/c790b4d5cab58020d391')
    blog_posts = response.json()  # Fetch again or cache it

    # Fetch the specific post
    blog_post = blog_posts[post_id]  # Assuming `post_id` matches the index in the list
    return render_template('post.html', blog_post=blog_post)


if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
app = Flask(__name__)
from flask import render_template

posts = []

@app.route("/")
def index():
    #return "{} posts".format(len(posts)) ## en vez de devolver el contenido de post
    return render_template("index.html", num_posts=len(posts))

@app.route("/p/<string:slug>/")
def show_post(slug):
    #return "Mostrando el post {}".format(slug)
    return render_template("post_view.html", slug_title=slug)

@app.route("/admin/post/")
@app.route("/admin/post/<int:post_id>/")
def post_form(post_id=None):
    #return "post_form {}".format(post_id)
    return render_template("admin/post_form.html", post_id=post_id)
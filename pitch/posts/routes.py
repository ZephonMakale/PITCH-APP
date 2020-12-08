from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from pitch import db
from pitch.models import Post, Comment, Upvote, Downvote
from pitch.posts.forms import PostForm, CommentForm

posts = Blueprint('posts', __name__)

@posts.route("/post/new", methods = ['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data, content = form.content.data, author = current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title = 'New Post', form = form, legend = 'New Post')

@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@posts.route("/post/<int:post_id>/update", methods = ['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('create_post.html', title = 'Update Post', form = form, legend = 'Update Post')

@posts.route("/post/<int:post_id>/delete", methods = ['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.home'))

@posts.route("/comment/<int:post_id>/comment", methods = ['GET', 'POST'])
@login_required
def comment(post_id):
    form =  CommentForm()
    post = Post.query.get(post_id)
    all_comments = Comment.query.filter_by(post_id = post_id).all()
    if form.validate_on_submit():
        comment = form.comment.data
        post_id = post_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment, user_id = user_id, post_id = post_id)
        new_comment.save_comment()
        return redirect(url_for('posts.comment', post_id=post.id))
    return render_template('comment.html', form = form, post = post, all_comments=all_comments)

@posts.route("/like/<int:id>", methods = ['GET', 'POST'])
@login_required
def like(id):
    get_posts = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for post in get_posts:
        to_str = f'{post}'
        print(valid_string+""+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.home', id=id))
        else:
            pass
    new_vote = Upvote(user = current_user, post_id =id)
    new_vote.save()
    return redirect(url_for('main.home', id= id))

@posts.route("/dislike/<int:id>", methods = ['GET', 'POST'])
@login_required
def dislike(id):
    post = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for posty in post:
        to_str = f'{posty}'
        print(valid_string+""+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.home', id=id))
        else:
            pass
    new_downvote = Downvote(user = current_user, post_id =id)
    new_downvote.save()
    return redirect(url_for('main.home', id= id))
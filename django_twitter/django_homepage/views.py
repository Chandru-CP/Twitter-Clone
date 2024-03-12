from .forms import PostForm, CommentForm
from .models import Hashtag, Comment
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required


def homepage(request):
    posts = Post.objects.all().order_by('-timestamp')
    comments = Post.objects.all().order_by('-timestamp')

    return render(request, 'django_homepage/homepage.html', {'posts': posts, 'comments': comments})


@login_required()
def upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            message = form.cleaned_data['message']
            hashtags = form.cleaned_data['hashtags']
            picture = form.cleaned_data['picture']
            hashtag_list = hashtags.split()
            post = Post.objects.create(
                author = request.user,
                message = message,
                picture = picture,
            )

            for hashtag_text in hashtag_list:
                hashtag, created = Hashtag.objects.get_or_create(hashtags=hashtag_text)
                post.hashtags.add(hashtag)
            return redirect('homepage')
    else:
        form = PostForm()
    return render(request, 'django_homepage/upload_post.html', {'form': form})


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        print(request.user,post.author)
        if request.user == post.author:
            post.delete()
        return redirect('homepage')

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return redirect('homepage')

def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    post.num_likes += 1
    post.save()
    return redirect('post_detail', post_id=post_id)


def unlike_post(request, post_id):
    post = Post.objects.get(id=post_id)
    if post.num_likes > 0:
        post.num_likes -= 1
        post.save()
    return redirect('post_detail', post_id=post_id)


def add_comment(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comments = form.cleaned_data['comments']
            comment_list = comments.split()
            for comment_text in comment_list:
                comment, created = Comment.objects.get_or_create(
                    post=post,
                    user=request.user,
                    comments=comment_text
                )

                post.comments.add(comment)
            return redirect('homepage')
    else:
        form = CommentForm()
    return render(request, 'django_homepage/add_comment.html', {'form': form})


def delete_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        if request.user == post.author:
            for comment in post.comments.all():
                comment.delete()
    return redirect('homepage')

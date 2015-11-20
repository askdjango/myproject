from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import CommentForm


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list': post_list,
    })


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)  # Post.DoesNotExist
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })


def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.save()
            return redirect('blog:post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def comment_edit(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=post_pk)
            comment.save()
            return redirect('blog:post_detail', post_pk)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


def comment_delete(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('blog:post_detail', post_pk)
    return render(request, 'blog/comment_delete_confirm.html', {
        'comment': comment,
    })




def post_new(request):
    return render(request, 'blog/post_form.html')

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm


'''
def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/index.html', {
        'post_list': post_list,
    })
'''


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'

# index = ListView.as_view(model=Post, template_name='blog/index.html')
index = PostListView.as_view()



'''
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)  # Post.DoesNotExist
    return render(request, 'blog/post_detail.html', {
        'post': post,
    })
'''

post_detail = DetailView.as_view(model=Post)  #, pk_url_kwarg='id', template_name='blog/other_detail.html')



'''
@login_required
def post_create(request):
    # request.GET
    # request.POST
    # request.FILES

    # request.user =>
    # django.contrib.auth.models.AnonymousUser
    # django.contrib.auth.models.User

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })
'''


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    # success_url = reverse_lazy('blog:index')

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super(PostCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.object.pk])

# post_create = login_required(PostCreateView.as_view())
post_create = PostCreateView.as_view()



'''
@login_required
def post_update(request, pk):
    post = Post.objects.get(pk=pk)

    if post.author != request.user:
        return redirect('blog:post_detail', pk)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('blog:post_detail', post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {
        'form': form,
    })
'''

class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return reverse('blog:post_detail', args=[self.object.pk])

# post_update = login_required(PostUpdateView.as_view())
post_update = PostUpdateView.as_view()


'''
@login_required
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)

    if post.author != request.user:
        return redirect('blog:post_detail', pk)

    if request.method == 'POST':
        post.delete()
        return redirect('blog:index')
    return render(request, 'blog/post_delete_confirm.html', {
        'post': post,
    })
'''

class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:index')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            return redirect('blog:post_detail', self.kwargs['pk'])
        return super(PostDeleteView, self).dispatch(request, *args, **kwargs)

# post_delete = login_required(PostDeleteView.as_view())
post_delete = PostDeleteView.as_view()


@login_required
def comment_new(request, pk):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = Post.objects.get(pk=pk)
            comment.author = request.user
            comment.save()
            return redirect('blog:post_detail', pk)
    else:
        form = CommentForm()
    return render(request, 'blog/post_form.html', {
        'form': form,
    })


@login_required
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


@login_required
def comment_delete(request, post_pk, pk):
    comment = Comment.objects.get(pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('blog:post_detail', post_pk)
    return render(request, 'blog/comment_delete_confirm.html', {
        'comment': comment,
    })

from django.shortcuts import redirect


class PostAuthorMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            return redirect('blog:post_detail', self.kwargs['pk'])
        return super(PostAuthorMixin, self).dispatch(request, *args, **kwargs)

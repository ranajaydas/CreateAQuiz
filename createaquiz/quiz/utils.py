from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Quiz


class CreateUpdateMixin:
    """Class inherited by Create and Update Views."""
    template_name = 'quiz/base_quiz_form.html'

    def get_context_data(self, **kwargs):
        """Add extra context to Views."""
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class DeleteMixin:
    """Class inherited by Delete Views."""
    template_name = 'quiz/base_quiz_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        """Shows success_message upon deletion."""
        messages.warning(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)


class UserIsAuthorMixin(UserPassesTestMixin):

    def form_valid(self, form):
        """Valid if the user is the author."""
        if self.model.__name__ is 'Quiz':
            form.instance.author = self.request.user

        if self.model.__name__ is 'Question':
            form.instance.quiz.author = self.request.user

        return super().form_valid(form)

    def test_func(self):
        """Passes if the user is the author."""
        if self.model.__name__ is 'Quiz':
            quiz = self.get_object()

        if self.model.__name__ is 'Question':
            quiz_slug = self.kwargs.get('quiz_slug')
            quiz = get_object_or_404(Quiz, slug__iexact=quiz_slug)

        return self.request.user == quiz.author


class PageLinksMixin:
    """Mixin for Pagination and Search results."""
    page_kwarg = 'page'
    search_kwarg = 'q'

    def _page_urls(self, page_number):
        if self.search_kwarg in self.request.GET:
            search_term = self.request.GET[self.search_kwarg]
            return "?{}={}&{}={}".format(self.search_kwarg, search_term, self.page_kwarg, page_number)
        else:
            return "?{}={}".format(self.page_kwarg, page_number)

    def first_page(self, page):
        # don't show on first page
        if page.number > 1:
            return self._page_urls(1)
        return None

    def last_page(self, page):
        last_page = page.paginator.num_pages
        if page.number < last_page:
            return self._page_urls(last_page)
        return None

    def previous_page(self, page):
        if page.has_previous():
            return self._page_urls(page.previous_page_number())
        return None

    def next_page(self, page):
        if page.has_next():
            return self._page_urls(page.next_page_number())
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = context.get('page_obj')
        if page is not None:
            context.update({'previous_page_url': self.previous_page(page),
                            'next_page_url': self.next_page(page),
                            'first_page_url': self.first_page(page),
                            'last_page_url': self.last_page(page),
                            })
        return context


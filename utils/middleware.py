from threading import local
from re import compile
from django.conf import settings
from django.shortcuts import redirect, reverse
from django.utils.deprecation import MiddlewareMixin

_thread_locals = local()


def get_current_request():
    """
    :returns the HttpRequest object for this thread
    """
    return getattr(_thread_locals, "request", None)


def get_current_user():
    """
    :returns the current user if it exists or None otherwise
    """
    request = get_current_request()
    if request:
        return getattr(request, "user", None)


class ThreadLocalMiddleware(object):
    """
    Middleware to add the HttpRequest to thread local storage
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        _thread_locals.request = request
        return self.get_response(request)


login_required_urls = [compile(expr) for expr in getattr(settings, 'LOGIN_REQUIRED_URLS', [])]


class LoginRequiredMiddleware(MiddlewareMixin):
    """
    Add this middleware in the settings.py file
    Include this in settings.py file
    LOGIN_REQUIRED_URLS = [
    r'^panel/(.*)$'
]
    """

    def process_request(self, request):
        if not request.user.is_authenticated:
            path = request.path_info.lstrip('/')
            if any(m.match(path) for m in login_required_urls):
                return redirect('{}?next={}'.format(reverse(settings.LOGIN_URL), request.path))

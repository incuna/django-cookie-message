from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string


COOKIE_MESSAGE_KWARGS = {
    'key': 'cookie_message',
    'value': '',
    'max_age': 365 * 24 * 60 * 60,
    'expires': None,
    'path': '/',
    'domain': None,
    'secure': None,
    'httponly': False,
}
COOKIE_MESSAGE_KWARGS.update(getattr(settings, 'COOKIE_MESSAGE_KWARGS', {}))


class CookieMessageMiddleware(object):
    template = 'cookies/message.html'

    def process_view(self, request, *args, **kwargs):
        # Add message on request
        if not self.has_cookie(request):
            messages.info(request, self.get_message(request))

    def process_template_response(self, request, response):
        # Add cookie on response
        if not self.has_cookie(request):
            response.set_cookie(**COOKIE_MESSAGE_KWARGS)
        return response

    def has_cookie(self, request):
        if not hasattr(request, 'COOKIES'):
            return False
        return COOKIE_MESSAGE_KWARGS['key'] in request.COOKIES

    def get_context(self, request):
        return {'request': request}

    def get_message(self, request):
        return render_to_string(self.template, self.get_context(request))

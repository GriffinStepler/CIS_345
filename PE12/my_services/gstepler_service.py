# Griffin Stepler, CIS345, iCourse, PE12
from nameko.rpc import rpc, RpcProxy
from nameko.web.handlers import http
from time import ctime
from getpass import getuser


class WebServer:
    """web server service to handle http GET requests"""
    name = 'web_server'
    greeting_service = RpcProxy('greeting_service')

    @http('GET', '/')
    def home(self, request):
        """what do you want to load as your homepage"""
        username = getuser()
        return self.greeting_service.greet(username)


class GreetingService:
    """tbd"""
    name = 'greeting_service'

    @rpc
    def greet(self, name):
        return f'Hello {name}! Visited site at {ctime()}.'

# Griffin Stepler, CIS345, iCourse, PE12
from nameko.rpc import rpc


class GreetingService:
    """tbd"""
    name = 'greeting_service'

    @rpc
    def greet(self, name):
        return f'Hello {name}! Greeting service executed.'

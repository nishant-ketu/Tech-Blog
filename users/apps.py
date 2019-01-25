from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    def reddy(self):
    	import users.signals

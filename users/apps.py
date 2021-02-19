from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # to avoid creating Profiles through admin panel
    def ready(self):
    	import users.signals

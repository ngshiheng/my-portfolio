from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

    # creates a profile automatically right after account is registered
    def ready(self):
        import user.signals
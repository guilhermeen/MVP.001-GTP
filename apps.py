from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'  # change this to match your database settings
    name = 'myapp'  # change this to match the name of your app
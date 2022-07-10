from django.apps import AppConfig


class FileConfig(AppConfig):
    name = 'apps.file'
    label = 'file'

    def ready(self):
        import apps.file.signals.handlers

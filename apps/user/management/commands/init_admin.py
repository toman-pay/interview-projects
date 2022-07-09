from django.core.management.base import BaseCommand

from django.contrib.auth import get_user_model

User = get_user_model()


class Command(BaseCommand):
    help = 'Create init superuser if not exists.'

    def handle(self, *args, **options):
        if not User.objects.all().exists():
            User.objects.create_superuser(username="admin", password="admin")
            print("Admin user created.")

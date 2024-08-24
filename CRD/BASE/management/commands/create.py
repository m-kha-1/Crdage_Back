from django.core.management.base import BaseCommand


from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from BASE.models import UserProfile, Producer2, Supervisor2, CgArtist3

# from BASE.views import createUser  

class Command(BaseCommand):
    help = 'Create a new user exemple :python manage.py create_user --username alice --email alice@example.com --password secret --organization AcmeInc --type producer'

    def add_arguments(self, parser):
        parser.add_argument("--user",'username', type=str, help='The username')
        parser.add_argument("--email",'email', type=str, help='The email address')
        parser.add_argument("--password",'password', type=str, help='The password')
        parser.add_argument("--organization",'organization',type=str,help='organization')
        parser.add_argument('--type', type=str, choices=['producer', 'supervisor', 'cgartist'], help='The user type')
        parser.add_argument('--role', type=str, help='The role for cgartist')

    def handle(self, *args, **options):
        username = options['username']
        email = options['email']
        password = options['password']
        organization = options['organization']
        user_type = options['type']
        role = options.get('role', '')

        if user_type == "producer":
            user = User.objects.create_user(username=username, email=email, password=password,organization=organization)
            profile = UserProfile.objects.create(user=user, type=user_type)
            producer = Producer2.objects.create(user=user, name=username)
        elif user_type == "supervisor":
            user = User.objects.create_user(username=username, email=email, password=password)
            profile = UserProfile.objects.create(user=user, type=user_type)
            supervisor = Supervisor2.objects.create(user=user, name=username)
        elif user_type == "cgartist":
            user = User.objects.create_user(username=username, email=email, password=password)
            profile = UserProfile.objects.create(user=user, type=user_type)
            cgartist = CgArtist3.objects.create(user=user, name=username, role=role)
        else:
            self.stdout.write(self.style.ERROR(f'Invalid user type: {user_type}'))

        self.stdout.write(self.style.SUCCESS(f'User created successfully: {username}'))
from django_seed import Seed
from django.core.management.base import BaseCommand, CommandParser
from rooms import models as room_models
from users import models as user_models
import random


class Command(BaseCommand):
    
    help = "This command creates many users"

    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int, help = "how many users do you want to create?", )

    

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        room_types = room_models.RoomType.objects.all()
        seeder.add_entity(room_models.Room, number, {
            "name": lambda x: seeder.faker.address(),
            "host": lambda x: random.choice(all_users),
            "room_type": lambda x: random.choice(room_types),
            "guests": lambda x: random.randint(1, 20),
            "price": lambda x: random.randint(1, 10000),
            "beds": lambda x: random.randint(1, 5),
            "bedrooms": lambda x: random.randint(1, 5),
            "baths": lambda x: random.randint(1, 5),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} rooms created!"))     # why is o/p not in green 
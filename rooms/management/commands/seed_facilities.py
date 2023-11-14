from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from rooms.models import Facilitie

class Command(BaseCommand):
    
    help = "This command creates facilities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help = "this is arguments help command", )

    

    def handle(self, *args, **options):
        facilities = [
        "Spa",
        "Semi open & outdoor restaurant",
        "Poolside bar",
        "Car parking",
        "Swimming pool/ Jacuzzi",
        "Public computer",
        "Disable rooms & Interconnecting rooms",
        "24 Hour security",
        "Outside catering service",
        "100 Seating capacity restaurant",
        "150 Capacity outdoor terrace",
        "45 Seating conference room",
        "35 Seating private air-conditioning dining room",
        "Water purification system",
        "Sunset boat trip",
        "Gift shop",
        ]

        for f in facilities:
            Facilitie.objects.create(name=f)
        self.stdout.write(self.style.SUCCESS(f"{len(facilities)} facilities created"))     # why is o/p not in green 
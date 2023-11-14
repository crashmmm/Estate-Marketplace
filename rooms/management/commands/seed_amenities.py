from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from rooms.models import Amenity

class Command(BaseCommand):
    
    help = "This command creates amenities"

    # def add_arguments(self, parser):
    #     parser.add_argument("--times", help = "this is arguments help command", )

    

    def handle(self, *args, **options):
        amenities = [
            "Gyms",
            "Swimming pool",
            "Parking",
            "Pet amenities",
            "Air conditioning",
            "Washer and dryer",
            "Playground",
            "Security",
            "Clubhouse",
            "Community garden",
            "Dishwasher",
            "Recreational amenities",
            "Garbage disposal",
            "Parking space",
            "Balcony",
            "Common areas",
            "Patio",
            "Amenity",
            "Closet Space",
            "Kitchen appliances",
            "Package lockers",
            "Power Backup",
            "Rooftop deck",
            "Rooftops",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS("Amenities created!"))     # why is o/p not in green 
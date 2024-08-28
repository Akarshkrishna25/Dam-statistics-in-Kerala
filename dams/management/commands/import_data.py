from django.core.management.base import BaseCommand
from dams.models import Dam, DamStatistics
import requests
from bs4 import BeautifulSoup
from datetime import datetime

class Command(BaseCommand):
    help = 'Populate the dam statistics data from the KSEB website'

    def handle(self, *args, **kwargs):
        url = "https://dams.kseb.in/?p=4703"
        response = requests.get(url, timeout=10)

        soup = BeautifulSoup(response.text, 'html.parser')

        # Parse the data (Example, actual implementation will vary based on the structure)
        # Extract dam data and save to the database
        for dam_data in parsed_data:
            dam, created = Dam.objects.get_or_create(
                name=dam_data['name'],
                district=dam_data['district']
            )

            for stat in dam_data['statistics']:
                DamStatistics.objects.update_or_create(
                    dam=dam,
                    date=datetime.strptime(stat['date'], '%Y-%m-%d'),
                    defaults={
                        'rainfall': stat['rainfall'],
                        'inflow': stat['inflow'],
                        'power_house_discharge': stat['power_house_discharge'],
                        'spillway_release': stat['spillway_release'],
                    }
                )

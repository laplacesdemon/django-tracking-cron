from django.core.management.base import BaseCommand, CommandError
from tracking_cron.models import VisitorTotal

class Command(BaseCommand):
    args = ''
    help = 'Updates the total user and page view count on tracking app'

    def handle(self, *args, **options):
        VisitorTotal.objects.create_total()
        self.stdout.write('Successfully updated the user tracking totals')
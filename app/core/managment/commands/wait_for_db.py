"""
Django command  to wait for the database to be availavle
"""

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """Django commanf to wait for database"""
    
    def handle(self, *args, **options):
        pass
"""therapists_profiles app tests"""

from datetime import date
import os
import django
from django.test import TestCase

from therapists_profiles.services.airtable_services import AirtableService
from therapists_profiles.models import SyncRecord, Therapist

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "meta_fullstack.settings")
django.setup()


def fill_test_table(airtable):
    """fills test airtable with test values"""
    airtable.insert({
        'Имя': 'Test_Name',
        'Методы': ['test_method_1', 'test_method_2'],
    })


def clear_test_table(airtable):
    """clears test airtable"""
    for record in airtable.get_all():
        airtable.delete(record['id'])


class AirtableServiceTestCase(TestCase):
    """Class for testing airtable services"""

    def test_get_therapists_from_airtable(self):
        """Test for get_therapists_from_airtable()"""
        airtable_service = AirtableService('Test_Table')
        airtable_therapists = airtable_service.get_therapists_from_airtable()
        self.assertEqual(airtable_therapists[0]['name'], 'Test_Name')

    def test_sync_airtable_with_postgres(self):
        """Test for sync_airtable_with_postgres()"""
        airtable_service = AirtableService('Test_Table')
        airtable_service.sync_airtable_with_postgres()
        self.assertEqual(Therapist.objects.first().name, 'Test_Name')
        self.assertEqual(SyncRecord.objects.last().date, date.today())

import datetime
from django.test import TestCase

from .models import Entry

# Create your tests here.
class EntryModelTests(TestCase):
    def test_was_entry_added(self):
        return True
        #create valid entry object
        #self.assertIs(entry.add, False)
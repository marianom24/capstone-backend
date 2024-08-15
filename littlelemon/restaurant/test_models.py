from django.test import TestCase
from .models import Menu, Booking

class MenuTest(TestCase):
    def test_get_item(self):
        item =  Menu.objects.create(title='Choripan', price=12, inventory=30)
        self.assertEqual(str(item),'Choripan : 12')
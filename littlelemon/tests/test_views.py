from django.test import TestCase
from restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(title="chorizo", price=10.99, inventory=20)
        self.item2 = Menu.objects.create(title="molleja", price=5.99, inventory=50)
        self.item3  = Menu.objects.create(title="vaciog", price=15.99, inventory=30)

    def test_getall(self):
        response = self.client.get('/restaurant/menu/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
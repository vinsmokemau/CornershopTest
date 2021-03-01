"""Invitations tests."""

# Utils
from datetime import datetime

# Django
from django.test import Client, TestCase

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Model
from apps.users.models import User
from rest_framework.authtoken.models import Token
from apps.orders.models import Menu, Option, Order


class OrderTestCase(APITestCase):
    """Invitations manager test case."""

    def setUp(self):
        """Test case setup."""
        today = datetime.now().date()

        self.user = User.objects.create(
            username='backendev',
            first_name='Backend',
            last_name='Developer',
            email='backendev@cornershopapp.com',
            password='back_dev_1234',
            is_active=True,
        )
        self.menu = Menu.objects.create(
            day=today
        )
        self.option = Option.objects.create(
            menu=self.menu,
            description="Hamburguer",
        )

    def get_today_request_body(self):
        return {
            "user": self.user.id,
            "option": self.order.id,
            "specifications": "With bacon and no lettuce",
        }

    def create_order(self):
        response = self.client.post(
            '/api/orders/',
            self.get_today_request_body(),
            'application/json'
        )
        self.assertEqual(response.status_code, 201)

        data = response.json()
        order = Order.objects.get(id=data['id'])
        return order

    def test_list_menus(self):
        today = datetime.now().date()

        response = self.client.get('/api/menus/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

        today_menu = self.create_today_menu()
        not_today_menu = self.create_not_today_menu()
        expected = [
            {
                'id': today_menu.id,
                "day": today,
                "options": [
                    {
                        "description": "Chicken and Salad",
                    },
                    {
                        "description": "Pork and Salad",
                    },
                ]
            },
            {
                'id': not_today_menu.id,
                "day": "2021-03-14"
                "options": [
                    {
                        "description": "Pizza and Coke",
                    },
                    {
                        "description": "Hamburguer and Chips",
                    },
                ]
            },
        ]
        response = self.client.get('/api/menus/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected)

    def test_create_order(self):
        response = self.client.post(
            '/api/menus/',
            self.get_today_request_body(),
            'application/json'
        )
        self.assertEqual(response.status_code, 201)

        order = Order.objects.get()
        expected = [
            {
                'id': order.id,
                "user": self.user.id,
                "option": self.option.id,
                "specifications": "With bacon and no lettuce"
            },
        ]
        self.assertEqual(response.json(), expected)

"""Invitations tests."""

# Utils
from datetime import datetime

# Django REST Framework
from rest_framework import status
from rest_framework.test import APITestCase

# Model
from apps.users.models import User
from apps.orders.models import Menu, Option
from rest_framework.authtoken.models import Token


class MenuValidUserTestCase(APITestCase):
    """Invitations manager test case."""

    def setUp(self):
        """Test case setup."""
        self.valid_user = User.objects.create(
            username='bigboss',
            first_name='nora_cornershop',
            last_name='X',
            email='nora@cornershopapp.com',
            is_staff=True,
            is_active=True,
            is_superuser=True,
            password='nora_pass_1234',
        )

        # Auth
        self.token = Token.objects.create(user=self.valid_user).key
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(self.token))

    def get_today_request_body(self):
        today = datetime.now().date()
        return {
            "day": today,
            "options": [
                {
                    "description": "Chicken and Salad",
                },
                {
                    "description": "Pork and Salad",
                },
            ]
        }

    def get_not_today_request_body(self):
        return {
            "day": "2021-03-14",
            "options": [
                {
                    "description": "Pizza and Coke",
                },
                {
                    "description": "Hamburguer and Chips",
                },
            ]
        }

    def create_today_menu(self):
        response = self.client.post(
            '/api/menus/',
            self.get_today_request_body(),
            'application/json'
        )
        self.assertEqual(response.status_code, 201)

        data = response.json()
        menu = Menu.objects.get(id=data['id'])
        return menu

    def create_not_today_menu(self):
        response = self.client.post(
            '/api/menus/',
            self.get_not_today_request_body(),
            'application/json'
        )
        self.assertEqual(response.status_code, 201)

        data = response.json()
        menu = Menu.objects.get(id=data['id'])
        return menu

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
                "day": "2021-03-14",
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

    def test_today_menu(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])

        menu = self.create_menu()
        not_today_menu = self.create_not_today_menu()
        utc_now = pytz.utc.localize(datetime.utcnow())
        mex_now = utc_now.astimezone(pytz.timezone("America/Mexico_City"))
        today, time = mex_now.date(), mex_now.time()
        if 11 > time.hour:
            expected = [
                {
                    'id': menu.id,
                    "day": menu.day,
                    "options": [
                        {
                            "description": "Chicken and Salad",
                        },
                        {
                            "description": "Pork and Salad",
                        },
                    ]
                },
            ]
            response = self.client.get('/api/menu/')
            self.assertEqual(response.status_code, 200)
            self.assertEqual(response.json(), expected)
        else:
            self.assertEqual(response.status_code, 405)

    def test_create_menu(self):
        self.assertEqual(menu.objects.count(), 0)

        response = self.client.post(
            '/api/menus/',
            self.get_today_request_body(),
            'application/json'
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(menu.objects.count(), 1)

        menu = Menu.objects.get()
        expected = [
            {
                'id': menu.id,
                "day": menu.day,
                "options": [
                    {
                        "description": "Chicken and Salad",
                    },
                    {
                        "description": "Pork and Salad",
                    },
                ]
            },
        ]
        self.assertEqual(response.json(), expected)

    def test_update_menu(self):
        menu = self.create_today_menu()

        data = {
            "id": menu.id,
            "day": menu.day,
            "options": [
                {
                    "description": "Chicken and Salad",
                },
                {
                    "description": "Pork and Salad",
                },
            ]
        }

        # Test HTTP PUT
        response = self.client.put(
            f'/api/orders/{menu.id}/',
            data,
            'application/json',
        )
        self.assertEqual(response.status_code, 200)

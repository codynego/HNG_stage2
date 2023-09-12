# myapp/tests.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Person
from .serializers import PersonSerializer

class PersonViewSetTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person_data = {
            'name': 'John Doe',
        }
        self.person = Person.objects.create(**self.person_data)

    def test_list_persons(self):
        response = self.client.get('/api/')  # Replace with your actual API URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_person(self):
        response = self.client.get(f'/api/{self.person.id}/')  # Replace with your actual API URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_person(self):
        response = self.client.post('/api/', self.person_data, format='json')  # Replace with your actual API URL
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_person(self):
        updated_data = {
            'name': 'Updated Name',
        }
        response = self.client.put(f'/api/{self.person.id}/', updated_data, format='json')  # Replace with your actual API URL
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_person(self):
        response = self.client.delete(f'/api/{self.person.id}/')  # Replace with your actual API URL
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

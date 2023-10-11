# test_integration.py
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.test import TestCase
from agenda.models import Agenda  # Import your models and serializers as needed
from rest_framework.authtoken.models import Token

class IntegrationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(username='testuser', password='testpassword') 
        
        self.agenda = Agenda.objects.create(user=self.user, title='Test Agenda', description='Test Description', status='Pending', due_date='2023-10-15')

    def test_agenda_detail_api_get(self):
        self.client.force_authenticate(user=self.user)
        

        url = reverse('agenda-detail' , args=[self.agenda.id])
        

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_agenda_detail_api_put(self):
        self.client.force_authenticate(user=self.user)
        data = {
            'title': 'Updated Agenda',
            'description': 'Updated Description',
            'status': 'Completed',
            'due_date': '2023-10-20'
        }
        url = reverse('agenda-detail', args=[self.agenda.id])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

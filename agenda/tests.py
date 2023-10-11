from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient
from .views import AgendaListAV, AgendaDetailAV
from .models import Agenda
from .serializer import AgendaSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class AgendaViewTests(TestCase):



    def setUp(self):
        self.factory = APIRequestFactory()
        self.client = APIClient()
        
        self.user = User.objects.create(username='testuser', password='testpassword')
      
        
        self.agenda = Agenda.objects.create(user=self.user, title='Test Agenda', description='Test Description', status='Pending', due_date='2023-10-15')

    def test_agenda_list_view(self):
        self.client.force_authenticate( user =self.user)
        
        request = self.factory.get('/agendaList/')
        request.user = self.user
        response = AgendaListAV.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_agenda_detail_view_get(self):
        self.client.force_authenticate( user =self.user)
        
        request = self.factory.get('/view_agenda/1')
        request.user = self.user
        response = AgendaDetailAV.as_view()(request, agendaID=1)
        self.assertEqual(response.status_code, 200)

    def test_agenda_serializer(self):
        serializer = AgendaSerializer(self.agenda)
        self.assertEqual(serializer.data['title'], 'Test Agenda')

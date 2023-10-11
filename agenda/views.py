from django.shortcuts import render
from .models import Agenda
from .serializer import AgendaSerializer

from rest_framework.response import Response
from rest_framework import generics


from rest_framework import status
from rest_framework.views import APIView
from .permissions import UserOnly, IsAuthenticated


from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q






# Create your views here.
class CreateAgendaAV(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = AgendaSerializer

    def perform_create(self, serializer):

        agenda_author = self.request.user

        serializer.save(user = agenda_author)



class AgendaListAV(APIView):
    permission_classes = [IsAuthenticated, UserOnly]
    def get(self, request):
       
        agendas = Agenda.objects.filter(user__username=request.user)

       
        status = request.query_params.get('status', None)
        if status:
            agendas = agendas.filter(status=status)

        title = request.query_params.get('title', None)

        if title:
            agendas = agendas.filter(title= title)

        

        
        sort_by = request.query_params.get('sort_by', 'created')  # Default sorting by 'created'
        agendas = agendas.order_by(sort_by)

        
        search_query = request.query_params.get('search', None)
        if search_query:
            
            agendas = agendas.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(due_date__icontains=search_query)
            )

        
        page = request.query_params.get('page', 1)  # Default page 1
        page_size = request.query_params.get('page_size', 10)  # Default page size 10

        paginator = Paginator(agendas, page_size)
        try:
            agendas = paginator.page(page)
        except EmptyPage:
            return Response([], status=status.HTTP_200_OK)

        serializer = AgendaSerializer(agendas, many=True)
        return Response(serializer.data)
    



class AgendaDetailAV(APIView):
    permission_classes = [IsAuthenticated, UserOnly]

    def get_object(self , primaryKey):
        try:
            return Agenda.objects.get(pk = primaryKey)
        except Agenda.DoesNotExist:
            return Response({'ERROR' : 'Object Does not exist'} , status = status.HTTP_404_NOT_FOUND)
        


    def get(self, request , agendaID):
        agenda = self.get_object(agendaID)
        # Check permissions before proceeding
        if not request.user == agenda.user:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)


        serializer = AgendaSerializer(agenda)

        return Response(serializer.data)
    



    def put(self, request , agendaID):
        agenda = self.get_object(agendaID)
        # Check permissions before proceeding
        if not request.user == agenda.user:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)


        serializer = AgendaSerializer(agenda, data = request.data)

        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data , status=status.HTTP_200_OK)
        
        return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
    


    def delete(self , request , agendaID):
        agenda = self.get_object(agendaID)
        # Check permissions before proceeding
        if not request.user == agenda.user:
            return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)


        agenda.delete()

        return Response(status = status.HTTP_204_NO_CONTENT)
    












        

        
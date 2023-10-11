from .views import CreateAgendaAV, AgendaListAV, AgendaDetailAV




from django.urls import path

urlpatterns = [
    path('create/' , CreateAgendaAV.as_view() , name = 'create-agenda' ),
    path('agendaList/', AgendaListAV.as_view(), name = 'agenda-list' ),
    path('view_agenda/<int:agendaID>' , AgendaDetailAV.as_view(), name='agenda-detail')

]
from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *



class ChildrenViewSet(ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = Children_Serializers

class PetsViewSet(ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = Pets_Serilaizers

class Narsing_House_ViewSet(ModelViewSet):
    queryset = Narsing_House.objects.all()
    serializer_class =Narsing_House_Serializers 
 
class HomelessViewSet(ModelViewSet):
    queryset = Homeless.objects.all()
    serializer_class =Homeless_Serializers 

class Children_House_ViewSet(ModelViewSet):
    queryset = Children_House.objects.all()
    serializer_class =Children_Hous_Serializer





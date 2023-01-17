from .models import *
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .permissions import IsAuthorOrReadOnly


class ChildrenViewSet(ModelViewSet):
    queryset = Children.objects.all()
    serializer_class = Children_Serializers
    permission_classes = [IsAuthorOrReadOnly]

class PetsViewSet(ModelViewSet):
    queryset = Pets.objects.all()
    serializer_class = Pets_Serilaizers
    permission_classes = [IsAuthorOrReadOnly]

class Narsing_House_ViewSet(ModelViewSet):
    queryset = Narsing_House.objects.all()
    serializer_class =Narsing_House_Serializers 
    permission_classes = [IsAuthorOrReadOnly]
    
class HomelessViewSet(ModelViewSet):
    queryset = Homeless.objects.all()
    serializer_class =Homeless_Serializers 
    permission_classes = [IsAuthorOrReadOnly]

class Children_House_ViewSet(ModelViewSet):
    queryset = Children_House.objects.all()
    serializer_class =Children_Hous_Serializer
    permission_classes = [IsAuthorOrReadOnly]




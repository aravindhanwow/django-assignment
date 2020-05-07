# Create your views here.
from rest_framework import viewsets
from .serializers import MemberSerializer
from .models import members

class MemberViewSet(viewsets.ModelViewSet):
    queryset = members.objects.all().order_by('Id')
    serializer_class = MemberSerializer
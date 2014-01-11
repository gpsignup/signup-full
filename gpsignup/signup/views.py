from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions

from signup.models import Location, Access_Key, Event, Person, Slot
from signup.serializers import LocationSerializer
from signup.serializers import AccessKeySerializer
from signup.serializers import EventSerializer
from signup.serializers import PersonSerializer
from signup.serializers import SlotSerializer
from signup.permissions import IsOwnerOrReadOnly

#-------------------------------------------------------------------------------
class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
#-------------------------------------------------------------------------------
class AccessKeyList(generics.ListCreateAPIView):
    queryset = Access_Key.objects.all()
    serializer_class = AccessKeySerializer

class AccessKeyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Access_Key.objects.all()
    serializer_class = AccessKeySerializer
#-------------------------------------------------------------------------------
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def pre_save(self, obj):
        obj.owner = self.request.user
#-------------------------------------------------------------------------------
class PersonList(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
#-------------------------------------------------------------------------------
class SlotList(generics.ListCreateAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

class SlotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer
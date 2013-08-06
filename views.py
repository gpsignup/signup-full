from signup.models import Location, Event, Person, Slot, Admin
from signup.serializers import LocationSerializer, EventSerializer, PersonSerializer, SlotSerializer
from rest_framework import generics
#-------------------------------------------------------------------------------
class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
#-------------------------------------------------------------------------------
class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
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
from django.forms import widgets
from rest_framework import serializers
from signup.models import Location, Event, Person, Slot, Admin

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'location_name')

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('id', 
        		  'event_name', 
    			  'locations',
    			  'description',
    			  'splash_url',
    			  'event_start_date',
    			  'event_end_date',
    			  'event_start_time',
    			  'event_end_time',
    			  'slot_duration',
    			  'default_slot_capacity',
    			  'event_signup_open_time',
    			  'event_signup_close_time',
    			  'event_created_timestamp',
    			  'event_modified_timestamp',
    			  'event_creator',
    			  'event_password',
    			  'is_private')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 
        		  'person_name',
    			  'email',
    			  'phone',
    			  'person_created_timestamp',
    			  'person_modified_timestamp',
    			  'person_code',
    			  'want_reminder')

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ('id', 
        		  'slot_date',
    			  'slot_start_time',
    			  'event',
    			  'people',
    			  'slot_location',
    			  'slot_capacity',
    			  'slot_created_timestamp',
    			  'slot_created_timestamp')
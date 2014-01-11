from django.forms import widgets
from django.contrib.auth.models import User

from rest_framework import serializers

from signup.models import Location, Access_Key, Event, Person, Slot

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ('id', 'location_name',)

class AccessKeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Access_Key
        fields = ('id', 'key_string', 'description',)

class EventSerializer(serializers.ModelSerializer):
    owner = serializers.Field(source='owner.username')

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
    			  'created_timestamp',
    			  'modified_timestamp',
    			  'event_creator',
    			  'event_password',
    			  'is_private',
                  'owner',)

class UserSerializer(serializers.ModelSerializer):
    events = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'events',)

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('id', 
        		  'person_name',
    			  'email',
    			  'phone',
    			  'created_timestamp',
    			  'modified_timestamp',
    			  'person_code',
    			  'want_reminder',)

class SlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        fields = ('id', 
        		  'slot_date',
    			  'slot_start_time',
                  'slot_end_time',
    			  'event',
    			  'people',
    			  'slot_location',
    			  'slot_capacity',
    			  'created_timestamp',
    			  'created_timestamp',)

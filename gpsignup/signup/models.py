from django.db import models
from django.contrib import admin
import datetime

# borrowed from "2 Scoops of Django"
class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self-    
    updating ``created`` and ``modified``. fields.
    """
    created_timestamp = models.DateTimeField(auto_now_add=True)
    modified_timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
#------------------------------------------------------------------------------- 
class Location(TimeStampedModel):
    location_name = models.CharField(max_length=100)
    
#-------------------------------------------------------------------------------
class Access_Key(TimeStampedModel):
    key_string = models.CharField(max_length=50)
    description = models.CharField(max_length=100)    
    
#------------------------------------------------------------------------------- 
class Event(TimeStampedModel):
    event_name = models.CharField(max_length=100)
    locations = models.ManyToManyField(Location, blank=True, null=True)
    access_keys = models.ManyToManyField(Access_Key, blank=True, null=True)
    description = models.CharField(max_length=100)    
    splash_url = models.URLField()
    event_start_date = models.DateField('event_start_date')
    event_end_date = models.DateField('event_end_date')
    event_start_time = models.TimeField('event_start_time')
    event_end_time = models.TimeField('event_end_time')
    slot_duration = models.PositiveIntegerField()
    default_slot_capacity = models.PositiveIntegerField()
    event_signup_open_time = models.DateTimeField()
    event_signup_close_time = models.DateTimeField()    
    event_creator = models.CharField(max_length=100)
    event_password = models.CharField(max_length=100)
    is_private = models.BooleanField() # False = signupee can't see others
    owner = models.ForeignKey('auth.User', related_name='events')
    
    class Meta:
        ordering = ('event_start_date', 'event_start_time',)

    def create_slots(self):    
        current_date = self.event_start_date
        current_time = self.event_start_time
        while current_date <= self.event_end_date:
            while current_time < self.event_end_time:
                for location in self.locations.all():
                    interval = datetime.timedelta(minutes=int(self.slot_duration))
                    interval_end = (datetime.datetime.combine(datetime.date(1,1,1),current_time) + interval).time()
                    self.slot_set.create(slot_day=current_day,
                                         slot_start_time=current_time,
                                         slot_end_time=interval_end,
                                         slot_capacity=self.default_slot_capacity,
                                         slot_location=location)
                current_time = interval_end                
            current_time = self.event_start_time
            current_day += datetime.timedelta(days=1)

    def __unicode__(self):
        return unicode(self.event_name)
    
    def save(self):        
        status = super(Event, self).save(*args, **kwargs)
        create_slots()
        return status

#-------------------------------------------------------------------------------
class Person(TimeStampedModel):
    person_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10, blank=True, null=True)    
    person_code = models.CharField(max_length=100, blank=True, null=True)
    want_reminder = models.BooleanField()

    def __unicode__(self):
        return unicode(self.person_name)

    def save(self):
        if not self.id:
            self.person_created_timestamp = datetime.datetime.today()
        self.person_modified_timestamp = datetime.datetime.today()
        return super(Person, self).save(*args, **kwargs)

#-------------------------------------------------------------------------------
class Slot(TimeStampedModel):
    slot_date = models.DateField('slot_date')
    slot_start_time = models.TimeField('slot_start_time')
    slot_end_time = models.TimeField('slot_end_time')
    event = models.ForeignKey(Event)
    people = models.ManyToManyField(Person, blank=True, null=True)
    slot_location = models.ForeignKey(Location)
    slot_capacity = models.PositiveIntegerField()    

    class Meta:
        ordering = ('slot_date', 'event', 'slot_start_time',)

    def __unicode__(self):
        return unicode(''.join([str(self.event),str(self.slot_day),str(self.slot_start_time),str(self.slot_end_time)]))

    def is_full(self):
        capacity = self.slot_capacity
        current_size = len(self.people.all())
        return current_size >= capacity
    
    def save(self):
        if not self.id:
            self.slot_created_timestamp = datetime.datetime.today()
        self.slot_modified_timestamp = datetime.datetime.today()
        return super(Slot, self).save(*args, **kwargs)

#-------------------------------------------------------------------------------
admin.site.register(Event)
admin.site.register(Slot)
admin.site.register(Person)
admin.site.register(Location)
admin.site.register(Access_Key)

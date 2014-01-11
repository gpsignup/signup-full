# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table(u'signup_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('location_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'signup', ['Location'])

        # Adding model 'Access_Key'
        db.create_table(u'signup_access_key', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('key_string', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'signup', ['Access_Key'])

        # Adding model 'Event'
        db.create_table(u'signup_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('event_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('splash_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('event_start_date', self.gf('django.db.models.fields.DateField')()),
            ('event_end_date', self.gf('django.db.models.fields.DateField')()),
            ('event_start_time', self.gf('django.db.models.fields.TimeField')()),
            ('event_end_time', self.gf('django.db.models.fields.TimeField')()),
            ('slot_duration', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('default_slot_capacity', self.gf('django.db.models.fields.PositiveIntegerField')()),
            ('event_signup_open_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('event_signup_close_time', self.gf('django.db.models.fields.DateTimeField')()),
            ('event_creator', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('event_password', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('is_private', self.gf('django.db.models.fields.BooleanField')()),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='events', to=orm['auth.User'])),
        ))
        db.send_create_signal(u'signup', ['Event'])

        # Adding M2M table for field locations on 'Event'
        m2m_table_name = db.shorten_name(u'signup_event_locations')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'signup.event'], null=False)),
            ('location', models.ForeignKey(orm[u'signup.location'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'location_id'])

        # Adding M2M table for field access_keys on 'Event'
        m2m_table_name = db.shorten_name(u'signup_event_access_keys')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('event', models.ForeignKey(orm[u'signup.event'], null=False)),
            ('access_key', models.ForeignKey(orm[u'signup.access_key'], null=False))
        ))
        db.create_unique(m2m_table_name, ['event_id', 'access_key_id'])

        # Adding model 'Person'
        db.create_table(u'signup_person', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('person_name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('person_code', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('want_reminder', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'signup', ['Person'])

        # Adding model 'Slot'
        db.create_table(u'signup_slot', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_timestamp', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('slot_date', self.gf('django.db.models.fields.DateField')()),
            ('slot_start_time', self.gf('django.db.models.fields.TimeField')()),
            ('slot_end_time', self.gf('django.db.models.fields.TimeField')()),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.Event'])),
            ('slot_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['signup.Location'])),
            ('slot_capacity', self.gf('django.db.models.fields.PositiveIntegerField')()),
        ))
        db.send_create_signal(u'signup', ['Slot'])

        # Adding M2M table for field people on 'Slot'
        m2m_table_name = db.shorten_name(u'signup_slot_people')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('slot', models.ForeignKey(orm[u'signup.slot'], null=False)),
            ('person', models.ForeignKey(orm[u'signup.person'], null=False))
        ))
        db.create_unique(m2m_table_name, ['slot_id', 'person_id'])


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table(u'signup_location')

        # Deleting model 'Access_Key'
        db.delete_table(u'signup_access_key')

        # Deleting model 'Event'
        db.delete_table(u'signup_event')

        # Removing M2M table for field locations on 'Event'
        db.delete_table(db.shorten_name(u'signup_event_locations'))

        # Removing M2M table for field access_keys on 'Event'
        db.delete_table(db.shorten_name(u'signup_event_access_keys'))

        # Deleting model 'Person'
        db.delete_table(u'signup_person')

        # Deleting model 'Slot'
        db.delete_table(u'signup_slot')

        # Removing M2M table for field people on 'Slot'
        db.delete_table(db.shorten_name(u'signup_slot_people'))


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'signup.access_key': {
            'Meta': {'object_name': 'Access_Key'},
            'created_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key_string': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'modified_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'signup.event': {
            'Meta': {'ordering': "('event_start_date', 'event_start_time')", 'object_name': 'Event'},
            'access_keys': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['signup.Access_Key']", 'null': 'True', 'blank': 'True'}),
            'created_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'default_slot_capacity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'event_creator': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'event_end_date': ('django.db.models.fields.DateField', [], {}),
            'event_end_time': ('django.db.models.fields.TimeField', [], {}),
            'event_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'event_password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'event_signup_close_time': ('django.db.models.fields.DateTimeField', [], {}),
            'event_signup_open_time': ('django.db.models.fields.DateTimeField', [], {}),
            'event_start_date': ('django.db.models.fields.DateField', [], {}),
            'event_start_time': ('django.db.models.fields.TimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_private': ('django.db.models.fields.BooleanField', [], {}),
            'locations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['signup.Location']", 'null': 'True', 'blank': 'True'}),
            'modified_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': u"orm['auth.User']"}),
            'slot_duration': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'splash_url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'signup.location': {
            'Meta': {'object_name': 'Location'},
            'created_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'modified_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        u'signup.person': {
            'Meta': {'object_name': 'Person'},
            'created_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'person_code': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'person_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'want_reminder': ('django.db.models.fields.BooleanField', [], {})
        },
        u'signup.slot': {
            'Meta': {'ordering': "('slot_date', 'event', 'slot_start_time')", 'object_name': 'Slot'},
            'created_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['signup.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'people': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['signup.Person']", 'null': 'True', 'blank': 'True'}),
            'slot_capacity': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'slot_date': ('django.db.models.fields.DateField', [], {}),
            'slot_end_time': ('django.db.models.fields.TimeField', [], {}),
            'slot_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['signup.Location']"}),
            'slot_start_time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['signup']
# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Course'
        db.create_table(u'courses_course', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'courses', ['Course'])

        # Adding model 'Lecture'
        db.create_table(u'courses_lecture', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('number', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Course'])),
            ('slides', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('video', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'courses', ['Lecture'])

        # Adding model 'Exercise'
        db.create_table(u'courses_exercise', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('number', self.gf('django.db.models.fields.PositiveSmallIntegerField')()),
            ('lecture', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Lecture'])),
            ('initial_code', self.gf('django.db.models.fields.TextField')()),
            ('hint', self.gf('django.db.models.fields.TextField')()),
            ('unit_test', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'courses', ['Exercise'])


    def backwards(self, orm):
        # Deleting model 'Course'
        db.delete_table(u'courses_course')

        # Deleting model 'Lecture'
        db.delete_table(u'courses_lecture')

        # Deleting model 'Exercise'
        db.delete_table(u'courses_exercise')


    models = {
        u'courses.course': {
            'Meta': {'ordering': "['title']", 'object_name': 'Course'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'courses.exercise': {
            'Meta': {'ordering': "['number']", 'object_name': 'Exercise'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'hint': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_code': ('django.db.models.fields.TextField', [], {}),
            'lecture': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Lecture']"}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'unit_test': ('django.db.models.fields.TextField', [], {})
        },
        u'courses.lecture': {
            'Meta': {'ordering': "['number']", 'object_name': 'Lecture'},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Course']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'number': ('django.db.models.fields.PositiveSmallIntegerField', [], {}),
            'slides': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'video': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['courses']
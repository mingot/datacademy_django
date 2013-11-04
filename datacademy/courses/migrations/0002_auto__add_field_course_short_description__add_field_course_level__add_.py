# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Course.short_description'
        db.add_column(u'courses_course', 'short_description',
                      self.gf('django.db.models.fields.CharField')(default='TBD.', max_length=150),
                      keep_default=False)

        # Adding field 'Course.level'
        db.add_column(u'courses_course', 'level',
                      self.gf('django.db.models.fields.CharField')(default='beginner', max_length=20),
                      keep_default=False)

        # Adding field 'Course.date'
        db.add_column(u'courses_course', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 11, 2, 0, 0)),
                      keep_default=False)

        # Adding field 'Lecture.video_duration'
        db.add_column(u'courses_lecture', 'video_duration',
                      self.gf('django.db.models.fields.IntegerField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Course.short_description'
        db.delete_column(u'courses_course', 'short_description')

        # Deleting field 'Course.level'
        db.delete_column(u'courses_course', 'level')

        # Deleting field 'Course.date'
        db.delete_column(u'courses_course', 'date')

        # Deleting field 'Lecture.video_duration'
        db.delete_column(u'courses_lecture', 'video_duration')


    models = {
        u'courses.course': {
            'Meta': {'ordering': "['title']", 'object_name': 'Course'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
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
            'video': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'video_duration': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['courses']
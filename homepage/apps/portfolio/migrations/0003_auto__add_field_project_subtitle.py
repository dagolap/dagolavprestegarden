# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Project.subtitle'
        db.add_column(u'portfolio_project', 'subtitle',
                      self.gf('django.db.models.fields.CharField')(max_length=75, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Project.subtitle'
        db.delete_column(u'portfolio_project', 'subtitle')


    models = {
        u'portfolio.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('filebrowser.fields.FileBrowseField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'sort_order': ('django.db.models.fields.SmallIntegerField', [], {}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '75', 'null': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['portfolio']
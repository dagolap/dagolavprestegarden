# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Comment.target'
        db.add_column(u'comments_comment', 'target',
                      self.gf('django.db.models.fields.URLField')(default='', max_length=400, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Comment.target'
        db.delete_column(u'comments_comment', 'target')


    models = {
        u'comments.comment': {
            'Meta': {'object_name': 'Comment'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'author_website': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'comment': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'target': ('django.db.models.fields.URLField', [], {'max_length': '400', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '75'})
        }
    }

    complete_apps = ['comments']
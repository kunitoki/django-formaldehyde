from __future__ import unicode_literals
import re
import itertools
from django import forms
#from django.forms.models import ModelFormOptions
#from django.db.models import Q
#from django.contrib.auth import get_user_model
#from django.utils.translation import ugettext_lazy as _
from django.utils import six

from .conf import settings


#==============================================================================
# Inspiration: http://schinckel.net/2013/06/14/django-fieldsets/

#_old_init = ModelFormOptions.__init__
#def _new_init(self, options=None):
#    _old_init(self, options)
#    self.fieldsets = getattr(options, 'fieldsets', None)
#ModelFormOptions.__init__ = _new_init


#==============================================================================
class Fieldline(object):
    def __init__(self, form, fieldline, layoutline):
        self.form = form  # A django.forms.Form instance
        if not hasattr(fieldline, "__iter__") or isinstance(fieldline, six.text_type):
            self.fields = [fieldline]
        else:
            self.fields = fieldline
        if not hasattr(layoutline, "__iter__") or isinstance(fieldline, six.integer_types):
            self.layout = [layoutline]
        else:
            self.layout = layoutline

        self.layout_cols = settings.GRID_COLUMN_NUMBER - settings.FIRST_LABEL_COLUMN_SIZE

    def __iter__(self):
        layout_cols = self.layout_cols
        if len(self.fields) > 1:
            layout_cols = int(layout_cols / len(self.fields) - 1)

        for field, layout in itertools.izip_longest(self.fields,
                                                     self.layout,
                                                     fillvalue=None):
            yield self.form[field], layout if layout else layout_cols


#==============================================================================
class Fieldset(object):
    def __init__(self, form, legend, fields, layout, description, classes):
        self.form = form
        self.legend = legend
        self.fields = fields
        self.layout = layout
        self.description = description
        self.classes = classes

    def __iter__(self):
        for fieldline, layoutline in itertools.izip_longest(self.fields,
                                                             self.layout,
                                                             fillvalue=None):
            yield Fieldline(
                form=self.form,
                fieldline=fieldline,
                layoutline=layoutline
            )


#==============================================================================
class FieldsetForm(object):
    def fieldsets(self):
        meta = getattr(self, 'MetaForm', None)
        if not meta or not meta.fieldsets:
            return

        for legend, data in meta.fieldsets:
            yield Fieldset(
                form=self,
                legend=legend,
                fields=data.get('fields', tuple()),
                layout=data.get('layout', tuple()),
                description=data.get('description', ''),
                classes=data.get('classes', '')
            )

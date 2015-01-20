from __future__ import unicode_literals
import re
import itertools
from django import forms
from django.utils import six

from .conf import settings


#==============================================================================
class Fieldline(object):
    def __init__(self, form, fieldline, layoutline):
        self.form = form
        if not hasattr(fieldline, "__iter__") or isinstance(fieldline, six.text_type):
            self.fields = [fieldline]
        else:
            self.fields = fieldline
        if not hasattr(layoutline, "__iter__") or isinstance(fieldline, six.integer_types):
            self.layout = [layoutline]
        else:
            self.layout = layoutline

        self.layout_cols = settings.GRID_COLUMN_NUMBER - settings.FIRST_LABEL_COLUMN_SIZE
        if len(self.fields) > 1:
            self.layout_cols = int(self.layout_cols / len(self.fields) - 1)

        self.__index = 0
        self.__len = max(len(self.fields), len(self.layout))

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.__index >= self.__len:
            raise StopIteration()

        field = self.fields[self.__index] if self.__index < len(self.fields) else None
        if field:
            field = self.form[field]

        layout = self.layout[self.__index] if self.__index < len(self.layout) else None
        if not layout:
            layout = self.layout_cols
        
        self.__index += 1

        return field, layout


#==============================================================================
class Fieldset(object):
    def __init__(self, form, legend, fields, layout, description, classes):
        self.form = form
        self.legend = legend
        self.fields = fields
        self.layout = layout
        self.description = description
        self.classes = classes

        self.__index = 0
        self.__len = max(len(self.fields), len(self.layout))

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.__index >= self.__len:
            raise StopIteration()

        fieldline = Fieldline(
            form=self.form,
            fieldline=self.fields[self.__index] if self.__index < len(self.fields) else None,
            layoutline=self.layout[self.__index] if self.__index < len(self.layout) else None,
        )

        self.__index += 1

        return fieldline


#==============================================================================
class FieldsetForm(object):
    def fieldsets(self):
        assert(isinstance(self, forms.Form))
        
        meta = getattr(self, 'MetaForm', None)
        if not meta or not meta.fieldsets:
            return

        for legend, data in meta.fieldsets:
            yield Fieldset(
                form=self, # A django.forms.Form instance
                legend=legend,
                fields=data.get('fields', tuple()),
                layout=data.get('layout', tuple()),
                description=data.get('description', ''),
                classes=data.get('classes', '')
            )

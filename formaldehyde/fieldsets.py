from __future__ import unicode_literals
from django import forms
from django.utils import six

from .conf import settings


#==============================================================================
class Fieldline(object):
    def __init__(self, form, fields, layout, labels):
        self.form = form

        if not hasattr(fields, "__iter__") or isinstance(fields, six.text_type):
            self.fields = [fields]
        else:
            self.fields = fields

        if not hasattr(layout, "__iter__") or isinstance(layout, six.integer_types):
            self.layout = [layout]
        else:
            self.layout = layout

        if not hasattr(labels, "__iter__") or isinstance(labels, six.integer_types):
            self.labels = [labels]
        else:
            self.labels = labels

        self.__index = 0
        self.__len = len(self.fields)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.__index >= self.__len:
            raise StopIteration()

        field = self.form[self.fields[self.__index]]

        field_size = self.layout[self.__index] if self.__index < len(self.layout) else None
        if field_size is None:
            field_size = settings.DEFAULT_FIELD_COLUMN_SIZE

        label_size = self.labels[self.__index] if self.__index < len(self.labels) else None
        if label_size is None:
            label_size = settings.FIRST_LABEL_COLUMN_SIZE if self.__index == 0 else settings.DEFAULT_LABEL_COLUMN_SIZE

        self.__index += 1

        return field, field_size, label_size


#==============================================================================
class Fieldset(object):
    def __init__(self, form, legend, description, classes, fields, layout, labels):
        self.form = form
        self.legend = legend
        self.description = description
        self.classes = classes
        self.fields = fields
        self.layout = layout
        self.labels = labels

        self.__index = 0
        self.__len = len(self.fields)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next()

    def next(self):
        if self.__index >= self.__len:
            raise StopIteration()

        fieldline = Fieldline(
            form=self.form,
            fields=self.fields[self.__index] if self.__index < len(self.fields) else None,
            layout=self.layout[self.__index] if self.__index < len(self.layout) else None,
            labels=self.labels[self.__index] if self.__index < len(self.labels) else None,
        )

        self.__index += 1

        return fieldline


#==============================================================================
class FieldsetFormMixin(object):
    def __init__(self, *args, **kwargs):
        super(FieldsetFormMixin, self).__init__(*args, **kwargs)

        assert(isinstance(self, forms.BaseForm))

        self.meta = getattr(self, 'MetaForm', None)

        self.fieldsets = None
        if self.meta and self.meta.fieldsets:
            self.fieldsets = self._fieldsets

    def _fieldsets(self):
        if self.meta and self.meta.fieldsets:
            for legend, data in self.meta.fieldsets:
                yield Fieldset(
                    form=self,
                    legend=legend,
                    description=data.get('description', ''),
                    classes=data.get('classes', ''),
                    fields=data.get('fields', tuple()),
                    layout=data.get('layout', tuple()),
                    labels=data.get('labels', tuple()),
                )

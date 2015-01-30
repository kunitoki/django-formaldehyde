from __future__ import unicode_literals
from django import forms
from django.utils import six


#==============================================================================
class StripWhitespaceFormMixin(object):
    """
    Strip whitespace automatically in all form fields after a full_clean call
    """

    def strip_whitespace_from_data(self):
        assert(isinstance(self, forms.BaseForm))

        if hasattr(self, 'data') and self.data:
            data = self.data.copy()
            if hasattr(self.data, 'lists'):
                for key, values in self.data.lists():
                    new_values = []
                    for v in values:
                        if isinstance(v, six.text_type):
                            v = v.strip()
                        new_values.append(v)
                    data.setlist(key, new_values)
            else:
                for key, value in six.iteritems(self.data):
                    if isinstance(value, six.text_type):
                        value = value.strip()
                    data[key] = value
            self.data = data

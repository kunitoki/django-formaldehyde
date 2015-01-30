from __future__ import unicode_literals
from django import forms


#==============================================================================
class ReadonlyFormMixin(object):
    """
    Mixin class to enable setting readonly of the form at runtime
    """

    def set_readonly(self, is_readonly=True):
        assert(isinstance(self, forms.BaseForm))

        for field in self.fields:
            self.fields[field].is_readonly = is_readonly

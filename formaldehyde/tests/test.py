import django
#from django.conf import settings
#from django.core.urlresolvers import reverse
#from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.contrib.contenttypes.models import ContentType
from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.test.utils import override_settings
from django.utils import six

from formaldehyde.conf import settings
from formaldehyde.fieldsets import FieldsetForm


#==============================================================================
class TestForm(FieldsetForm, forms.Form):
    first_name = forms.CharField(label='First name', max_length=100)
    middle_name = forms.CharField(label='Middle name', max_length=150)
    last_name = forms.CharField(label='Last name', max_length=200)
    street = forms.CharField(label='Street name', max_length=200)

    class Meta:
        fields = ('first_name', 'middle_name', 'last_name', 'street')

    class MetaForm:
        fieldsets = (
            (None, {
                'fields': (
                    ('first_name', 'middle_name'),
                    'last_name',
                ),
                'layout': (
                    (4, 6),
                    2
                ),
                'classes': 'form-control'
            }),
            ('Address', {
                'fields': (
                    'street',
                ),
            }),
        )

    def __init__(self, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)


#==============================================================================
class FormalehydeTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()

    def tearDown(self):
        pass

    def test_fieldset_form(self):
        form = TestForm()

        self.assertIsNotNone(form.fieldsets)

        fieldset01 = six.next(form.fieldsets())
        self.assertIsNone(fieldset01.legend)
        self.assertEqual(fieldset01.description, '')
        self.assertEqual(fieldset01.classes, 'form-control')

        fieldset01_line01 = six.next(fieldset01)
        fieldset01_line01_field01, fieldset01_line01_layout01 = six.next(fieldset01_line01)
        self.assertEqual('first_name', fieldset01_line01_field01.name)
        self.assertEqual(4, fieldset01_line01_layout01)
        fieldset01_line01_field02, fieldset01_line01_layout02 = six.next(fieldset01_line01)
        self.assertEqual('middle_name', fieldset01_line01_field02.name)
        self.assertEqual(6, fieldset01_line01_layout02)

        fieldset01_line02 = six.next(fieldset01)
        fieldset01_line02_field01, fieldset02_line01_layout01 = six.next(fieldset01_line02)
        self.assertEqual('street', fieldset01_line02_field01.name)
        self.assertEqual(fieldset01_line02.layout_cols, fieldset01_line02_layout01)
        
        #for fieldset in form.fieldsets():
        #    print(fieldset.legend)
        #    print(fieldset.description)
        #    print(fieldset.classes)
        #    for fieldline in fieldset:
        #        for field, field_size in fieldline:
        #            print("%s (%s)" % (field, field_size))

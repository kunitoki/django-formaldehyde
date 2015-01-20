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
                'layout': (
                    12,
                )
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

        f01 = form.fieldsets().next()
        self.assertIsNone(f01.legend)
        self.assertEqual(f01.description, '')
        self.assertEqual(f01.classes, 'form-control')
        
        #for fieldset in form.fieldsets():
        #    print(fieldset.legend)
        #    print(fieldset.description)
        #    print(fieldset.classes)
        #    for fieldline in fieldset:
        #        for field, field_size in fieldline:
        #            print("%s (%s)" % (field, field_size))

.. include:: ../README.rst


Getting started
===============

1. You can get Django Formaldehyde by using pip::

    pip install django-formaldehyde

2. You will need to add the ``'formaldehyde'`` application to the ``INSTALLED_APPS`` setting of your Django project ``settings.py`` file.::

    INSTALLED_APPS = (
        ...

        'formaldehyde',
    )


Configuration
=============

It is possible to configure by using in ``settings.py``.::

    FORMALDEHYDE_SETTINGS = {
        'GRID_COLUMN_NUMBER': 12,
        'LABEL_COLUMN_SIZE': 1,
        'FIRST_LABEL_COLUMN_SIZE': 2
    }


Classes and Mixins
==================

django-formaldehyde provides a series of django.forms.Form mixins to help the handling of forms in applications.


FieldsetFormMixin
-----------------

The mixin add fieldsets with fieldlines and layout support to forms. It adds the
inner class MetaForm where you can specify your fieldsets configuration.::

    from django import forms
    from formaldehyde.fieldsets import FieldsetFormMixin

    class ExampleFieldsetForm(FieldsetFormMixin, forms.Form):
        first_name = forms.CharField(label='First name', max_length=100)
        last_name = forms.CharField(label='Last name', max_length=100)
        nick_name = forms.CharField(label='Nick name', max_length=100)
        avatar = forms.IntegerField()
        photo = forms.ImageField()

        class Meta:
            fields = '__all__'

        class MetaForm:
            fieldsets = (
                (None, {
                    'fields': (
                        ('first_name', 'last_name'),
                        'nick_name',
                    ),
                    'layout': (
                        (4, 6),
                        2
                    ),
                    'classes': 'form-control'
                }),
                ('Social', {
                    'fields': (
                        'avatar',
                        'photo'
                    )
                }),
            )


ReadonlyFormMixin
-----------------


StripWhitespaceFormMixin
------------------------


Support
=======

* Github: Use `django-formaldehyde github issues <https://github.com/kunitoki/django-formaldehyde/issues>`_, if you have any problems using Django Formaldehyde.


.. include:: ../CHANGELOG.rst

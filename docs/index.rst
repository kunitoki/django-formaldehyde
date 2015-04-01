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
        'DEFAULT_FIELD_COLUMN_SIZE': 1,
        'DEFAULT_LABEL_COLUMN_SIZE': 1,
        'FIRST_LABEL_COLUMN_SIZE': 2
    }


Classes and Mixins
==================

django-formaldehyde provides a series of django.forms.Form mixins to help the handling of forms in applications.


FieldsetFormMixin
-----------------

The mixin add fieldsets with fieldlines to forms. It also add the concept of layout
of the fields, so it is possible to place fields and labels in the grid space.
Everything is used inside an inner class called MetaForm::

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
                    'labels': (
                        (2, 1),
                        1
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


An example template (for bootstrap grid system) for rendering the form looks like::

    {% if form.fieldsets %}
        {% for fieldset in form.fieldsets %}
            <fieldset class="{{ fieldset.classes }}">
                {% if fieldset.legend %}
                    <legend>{{ fieldset.legend }}</legend>
                {% endif %}
                {% if fieldset.description %}
                    <p class="description">{{ fieldset.description }}</p>
                {% endif %}
                {% for fieldline in fieldset %}
                    <div class="form-group">
                    {% for field, layout in fieldline %}
                        {% if field.is_hidden %}
                            {{ field }}
                        {% else %}
                            <label class="col-sm-{% if forloop.first %}2{% else %}1{% endif %} control-label">
                                {{ field.label }}
                            </label>
                            <div class="col-sm-{{ layout|default:10 }}">
                                {{ field }}
                            </div>
                        {% endif %}
                    {% endfor %}
                    </div>
                {% endfor %}
            </fieldset>
        {% endfor %}
    {% else %}
        {% for hidden in form.hidden_fields %}
            {{ hidden }}
        {% endfor %}
        {% for field in form.visible_fields %}
            <div class="form-group{% if field.errors %} has-error{% endif %}">
                <label class="col-sm-{% if forloop.first %}2{% else %}1{% endif %} control-label">
                    {{ field.label }}
                </label>
                <div class="col-sm-{{ field_size|default:10 }}">
                    {{ field }}
                </div>
            </div>
        {% endfor %}
    {% endif %}


ReadonlyFormMixin
-----------------


StripWhitespaceFormMixin
------------------------


Support
=======

* Github: Use `django-formaldehyde github issues <https://github.com/kunitoki/django-formaldehyde/issues>`_, if you have any problems using Django Formaldehyde.


.. include:: ../CHANGELOG.rst

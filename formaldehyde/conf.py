import sys
from django.conf import settings as django_settings
from django.utils.functional import cached_property as settings_property


#==============================================================================
# Do not cache properties when in test mode
if 'test' in sys.argv:
    settings_property = property


#==============================================================================
# Helper class for lazy settings
class LazySettingsDict(object):

    """ Internal properties """
    @settings_property
    def settings(self):
        return getattr(django_settings, 'FORMALDEHYDE_SETTINGS', {})

    def get_property(self, name, default):
        return self.settings.get(name, default)

    def get_property_fallback(self, name, default):
        return self.settings.get(name, getattr(django_settings, name, default))


    """ Global setting variables """
    @settings_property
    def GRID_COLUMN_NUMBER(self):
        return self.get_property('GRID_COLUMN_NUMBER', 12)

    @settings_property
    def LABEL_COLUMN_SIZE(self):
        return self.get_property('LABEL_COLUMN_SIZE', 1)

    @settings_property
    def FIRST_LABEL_COLUMN_SIZE(self):
        return self.get_property('FIRST_LABEL_COLUMN_SIZE', 2)


#==============================================================================
settings = LazySettingsDict()

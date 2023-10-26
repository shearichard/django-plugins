from django.dispatch import Signal

#################################################################
# Apparently the signature of Signal has changed in >= Django 4.0 
# so that 'providing_args is no longer needed. Most sources say
# you can just remove the argument, others suggest you do this
#
#  django_plugin_disabled = Signal("plugin")
#
# At least initially I'm going with straightforward removal
#
#################################################################
#django_plugin_disabled = Signal(providing_args=["plugin"])
#django_plugin_enabled = Signal(providing_args=["plugin"])
django_plugin_disabled = Signal()
django_plugin_enabled = Signal()

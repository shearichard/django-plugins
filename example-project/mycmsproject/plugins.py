from __future__ import absolute_import

from django.urls import path, reverse

from djangoplugins.point import PluginPoint

import mycmsproject.views


class ContentType(PluginPoint):
    urls = [
        path(r'^$', mycmsproject.views.content_list, name='content-list'),
        path(r'^create/$', mycmsproject.views.content_create,
            name='content-create')
    ]

    instance_urls = [
        path(r'^$', mycmsproject.views.content_read, name='content-read')
    ]

    def get_list_url(self):
        return reverse('content-list')

    def get_create_url(self):
        return reverse('content-create')

    def get_read_url(self, content):
        return reverse('content-read', args=[content.pk])

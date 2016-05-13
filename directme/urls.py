from django.conf.urls import url

from . import views


urlpatterns = [

    url(r'^$', 'directme.views.manage_work', name='manage_work'),
    url(r'^client/$', 'directme.views.manage_clients', name='manage_clients'),
    url(r'^driver/$', 'directme.views.manage_driver', name='manage_driver'),
    url(r'^draw/$', 'directme.views.draw_tree', name='draw_tree'),
]

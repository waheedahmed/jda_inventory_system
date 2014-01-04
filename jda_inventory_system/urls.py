from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
from inventory_app.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', jda_login, name="login"),
    url(r'^logout/$', logout_user, name='logout'),
    url(r'^home/$', home, name="home"),
    url(r'^manage-admins/$', manage_admins, name="manage-admins"),
    url(r'^user/add/$', add_user, name="add-user"),
    url(r'^status/(\d+)/(.*)$', set_status, name="set-status"),
    url(r'^equipment/add/$', add_equipment, name="add-equipment"),
    url(r'^equipment/(.*)/$', equipment, name="equipment"),
    url(r'^part/add/(.*)/$', add_part, name="add-part"),
    url(r'^part/(.*)/$', part, name="part"),
    url(r'^edit/part/(.*)/$', edit_part, name="edit-part"),
    url(r'^history/part/(.*)/$', issue_history, name="part"),
    url(r'^issue-part/(.*)/$', issue_part, name="issue-part"),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('',

                            (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                            )
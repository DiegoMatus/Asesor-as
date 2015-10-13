from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'Asesorías'
urlpatterns = patterns ('coafid.views',
    url(r'^$', 'index',			name="index"),
    url(r'^(?P<student>[\w|\W]+)/$',									'student_view',		name='student'),
    url(r'^(?P<project>[\w|\W]+)/$',									'project_view',		name='project'),
    url(r'^(?P<student>[\w|\W]+)/(?P<advisory>[\w|\W]+)/$',				'advisory_view',		name='advisory'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 	#Servir estáticos en desarrollo
from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from . import views
from articles import views as article_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'about/$', views.about),
    url(r'accounts/', include('accounts.urls', namespace='accounts')),
    url(r'articles/', include('articles.urls', namespace='articles')),
    url(r'$', article_views.article_list, name='home'),
]   

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    # url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^admin/', admin.site.urls),
    url(r'^core/', include('core.urls')),
    url(r'^slack/', include('slack.urls', namespace="slack"))
]




urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

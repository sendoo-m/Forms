from django.contrib import admin
from django.urls import path, include
from App import views
from django.conf import settings
from Candidates import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    # path('jet/', include('jet.urls', 'jet')),  # Django JET URLS not work with me
    # path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS not work with me
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('catalog/', include('catalog.urls')),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView

urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]
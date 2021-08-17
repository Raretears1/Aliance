from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import test_view, contacts, bucha, irpin, stoyanka, gost, vorzel, kyiv

urlpatterns = [
    path('', test_view, name='main'),
    path('contacts/', contacts, name='contacts'),
    path('bucha/', bucha, name='bucha'),
    path('irpin/', irpin, name='irpin'),
    path('stoyanka/', stoyanka, name='stoyanka'),
    path('gostomel/', gost, name='gostomel'),
    path('vorzel/', vorzel, name='vorzel'),
    path('kyiv/', kyiv, name='kyiv')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

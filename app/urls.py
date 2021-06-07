from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.views import BirthdayCalendarView

app_name = 'aniversarios'

urlpatterns = [
    path('aniversarios', BirthdayCalendarView.as_view(), name="aniversarios_list"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATICFILES_DIRS[0], document_root=settings.STATICFILES_DIRS[0])

from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app.views import BirthdayCalendarView, BirthdayCalendarDelete

app_name = 'aniversarios'

urlpatterns = [
    path('', BirthdayCalendarView.as_view(), name="aniversarios_list"),
    path('birthday/delete/<int:pk>', BirthdayCalendarDelete.as_view(), name="aniversario_delete")
]

if settings.DEBUG:
    urlpatterns += static(settings.STATICFILES_DIRS[0], document_root=settings.STATICFILES_DIRS[0])

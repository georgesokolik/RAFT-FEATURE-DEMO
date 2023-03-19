from django.urls import path
from chatbot import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.views.generic.base import TemplateView


urlpatterns = [
    path('chatbot/', views.ChatbotView.as_view(), name='chatbot'),
    path('summary_report/', views.summary_report, name='summary_report'),
]

urlpatterns += staticfiles_urlpatterns()
#urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
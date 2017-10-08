from django.conf.urls import url
from core.views import RegisterCustomerView

urlpatterns = (
    url(r'^register_customer/$', RegisterCustomerView.as_view(), name='register_customer'),
)

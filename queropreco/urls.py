from django.conf.urls import url, include
from django.contrib import admin
from core.views import home, RegisterCustomerView


urlpatterns = (
    url(r'^$', home, name='home'),
    url(r'^account/', include('account.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^customer/$', view=RegisterCustomerView.as_view(), name='customer'),
    url(r'^customer/', include('core.urls')),
)

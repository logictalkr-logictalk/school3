from django.conf.urls import url
from regapp.views import home,Reg,emp

app_name = 'application'

urlpatterns = [
    url(r'^$', home.as_view()),
    url(r'^Reg$',Reg.as_view()),
    url(r'^emp$',emp.as_view()),


]
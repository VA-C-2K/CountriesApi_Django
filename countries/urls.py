from django.conf.urls import  url
from countries import  views

urlpatterns = [
    url(r'^api/countries$', views.countries_list),
    url(r'^api/countries/(?P<pk>[0-9]+)$',views.countries_detail)
    # in Python regular expression,the syntax for named regular expression group is(?P<pk>[0-9]+),
    #where name is  the name of the  group and pattern is pattern is some  pattern  to match
]

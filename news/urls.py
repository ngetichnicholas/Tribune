from django.conf.urls import url
from django.urls import re_path,path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static

urlpatterns =[
    url(r'^$', views.news_today, name = 'newsToday'),
    # path('accounts/register/',views.register,name='register'),
    path('accounts/login',auth_views.LoginView.as_view(template_name = 'registration/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'registration/logout.html'),name='logout'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_news,name = 'pastNews'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^article/(\d+)',views.article,name ='article'),
    url('new/article', views.new_article, name='new-article'),
    url(r'^accounts/profile', views.profile,name='user-profile'),
    url(r'^ajax/newsletter/$', views.newsletter, name='newsletter'),
    url(r'^api/merch/$', views.MerchList.as_view()),
    url(r'api/merch/merch-id/(?P<pk>[0-9]+)/$',
        views.MerchDescription.as_view())


]

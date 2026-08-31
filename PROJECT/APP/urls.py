from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create/', views.product_create, name='product_create'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('change-password/', views.password_change, name='password_change'),
    path('product/<int:product_id>/', views.product_detail, name='product'),
    path('product/<int:product_id>/update/', views.product_update, name='product_update'),
    path('product/<int:product_id>/delete/', views.product_delete, name='product_delete'),
    path('user-dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin_dashboard/', views.product_list, name='admin_dashboard'),
    path('pay/', views.make_payement, name='pay')
]
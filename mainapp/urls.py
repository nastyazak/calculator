from django.urls import path
from rest_framework.routers import SimpleRouter
from django.contrib.auth.views import LogoutView
from django_pdfkit import PDFView
from . import views
from .views import *

router = SimpleRouter()
router.register('api/categories', CategoryView)
router.register('api/works', TypeWorkView)

urlpatterns = [
    path('', views.render_app, name='calculation'),
    path('api/order/', views.OrderList, name='order'),
    path('thanks/', views.render_thanks, name='thanks'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('signup/', views.UserRegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('estimate/', render_estimate, name='estimate'),
    path('pdf/', GeneratePdf.as_view(), name='generate_pdf_estimate'),
    path('pdf_download/', DownloadPdf.as_view(), name='download_pdf_estimate'),
    path('category/', render_category, name='admin_category'),
    path('work/', render_work, name='admin_work'),
    path('add_category/', CategoryCreateView.as_view(), name='add_category'),
    path('<slug:pk>/edit_category/', CategoryUpdateView.as_view(), name='update_category'),
    path('<slug:pk>/remove_category/', CategoryDeleteView.as_view(), name='delete_category'),
    path('add_work/', TypeWorkCreateView.as_view(), name='add_work'),
    path('<slug:pk>/edit_work/', TypeWorkUpdateView.as_view(), name='update_work'),
    path('<slug:pk>/remove_work/', TypeWorkDeleteView.as_view(), name='delete_work'),
]

urlpatterns += router.urls

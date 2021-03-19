from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('about_us/', views.about, name="about" ),
    path('contact_us/', views.contact, name="contact" ),
    path('portfolio/', views.portfolio, name="portfolio" ),
    path('photography/', views.photography, name="photography" ),
    path('photography/<str:category>/', views.gallery, name="gallery" ),
    path('web_development/', views.web_development, name="web_developement" ),
    path('app_development/', views.app_development, name="app_developement" ),
    path('digital_marketing/', views.digital_marketing, name="digital_marketing" ),
    path('web_&_graphics_designing/', views.graphics, name="web_&_graphics_designing" ),
    path('budget/', views.budget, name="budget" ),
    path('budget_app/', views.budget_app, name="budget" ),
    path('budget_web_and_app/', views.budget_web_and_app, name="budget" ),
    path('faqs/', views.faq, name="faqs" ),
]

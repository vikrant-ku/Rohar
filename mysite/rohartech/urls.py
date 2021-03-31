from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('about_us', views.about, name="about" ),
    path('contact_us', views.contact, name="contact" ),
    path('portfolio', views.portfolio, name="portfolio" ),
    path('photography', views.photography, name="photography" ),
    path('photography/<str:category>', views.gallery, name="gallery" ),
    path('web-development', views.web_development, name="web_developement" ),
    path('app-development', views.app_development, name="app_developement" ),
    path('digital-marketing', views.digital_marketing, name="digital_marketing" ),
    path('web-&-graphics-designing', views.graphics, name="web_&_graphics_designing" ),
    path('budget', views.budget, name="budget" ),
    path('budget-app', views.budget_app, name="budget-app" ),
    path('budget-web-and-app', views.budget_web_and_app, name="budget-web-and-app" ),
    path('budget-dm', views.budget_dm, name="budget-dm" ),
    path('faqs', views.faq, name="faqs" ),
]

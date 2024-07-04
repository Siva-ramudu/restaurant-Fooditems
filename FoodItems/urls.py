from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.homepage),
    path('add/',views.addItem,name="addmenuitem"),
    path('menu/',views.menu ,name="menu"),
    path('delete/<id>',views.deleteItem,name="deleteitem"),
    path('edit/<id>',views.editItem,name="edititem"),
    path('signup/',views.signup,name="signup"),
    path('signin/',views.signin, name='signin'),
    path('logout/',views.signout,name='logout')
] 
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


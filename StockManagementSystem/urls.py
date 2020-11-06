"""StockManagementSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from API import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register("vendor",views.VendorViewSet,basename="vendor")
router.register("item",views.ItemViewSet,basename="item")
router.register("stock",views.StockViewSet,basename="stock")
router.register("sale",views.SaleViewSet,basename="sale")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(router.urls)),
    path('api/gettoken/',TokenObtainPairView.as_view(),name="gettoken"), #path for getting api token
    path('api/refreshtoken/',TokenRefreshView.as_view(),name="refreshtoken"),
    path('account/',include('Account.urls')),
    path('',include('Frontend.urls'))
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

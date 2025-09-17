
from django.urls import include, path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


from ecom.api_views import *

# router = DefaultRouter()

# ecom-------
from ecommerce.urls import router
router.register(r'procuct/products',ProductViewSet,basename='product')
router.register(r'procuct/tag',TagViewSet,basename='tag')
router.register(r'procuct/catogories',ProductCatagoriesViewSet,basename='catogories')



urlpatterns = [
    # ------------------jwt------------
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    #-----------------customUrl---------------
    path('api/', include(router.urls)),
    
]

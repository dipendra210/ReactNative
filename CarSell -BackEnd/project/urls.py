
from django.contrib import admin
from django.urls import path
from api.views import BrandList, RegisterAPIView, GetPost, PostListByBrand, ViewsCount,LatestPosts, MostViewed, ModelListByBrand, RegularPost, SpecialPost, CreateRequest, UserPosts, SavePushToken
from django.conf.urls.static import static
from django.conf import settings
from api import views
from rest_framework_jwt.views import obtain_jwt_token

from website import views as web_views
# from graphene_django.views import GraphQLView
# from schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', obtain_jwt_token, name='login'),

    path('brands/', BrandList.as_view(), name='brand-list'), 
    path('models/brand/<int:brand_id>', ModelListByBrand.as_view(), name='model-brand'),

    path('post/id/<int:post_id>', GetPost.as_view(), name='posts'),
    path('posts/brand/<int:brand_id>', PostListByBrand.as_view(), name='post-brand'),
    path('post/views/<int:post_id>', ViewsCount.as_view(), name='post-views'),
    path('posts/latest/', LatestPosts.as_view(), name='latest-posts'),
    path('posts/most/', MostViewed.as_view(), name='most-viewed-posts'),
    path('post/regular/', RegularPost.as_view(), name='regular-post'),
    path('post/special/', SpecialPost.as_view(), name='special-post'),
    path('posts/user/<int:user_id>', UserPosts.as_view(), name='create-post'),

    path('user/request/', CreateRequest.as_view(), name='create-request'),
    path('user/pushtoken/', SavePushToken.as_view(), name='push-token'),

    # path('test/register/', web_views.register, name='authy_test'),
   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
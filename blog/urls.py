from django.urls import path
import blog.views 

urlpatterns = [
    path('photo/upload/', blog.views.PhotoUploadView.as_view(), name='photo_upload'),
    path('create/', blog.views.BlogAndPhotoUploadView.as_view(), name='blog_create'),
    # path('<int:blog_id>', blog.views.BlogDetailView.as_view(), name='blog_detail'),
    # path('<int:blog_id>/edit', blog.views.EditBlogView.as_view(), name='edit_blog'),
    # path('photo/upload-multiple/', blog.views.CreateMultiplePhotos.as_view(), name='create_multiple_photos'),
    # path('follow-users/', blog.views.FollowUsersView.as_view(), name='follow_users'),
    # path('photos/', blog.views.PhotoFeedView.as_view(), name='photos')
]

from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='compliance-home'),
	path('compliance/<int:pk>/', PostDetailView.as_view(), name='compli-detail'),
	path('compliance/new/', PostCreateView.as_view(), name='compli-create'),
	path('compliance/<int:pk>/update/', PostUpdateView.as_view(), name='compli-update'),
	path('compliance/<int:pk>/delete/', PostDeleteView.as_view(), name='compli-delete'),      
    path('about/', views.about, name='compliance-about')
    
]
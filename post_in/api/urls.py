from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')
router.register('users', UserViewSet, basename='users')
urlpatterns = router.urls


"""
# 6 версия:
router = DefaultRouter()
router.register('notes', NoteViewSet, basename='notes')
urlpatterns = router.urls
"""


"""
# 5 версия:
notes_list = NoteViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
notes_detail = NoteViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
urlpatterns = [
    path('notes/', notes_list, name='notes-list'),
    path('notes/<int:pk>/', notes_detail, name='notes-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)  # позволит в адресе указать /?format=json и увидеть чисто json
"""


"""
# 2, 3, 4 версия:
urlpatterns = [
    path('notes/', NoteListView.as_view()),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='notes-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)  # позволит в адресе указать /?format=json и увидеть чисто json
"""


"""
# 1 версия:
urlpatterns = [
    path('notes/', notes_list,  name='notes-list'),
    path('notes/<int:pk>/', notes_detail, name='notes-detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)  # позволит в адресе указать /?format=json и увидеть чисто json
"""

# 127.0.0.1:8000/api/notes - увидите ответ на api

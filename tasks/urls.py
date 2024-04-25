from django.urls import path
from django.views.generic import RedirectView
from .views import CreateTask, ListTask, UpdateTask, DeleteTask
from .htmx_views import ConcludeTask


urlpatterns = [
    path('', RedirectView.as_view(url='/tasks/'), name='index_redirect'),
    path('tasks/', ListTask.as_view(), name='list_view'),
    path('tasks/create_task/', CreateTask.as_view(), name='create_view'),
    path('tasks/delete/<int:pk>/', DeleteTask.as_view(), name='delete_view'),
    path('tasks/update/<int:pk>/', UpdateTask.as_view(), name='update_view'),
]


htmx_urlpatterns = [
    path('tasks/search/<str:param>/', ConcludeTask.as_view(), name='filter_view'),
    path('tasks/conclude/<int:pk>/', ConcludeTask.as_view(), name='conclude_view')
]

urlpatterns += htmx_urlpatterns
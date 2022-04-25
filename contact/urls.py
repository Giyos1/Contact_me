from django.urls import path
from .views import contact_list, create_page, create, get, delete_page, delete, add_page, add, admin, upload_page, upload

app_name = 'contact'
urlpatterns = [
    path('list/', contact_list, name='list'),
    path('create_page/', create_page, name='create_page'),
    path('create/', create, name='create'),
    path('get/<int:contact_id>', get, name='get'),
    path('delete_page/<int:contact_id>/', delete_page, name='delete_page'),
    path('delete/<int:contact_id>/', delete, name='delete'),
    path('add_page/<int:contact_id>', add_page, name='add_number_page'),
    path('add/<int:contact_id>', add, name='add_number'),
    path('admin/', admin, name='admin'),
    path('upload_page/', upload_page, name='upload_page'),
    path('upload/', upload, name='upload'),
]

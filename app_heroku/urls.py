from django.urls import path
from .views import my_home, my_index, my_about, my_todo_detail
from . import views as logic

# тут только "маршруты" - адрес страницы
urlpatterns = [
    path('', my_home, ""),
    path('my_home/', my_home, name="my_home"),
    path('my_index/', my_index, name="my_index"),
    path('my_about/', my_about, name="my_about"),

    path('my_todo_detail/<int:todo_id>/', my_todo_detail, name="my_todo_detail"),
    path(route='todo_list/', view=logic.todo_list, name="todo_list"),
    path(route='my_todo_create/', view=logic.my_todo_create, name="my_todo_create"),
    path(route='my_todo_delete/<int:todo_id>/', view=logic.my_todo_delete, name="my_todo_delete"),
    path(route='my_todo_update_status/<int:todo_id>/', view=logic.my_todo_update_status, name="my_todo_update_status"),
    path(route='my_todo_change_data/<int:todo_id>/', view=logic.my_todo_change_data, name="my_todo_change_data"),

    path(route='my_admin_page/', view=logic.my_admin_page, name="my_admin_page"),
]


from django.urls import path
from tutorial.urls import router

import books.views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('books', books.views.BookViewset, basename='books')

urlpatterns = [
    # path('', books.views.BookListApi.as_view()),
    # path('books/list/create/', books.views.BookaListCreateApi.as_view() ),
    # path('books/update/delete/<int:pk>/', books.views.BookUpdateDeleteApi.as_view()),
    # path('books/create/', books.views.BookCreateApi.as_view()),
    # path('<int:pk>/', books.views.BookDetailApi.as_view()),
    # path('<int:pk>/update/', books.views.BookUpdateApi.as_view()),
    # path('<int:pk>/delete/', books.views.BookDeleteApi.as_view())
]
urlpatterns = urlpatterns + router.urls
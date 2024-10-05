from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from yaml import serialize

from .models import Book
from .serializers import BookSerializer
from rest_framework import generics, status
from rest_framework.views import APIView
# class BookListApi(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
class BookListApi(APIView):
	def get(self, request):
		books = Book.objects.all()
		serialozer_data = BookSerializer(books, many=True).data
		data = {
			'status': f"Retured {len(books)} books",
			'books': serialozer_data
		}
		return Response(data)

# class BookDetailApi(generics.RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#

# class BookDetailApi(APIView):
#     def get(self, request, pk):
#         book = Book.objects.get(id=pk)
#         serializer_data = BookSerializer(book).data
#         data = {
#             'status': "Successfull",
#             'book': serializer_data
#         }
#         return Response(data)
class BookDetailApi(APIView):

	def get(self, request, pk):
		try:
			book = Book.objects.get(id=pk)
			serializer_data = BookSerializer(book).data
			data = {
				'status': "Successfull",
				'book': serializer_data
			}
			return Response(data)
		except Exception:
			return Response(
				{
					"status": "False",
					"message": "Book is not found"
				},
				status=status.HTTP_404_NOT_FOUND
			)

# class BookDeleteApi(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookDeleteApi(APIView):
	def delete(self, request, pk):
		try:
			book = Book.objects.get(id=pk)
			book.save()
			return Response(
				{
					'status': True,
					'message': "Successfull deleted",
				},
				status=status.HTTP_200_OK
			)
		except Exception:
			return Response(
				{
					"status": "False",
					"message": "Book is not found"
				},
				status=status.HTTP_400_BAD_REQUEST
			)

class BookUpdateApi(generics.UpdateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

# class BookCreateApi(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

class BookCreateApi(APIView):
	def post(self, request):
		data = request.data
		serializer = BookSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			data = {
				'status': f"Books are saved to the database",
				'books': data
			}
			return Response(data)


class BookaListCreateApi(generics.ListCreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class BookUpdateDeleteApi(generics.RetrieveUpdateDestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class BookViewset(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import Food, Today
from .serializers import FoodSerializer, TodaysCalories


# class FoodList(generics.ListCreateAPIView):
#     serializer_class = FoodSerializer

#     def get_queryset(self):
#         queryset = Food.objects.all()
#         name = self.request.query_params.get('name')
#         if name is not None:
#             queryset = queryset.filter(name=name)
#         return queryset


# class FoodDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = FoodSerializer
#     queryset = Food.objects.all

class FoodList(APIView):
    def get(self, request):
        queryset = Food.objects.all()
        serializer = FoodSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        foodSerializer = FoodSerializer(data=request.data)
        if foodSerializer.is_valid():
            foodSerializer.save()
            return Response(foodSerializer.data, status=status.HTTP_201_CREATED)

        return Response(foodSerializer.errors)


class FoodDetail(APIView):
    def get_food(self, pk):
        try:
            return Food.objects.get(pk=pk)

        except Food.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        food = self.get_food(pk)
        serializer = FoodSerializer(food)
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_food(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # def put(self, request, pk):
    #     pass


class FoodAddedList(APIView):

    def get(self, request):
        queryset = Today.objects.all()
        serializer = TodaysCalories(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        todaySerializer = TodaysCalories(data=request.data)
        if todaySerializer.is_valid():
            todaySerializer.save()
            return Response(todaySerializer.data, status=status.HTTP_201_CREATED)

        return Response(todaySerializer.errors)


class FoodAddedDetail(APIView):
    def get_foodToday(self, pk):
        try:
            return Today.objects.get(pk=pk)

        except Today.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        food = self.get_foodToday(pk)
        serializer = TodaysCalories(food)
        return Response(serializer.data)

    def delete(self, request, pk):
        self.get_foodToday(pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404

from jobs.models import Job
from jobs.api.serializers import JobSerializer


class JobListCreateAPIView(APIView):

  def get(self, request):
    jobs = Job.objects.all()
    # jobs = Job.objects.filter(available=True)
    serializer = JobSerializer(jobs, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = JobSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class JobDetailAPIView(APIView):

  def get_object(self, pk):
    job = get_object_or_404(Job, pk=pk)
    return job

  def get(self, request, pk):
    job = self.get_object(pk)
    serializer = JobSerializer(job)
    return Response(serializer.data)

  def put(self, request, pk):
    job = self.get_object(pk)
    serializer = JobSerializer(job, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk):
    job = self.get_object(pk)
    job.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)



# @api_view(["GET", "POST"])
# def article_list_create_api_view(request):

#   if request.method == "GET":
#     articles = Article.objects.filter(active=True)
#     serializer = ArticleSerializer(articles, many=True)
#     return Response(serializer.data)

#   elif request.method == "POST":
#     serializer = ArticleSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(["GET", "PUT", "DELETE"])
# def article_detail_api_view(request, pk):

#   try:
#     article = Article.objects.get(pk=pk)
#   except Article.DoesNotExist:
#       return Response({"error": {
#                         "code": 404,
#                         "message": "Article not found!"
#                       }}, status=status.HTTP_404_NOT_FOUND)

#   if request.method == "GET":
#     serializer = ArticleSerializer(article)
#     return Response(serializer.data)

#   elif request.method == "PUT": # update a specific record
#     serializer = ArticleSerializer(article, data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   elif request.method == "DELETE":
#     article.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
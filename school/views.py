from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import (
    HomePageSerializer,
    AboutPageSerializer,
    TeacherPageSerializer,
    BlogPageSerializer,
    CoursePageSerializer,
    BlogDetailPageSerializer,
)
from .models import (
    Slider,
    About,
    OurHistory,
    Result,
    Partner,
    AboutCard,
    Teacher,
    Blog,
    BlogCategory,
    Tag,
    Course
)

class HomePageAPIView(APIView):
    def get(self, request):
        data = {
            'sliders': Slider.objects.all(),
            'about': About.objects.all(),
            'our_history': OurHistory.objects.all(),
            'results': Result.objects.all(),
            'partners': Partner.objects.all(),
        }
        serializer = HomePageSerializer(data, context={'request': request})
        return Response(serializer.data)


class AboutPageAPIView(APIView):
    def get(self,request):
        data = {
            'about' : About.objects.all(),
            'card' : AboutCard.objects.all(),
            'partners' : Partner.objects.all(),
        }
        serializer = AboutPageSerializer(data, context={'request':request})
        return Response(serializer.data)
    
    
class TeacherPageAPIView(APIView):
    def get(self,request):
        data = {
            'teacher': Teacher.objects.all(),
            'partners': Partner.objects.all(),
        }
        serializer = TeacherPageSerializer(data,context={'request':request})
        return Response(serializer.data)
    

class BlogPageAPIView(APIView):
    def get(self,request):
        data = {
            'blog':Blog.objects.all(),
            'category':BlogCategory.objects.all(),
            'tag':Tag.objects.all()
        }
        serializer = BlogPageSerializer(data,context={'request':request})
        return Response(serializer.data)

class BlogDetailAPIView(APIView):
    def get(self, request, slug):
        try:
            blog = Blog.objects.get(slug=slug)
        except Blog.DoesNotExist:
            return Response({'error': 'Blog not found'}, status=status.HTTP_404_NOT_FOUND)

        category = BlogCategory.objects.all()
        tags = Tag.objects.all()
        
        data = {
            'blog': blog,
            'category': category,
            'tags': tags
        }
        serializer = BlogDetailPageSerializer(data, context={'request': request})
        return Response(serializer.data)
    

class CoursePageAPIView(APIView):
    def get(self,request):
        data = {
            'course':Course.objects.all(),
            'partner':Partner.objects.all()
        }
        serializer = CoursePageSerializer(data,context={'request':request})
        return Response(serializer.data)
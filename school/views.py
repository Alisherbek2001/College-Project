from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import (
    HomePageSerializer,
    AboutPageSerializer,
    TeacherPageSerializer,
    BlogPageSerializer,
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
    Tag
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
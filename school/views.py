from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import HomePageSerializer
from .models import Slider, About, OurHistory, Result, Partner

class HomePageAPIView(APIView):
    def get(self, request):
        data = {
            'sliders': Slider.objects.all(),
            'about': About.objects.all(),
            'our_history': OurHistory.objects.all(),
            'results': Result.objects.all(),
            'partners': Partner.objects.all(),
        }
        serializer = HomePageSerializer(data)
        return Response(serializer.data)

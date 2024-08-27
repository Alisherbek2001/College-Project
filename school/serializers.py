from rest_framework import serializers
from .models import Partner, Slider,About,OurHistory,Result

class SliderSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()

    class Meta:
        model = Slider
        fields = ['id', 'title', 'image', 'description']

    def get_title(self, obj):
        return {
            'uz': obj.title_uz,
            'ru': obj.title_ru,
            'en': obj.title_en
        }

    def get_description(self, obj):
        return {
            'uz': obj.description_uz,
            'ru': obj.description_ru,
            'en': obj.description_en
        }
        
class AboutSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    
    class Meta:
        model = About
        fields = ['id','title','slug','image','description']
        
    def get_title(self, obj):
        return {
            'uz': obj.title_uz,
            'ru': obj.title_ru,
            'en': obj.title_en
        }

    def get_description(self, obj):
        return {
            'uz': obj.description_uz,
            'ru': obj.description_ru,
            'en': obj.description_en
        }


class OurHistorySerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    
    class Meta:
        model = OurHistory
        fields = ['id','history_year','description','image']
    
    def get_description(self, obj):
        return {
            'uz': obj.description_uz,
            'ru': obj.description_ru,
            'en': obj.description_en
        }
        
class ResultSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = Result
        fields = ['id','name','amount','icon']
        
    def get_name(self,obj):
        return {
            'uz':obj.name_uz,
            'ru':obj.name_ru,
            'en':obj.name_en
        }
        
class PartnerSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    
    class Meta:
        model = Partner
        fields = ['id','name','link','icon']
        
    def get_name(self,obj):
        return {
            'uz':obj.name_uz,
            'ru':obj.name_ru,
            'en':obj.name_en
        }


class HomePageSerializer(serializers.Serializer):
    sliders = SliderSerializer(many=True)
    about = AboutSerializer(many=True)
    our_history = OurHistorySerializer(many=True)
    results = ResultSerializer(many=True)
    partners = PartnerSerializer(many=True)
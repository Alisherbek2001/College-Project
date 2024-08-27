from modeltranslation.translator import register, TranslationOptions
from .models import Slider,About,OurHistory,Result,Partner

@register(Slider)
class SliderTranslateOptions(TranslationOptions):
    fields = ('title','description')
    
    
@register(About)
class AboutTranslateOptions(TranslationOptions):
    fields = ('title','description')
    
@register(OurHistory)
class OurHistoryTranslateOptions(TranslationOptions):
    fields = ('description',)
    
@register(Result)
class ResultTranslateOptions(TranslationOptions):
    fields = ('name',)
    
@register(Partner)
class PartnerTranslateOptions(TranslationOptions):
    fields = ('name',)
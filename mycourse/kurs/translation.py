from .models import Course
from modeltranslation.translator import TranslationOptions, register

@register(Course)
class MovieTranslationOptions(TranslationOptions):
    fields = ('name','description')
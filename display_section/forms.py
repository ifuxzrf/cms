from django.forms import ModelForm, Form, fields
from display_section.models import Things, image


class Things_form(ModelForm):
    a = fields.CharField()

    class Meta:
        model = Things
        fields = '__all__'
        # labels = {'name': '名字'}
        # help_texts = {'name': '测试一下'}
        # widgets = None
        # error_messages = None
        # field_classes = None


class Image_form(ModelForm):
    class Meta:
        model = image
        fields = '__all__'

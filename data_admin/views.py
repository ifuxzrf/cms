from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpRequest, HttpResponse
from data_admin.models import Synonyms, Emotional, Sensitive
from django.contrib.auth.mixins import LoginRequiredMixin
from tools.utils import pages

import datetime


# Create your views here.
class SynonymsView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/synonyms.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Synonyms.objects.all()
        context = pages(obj, self.request, context)
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action', '')
        if action == 'delete':
            print('delete')
            synonyms_id = request.POST.get('synonyms_id', '')
            Synonyms.objects.filter(id=synonyms_id).delete()
        else:
            word = request.POST.get('word')
            parent_id = request.POST.get('parent_id')
            count = int(request.POST.get('count'))
            status = int(request.POST.get('status'))
            create_time = datetime.datetime.now()
            if action == 'add':
                Synonyms.objects.get_or_create(word=word, parent_id=parent_id, count=count, status=status,
                                               create_time=create_time)
            elif action == 'change':
                synonyms_id = request.POST.get('synonyms_id')
                Synonyms.objects.filter(id=synonyms_id).update(**{'word': word, 'parent_id': parent_id,
                                                                   'count': count, 'status': status,
                                                                   'create_time': create_time})
            else:
                pass
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class EmotionalView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/emotional.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Emotional.objects.all()
        context = pages(obj, self.request, context)
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action', '')
        if action == 'delete':
            print('delete')
            emotional_id = request.POST.get('emotional_id', '')
            Emotional.objects.filter(id=emotional_id).delete()
        else:
            word = request.POST.get('word')
            table_type = request.POST.get('table_type')
            emotion_type = request.POST.get('emotion_type')
            count = int(request.POST.get('count'))
            status = int(request.POST.get('status'))
            create_time = datetime.datetime.now()
            if action == 'add':
                Emotional.objects.get_or_create(word=word, table_type=table_type, emotion_type=emotion_type,
                                                count=count, status=status, create_time=create_time)
            elif action == 'change':
                emotional_id = request.POST.get('emotional_id')
                Emotional.objects.filter(id=emotional_id).update(**{'word': word, 'table_type': table_type,
                                                                    'emotion_type': emotion_type, 'count': count,
                                                                    'status': status, 'create_time': create_time})
            else:
                pass
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class SensitiveView(LoginRequiredMixin, TemplateView):
    template_name = 'admin/sensitive.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Sensitive.objects.all()
        context = pages(obj, self.request, context)
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action', '')
        if action == 'delete':
            print('delete')
            sensitive_id = request.POST.get('sensitive_id', '')
            Sensitive.objects.filter(id=sensitive_id).delete()
        else:
            word = request.POST.get('word')
            table_type = request.POST.get('table_type')
            count = int(request.POST.get('count'))
            status = int(request.POST.get('status'))
            create_time = datetime.datetime.now()
            if action == 'add':
                Sensitive.objects.get_or_create(word=word, table_type=table_type, count=count, status=status,
                                                create_time=create_time)
            elif action == 'change':
                sensitive_id = request.POST.get('sensitive_id')
                Sensitive.objects.filter(id=sensitive_id).update(**{'word': word, 'table_type': table_type,
                                                                    'count': count, 'status': status,
                                                                    'create_time': create_time})
            else:
                pass
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

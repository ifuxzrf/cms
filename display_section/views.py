import datetime
from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView

from display_section.forms import Things_form
from display_section.models import Things
import logging
from rest_framework import viewsets
from display_section.serializers import ThingsSerializer

# Create your views here.

from tools.utils import pages


class ThingsView(TemplateView):
    template_name = 'display/product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = Things.objects.all()
        new_form = Things_form
        update_form = Things_form
        context['new_form'] = new_form
        context['update_form'] = update_form
        context = pages(obj, self.request, context)
        return context

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action', '')
        if action == 'delete':
            print('delete')
            synonyms_id = request.POST.get('synonyms_id', '')
            Things.objects.filter(id=synonyms_id).delete()
        else:
            word = request.POST.get('word')
            parent_id = request.POST.get('parent_id')
            count = int(request.POST.get('count'))
            status = int(request.POST.get('status'))
            create_time = datetime.datetime.now()
            if action == 'add':
                Things.objects.get_or_create(word=word, parent_id=parent_id, count=count, status=status,
                                             create_time=create_time)
            elif action == 'change':
                synonyms_id = request.POST.get('synonyms_id')
                Things.objects.filter(id=synonyms_id).update(**{'word': word, 'parent_id': parent_id,
                                                                'count': count, 'status': status,
                                                                'create_time': create_time})
            else:
                pass
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


def form1(request):
    from display_section.forms import Things_form
    f = Things_form()
    if request.method == 'GET':
        pass
    else:
        args = request.POST
        print(args)
    return render(request, 'display/form1.html', {'form': f})


# class ThingsViewSet(viewsets.ModelViewSet):
#     queryset = Things.objects.all()
#     serializer_class = ThingsSerializer

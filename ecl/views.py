from django.shortcuts import render
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.
from django.http import HttpResponse
from .models import Entry, Tag

def errors(request, error_id):
    return HttpResponse("This is the error/problem")

class IndexView(generic.ListView):
    context_object_name = 'entries'    
    template_name = 'ecl/index.html'
    queryset = Entry.objects.all().reverse()

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        # And so on for more models
        return context

class TagView(generic.ListView):
    template_name = 'ecl/index.html'
    context_object_name = 'tags'

    def get_queryset(self):
        return Tag.objects.all()

class EntryView(generic.ListView):
    def get_entries(self):
        return "Hello"

def add(request):
    print(request.POST)

    entry_content = request.POST.get("entry_box", "")
    correction_content = request.POST.get("correction_box", "")
    category = request.POST.get("category", "")
    t, created = Tag.objects.get_or_create(tag=category)
    e = Entry.objects.create(error_text = entry_content, correction_text = correction_content, tag = t)
    e.save()
    return HttpResponse(entry_content)

class EntriesByTag(generic.ListView):
    template_name = 'ecl/index.html'
    context_object_name = 'entries'

    def get_queryset(self):
        return Entry.objects.filter(tag=self.kwargs['pk']).reverse()

class EntriesByTag(generic.ListView):
    template_name = 'ecl/index.html'
    context_object_name = 'entries'

    def get_queryset(self):
        return Entry.objects.filter(tag=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(EntriesByTag, self).get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()
        return context

def about(request):
    return render(request, 'ecl/about.html')
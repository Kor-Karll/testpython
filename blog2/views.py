from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from django.utils import timezone
from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from blog2.models import Post

from django.views.generic.edit import FormView
from blog2.forms import PostSearchFrom
from django.db.models import Q
from django.shortcuts import render

# Create your views here.

class TagTV(TemplateView):
    template_name = 'tagging/tagging_cloud.html'

class PostLV(ListView):
    model = Post
    template_name = 'blog2/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

class PostTOL(TaggedObjectList):
    model = Post
    template_name = 'tagging/tagging_post_list.html'

class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_date'

# FormView

# GET 요청은 화면만 보여주고 입력대기
# POST 요청으로 입력값이 들어오면 유효성 검사를 한 후 form_valid 함수 실행
class SearchFormView(FormView):
    form_class = PostSearchFrom
    template_name = 'blog2/post_search.html'

    def form_valid(self, form):
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__incontains=schWord) | Q(description__incontains=schWord) | Q(content__incontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)

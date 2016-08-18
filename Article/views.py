from django.shortcuts import render
from django.http import HttpResponse
from Article.models import BlogArticle
from datetime import datetime
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import TemplateView

from django.contrib.syndication.views import Feed

# Create your views here.
def home(request):
    posts = BlogArticle.objects.all()
    paginator = Paginator(posts,1)
    page = request.GET.get('page')
    try:
        postlist = paginator.page(page)
    except PageNotAnInteger:
        postlist = paginator.page(1)
    except EmptyPage:
        postlist = paginator.paginator(paginator.num_pages)
    return render(request,'home.html',{'post_list':postlist})

def detail(request,id):
    try:
        post = BlogArticle.objects.get(id = str(id))
    except BlogArticle.DoseNotExist:
        raise Http404
    return render(request,'post.html',{'post':post})

def test(request):
    return render(request,'test.html',{'current_time':datetime.now()})

def archives(request):
	try:
		postlist = BlogArticle.objects.all()

	except BlogArticle.DoseNotExist:
		raise Http404
	return render(request,"archives.html",{'post_list':postlist,'error':False})

class AboutView(TemplateView):
    """docstring for AboutView"""
    template_name = "aboutme.html"
        
# def about_me(request):
# 	return render(request,"aboutme.html")

def search_tag(request, tag) :
    try:
        post_list = BlogArticle.objects.filter(category__iexact = tag) #contains
    except BlogArticle.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request,'home.html')
        else:
            post_list = BlogArticle.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list,
                                                    'error' : False})
    return redirect('/')

class RSSFeed(Feed):
    """docstring for RSSFeed"""
    # def __init__(self, arg):
    #     super(RSSFeed, self).__init__()
    #     self.arg = arg
    title = "RSS feed - article"
    link = "feeds/posts"
    decription = "RSS feed - blog posts"

    def items(self):
        return BlogArticle.objects.order_by('-date_time')

    def item_title(self,item):
        return item.title

    def item_pubdate(self,item):
        return item.date_time

    def item_description(self,item):
        return item.content
        


from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View

from article.models import Article, Aboutme

# Create your views here.


class HomepageView(View):
    def get(self, request):
        # 获取全部的Article对象
        post_list = Article.objects.all()
        return render(request, 'homepage.html', {
            'post_list': post_list
        })


class DetailView(View):
    def get(self, request, id):
        post = Article.objects.get(id=str(id))
        return render(request, "post.html", {
            "post": post
        })


class AboutmeView(View):
    def get(self, request):
        about = Aboutme.objects.all()
        return render(request, "about_me.html", {
            "about": about
        })


class ArchivesView(View):
    def get(self, request):
        post_list = Article.objects.all()  # 获取全部的Article对象
        return render(request, "archives.html", {
            'post_list': post_list,
            'error':False
        })


class TagView(View):
    def get(self, request, tag):
        post_list = Article.objects.filter(category=tag)
        return render(request, 'tag.html', {
            'post_list':post_list,
        })


class SearchView(View):
    def get(self, request, search):
        search = request.GET['search']
        if not search:
            return render(request, 'homepage.html')
        else:
            post_list = Article.objects.filter(title__contains=search)
            if len(post_list) == 0:
                return render(request, 'archives.html', {
                    'post_list':post_list,
                    'error':True
                })
            else:
                return render(request, 'archives.html', {
                    'post_list': post_list,
                    'error': False
                })


def page_not_found(request):
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response
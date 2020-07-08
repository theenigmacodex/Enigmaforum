from django.shortcuts import render,get_object_or_404,redirect,render
from django.http import HttpResponse
from .models import Post,Comment
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from users.models import Profile
from django.contrib.auth.decorators import login_required

def home(request):
    context = {
        'posts': Post.objects.all() ,
        'title':"ACE Students",
        'user':User.objects.all()
    }
    return render(request,'blog/home.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    response_template = 'blog/post_detail.html'
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content','postimg','tag']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content','postimg','tag']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if(self.request.user == post.author):
            return True
        return False


class UserPostListView(ListView):
    model = Profile
    template_name = 'blog/user_profile.html'
    allow_empty = False  #this will show 404 if the username does not exists
    ordering = ['-created_date']

    def get(self,request,*args, **kwargs):
        username = self.kwargs['username']
        user_profile = User.objects.get(username=username)
        profile_us = Profile.objects.get(user=user_profile)
        ispro =  profile_us.pro_user
        githubusr = profile_us.github
        posts = Post.objects.filter(author = user_profile)
        comments = Comment.objects.filter(author = user_profile)
        return render(request,'blog/user_profile.html',{'user_profile':user_profile,
                                                        'name':username ,'posts':posts , 'comments':comments,'ispro':ispro,'githubusr':githubusr})
    

class AboutPageView(ListView):
    model = User
    template_name='blog/aboutpage.html'

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST,request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            if('<script src=https://emgithub.com/embed.js' in comment.text or '<script src="https://gist.github.com' in comment.text):
                pass
            elif('<script>' in comment.text and "</script>" in comment.text):
                comment.text = "[ Javascript supression ]"
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


class TagPostListView(ListView):
    model = Post
    template_name = 'blog/tag_related_page.html'
    allow_empty = False  #this will show 404 if the username does not exists

    def get(self,request,*args, **kwargs):
        the_tag = self.kwargs['tag']
        posts = Post.objects.filter(tag=the_tag)
        print(posts)
        return render(request,'blog/tag_related_page.html',{'tag':the_tag,
                                                        'posts':posts})
    
class CommentUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Comment
    template_name = 'blog/add_comment_to_post.html'
    fields = ['githubrepo','microtext','text','commentimg']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        comment = self.get_object()
        if(self.request.user == comment.author):
            return True
        return False

def anime(request):
    context = {
        'posts': Post.objects.all() ,
        'title':"ACE Students",
        'user':User.objects.all()
    }
    return render(request,'https://raw.githubusercontent.com/itspacchu/pacchu-forum/master/misc.html',context)
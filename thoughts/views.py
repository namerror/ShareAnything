from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def post_list(request):
    posts = Post.objects.all().order_by("-publish")
    new_post = None

    # creating a new post
    if request.method == "POST":
        form = PostForm(data=request.POST)

        if form.is_valid():
            try:
                new_post = form.save(commit=False)
                new_post.title = request.POST["title"]
                new_post.author = request.POST["author"]
                new_post.body = request.POST["body"]
                new_post.save()
                return HttpResponse("1")
            except:
                return HttpResponse("Error")
    else:
        form = PostForm()

    return render(request, 'thoughts/post-list.html', {"posts":posts, 'new_post': new_post, 'post_form': form})

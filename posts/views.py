from django.shortcuts import render,redirect
from .models import posts
# Create your views here.
def index(request):
    post = posts.objects.all()

    if 'comments' not in request.session:
        request.session['comments']=[]

    comment=request.session['comments']

    if request.method=='POST':
        new_comment=request.POST.get('myTextarea')
        if new_comment:
            comment.append(new_comment)
            request.session['comments']=comment
            return redirect('index')
        

        del_comment=request.POST.get('comm')
        if del_comment and del_comment in comment:
            
            comment.remove(del_comment)
            request.session['comments']=comment
            return redirect('index')

    return render(request, 'index.html', {'post': post, 'comments': comment})



def post(request,pk):
    post=posts.objects.get(id=pk)
    return render(request,'post.html',{'post':post})


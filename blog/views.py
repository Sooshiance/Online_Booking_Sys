from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Post
from .forms import CommentForm


def showComment(request):
    c = Post.objects.all().filter(admin_approval=True)
    return render(request, 'blog/showcomment.html', {'comments':c})


def shareComment(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data['title']
                txt = form.cleaned_data['txt']
                vote = form.cleaned_data['vote']
                note = Post.objects.create(title=title, txt=txt, vote=vote, user=request.user)
                note.save()
                messages.success(request, 'دیدگاه شما با موفقیت ثبت شد، لطفا منتظر تایید مدیر بمانید')
                return redirect('SHOW')
            else:
                messages.error(request, "اشتباهی رخ داده")
                return redirect('SHARE')
        else:
            form = CommentForm()
        return render(request, 'blog/comment.html', {'form':form})
    else:
        messages.info(request, 'لطفا وارد شوید')
        return redirect('LOGIN')

from django.shortcuts import render, redirect
from django.views import generic
from .models import New
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import NewAgePost
from django.urls import reverse_lazy

# def pos_lis(request):
#     # all_posts = New.objects.all()
#     all_posts = New.objects.filter(status='pub').order_by('-date_modify')
#     return render(request, 'blogg/poslis.html', {'post_list': all_posts})


class Ournewview(generic.ListView):
    template_name = 'blogg/poslis.html'
    context_object_name = 'post_list'

    def get_queryset(self):
        return New.objects.filter(status='pub').order_by('-date_modify')


def creat_newpos(request):
    if request.method == 'POST':
        form = NewAgePost(request.POST)
        if form.is_valid():
            form.save() #kalak mojofd estfade az esm moshtarak jahat save(darsorat valid bodn) ya edm save ast
            return redirect('new_post')
    else:
        form = NewAgePost()
    return render(request, 'blogg/creating.html', context={'form': form})
    # if request.method == 'POST':
    #     my_title = request.POST.get('title')
    #     my_post = request.POST.get('text')
    #     my_author = User.objects.all()[0]
    #     New.objects.create(title=my_title, text=my_post, authors=my_author, status='pub')
    # else:
    #     print('GET requesttttt')
    # print(request.POST)
    # return render(request, 'blogg/creating.html')


class Ournewcreation(generic.CreateView):
    form_class = NewAgePost
    template_name = 'blogg/creating.html'

# def pos_detail(request, dk):
#     #agar yek farde nasho adad Ex. 1000 ra vared krd eror varede ra besorat print('') nshan dahad va na moshakhassat system ma ra
#     # try:
#     #     post2 = New.objects.get(pk=dk)
#     # except ObjectDoesNotExist:
#     #     post2 = None
#     #     print('Expectied') #be jaye 4 khat fogh yek khat zir ra bekar bbrid
#     post2 = get_object_or_404(New, pk=dk)
#     return render(request, 'blogg/details.html', {'post1': post2})


class Ournewdetail(generic.DetailView):
    model = New
    template_name = 'blogg/details.html'
    context_object_name = 'post1'

# def post_update(request, pk):
#     # post = get_object_or_404(New, pk=pk)
#     post = New.objects.get(pk=pk)
#     form = NewAgePost(request.POST or None, instance=post)
#
#     if form.is_valid():
#         form.save()
#         return redirect('new_post')
#         # print(request.POST.get('text'))
#
#     return render(request, 'blogg/creating.html', context={'form': form})


class Ournewupdate(generic.UpdateView):
    model = New
    form_class = NewAgePost
    template_name = 'blogg/creating.html'

def post_delect(request, pk):
    dele = get_object_or_404(New, pk=pk)

    if request.method == 'POST':
        dele.delete()
        return redirect('new_post')
    return render(request, 'blogg/deleting.html', context={'dele': dele})

class Ournewdelect(generic.DeleteView):
    model = New
    template_name = 'blogg/deleting.html'
    success_url = reverse_lazy('new_post')


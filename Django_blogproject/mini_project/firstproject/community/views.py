from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from community.models import Posting

# Create your views here.

def List(request):
    posts = Posting.objects.filter(upload_time__lte = timezone.now()).order_by('upload_time')
    return render(request, 'list.html', {'posts':posts})

def detail(request, pk):
    post = get_object_or_404(Posting, pk=pk)
    return render(request, 'detail.html', {'post':post})

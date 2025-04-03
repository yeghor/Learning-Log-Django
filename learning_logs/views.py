from django.shortcuts import render, redirect
from .models import Topics, Entry
from .forms import TopicsForm, EntryForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
# Create your views here.

def check_topic_owner(request, owner):
    if owner != request.user:
        raise Http404

def index(request):
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    topics = Topics.objects.filter(owner=request.user).order_by('date_added')

    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    check_topic_owner(request, topic.owner)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request):
    if request.method != 'POST':
        form = TopicsForm()
    else:
        form = TopicsForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            form.save()
            return redirect('learning_logs:topics')
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    check_topic_owner(request, topic.owner)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('learning_logs:topic', topic_id=topic_id)
    
    context = {'topic': topic,  'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    check_topic_owner(request, topic.owner)

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def delete_entry(request, entry_id, topic_id):
    entry = Entry.objects.get(id=entry_id)
    topic = Topics.objects.get(id=topic_id)

    check_topic_owner(request, topic.owner)

    if request.method == 'POST':
        entry.delete()
        return redirect('learning_logs:topic', topic_id=topic_id)
    context = {'entry': entry, 'topic': topic}
    return render(request, 'learning_logs/confirm_delete_entry.html', context)

@login_required
def delete_topic(request, topic_id):
    topic = Topics.objects.get(id=topic_id)
    check_topic_owner(request, topic.owner)
    if request.method == 'POST':
        topic.delete()
        return redirect('learning_logs:topics')
    context = {'topic': topic}
    return render(request, 'learning_logs/confirm_delete_topic.html', context)

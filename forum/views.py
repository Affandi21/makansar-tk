from django.shortcuts import render

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Discussion, Makanan, Reply
from .forms import DiscussionForm, ReplyForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden



@login_required(login_url='/login')
def show_discussions(request, makanan_id):
    makanan = get_object_or_404(Makanan, id=makanan_id)
    discussions = makanan.discussion_set.all().order_by('-date_created')
    return render(request, 'show_discussions.html', {'makanan': makanan, 'discussions': discussions})

@csrf_exempt
@login_required(login_url='/login')
def add_discussion(request, makanan_id):
    if not request.user.buyer:
        return HttpResponseForbidden("You do not have permission to access this page.")
    makanan = get_object_or_404(Makanan, id=makanan_id)
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.user = request.user
            discussion.makanan = makanan
            discussion.save()
            return redirect('forum:show_discussions', makanan_id=makanan.id)
    else:
        form = DiscussionForm()
    return render(request, 'add_discussion.html', {'form': form, 'makanan': makanan})

@csrf_exempt
@login_required(login_url='/login')
def update_discussion(request, discussion_id):
    if not request.user.buyer:
        return HttpResponseForbidden("You do not have permission to access this page.")
    discussion = get_object_or_404(Discussion, id=discussion_id)
    if discussion.user != request.user:
        messages.error(request, "Anda tidak memiliki izin untuk mengedit diskusi ini.")
        return HttpResponseRedirect(reverse('forum:show_discussions', args=[discussion.makanan.id]))

    if request.method == 'POST':
        form = DiscussionForm(request.POST, instance=discussion)
        if form.is_valid():
            form.save()
            messages.success(request, "Diskusi telah berhasil diperbarui.")
            return HttpResponseRedirect(reverse('forum:show_discussions', args=[discussion.makanan.id]))
    else:
        form = DiscussionForm(instance=discussion)
    return render(request, 'edit_discussion.html', {'form': form, 'discussion': discussion})

@csrf_exempt
@login_required(login_url='/login')
def delete_discussion(request, discussion_id):
    if not request.user.buyer:
        return HttpResponseForbidden("You do not have permission to access this page.")
    discussion = get_object_or_404(Discussion, id=discussion_id)
    if discussion.user != request.user:
        messages.error(request, "Anda tidak memiliki izin untuk menghapus diskusi ini.")
        return HttpResponseRedirect(reverse('forum:show_discussions', args=[discussion.makanan.id]))

    makanan_id = discussion.makanan.id
    discussion.delete()
    messages.success(request, "Diskusi telah berhasil dihapus.")
    return HttpResponseRedirect(reverse('forum:show_discussions', args=[makanan_id]))

@login_required(login_url='/login')
def add_reply(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id)
    if request.method == 'POST':
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.user = request.user
            reply.discussion = discussion
            reply.save()
            return HttpResponseRedirect(reverse('forum:show_discussions', args=[discussion.makanan.id]))
    else:
        form = ReplyForm()
    return render(request, 'add_reply.html', {'form': form, 'discussion': discussion})

@login_required(login_url='/login')
def update_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    if reply.user != request.user:
        messages.error(request, "Anda tidak memiliki izin untuk mengedit balasan ini.")
        return HttpResponseRedirect(reverse('forum:show_discussions', args=[reply.discussion.makanan.id]))
    if request.method == 'POST':
        form = ReplyForm(request.POST, instance=reply)
        if form.is_valid():
            form.save()
            messages.success(request, "Balasan telah berhasil diperbarui.")
            return HttpResponseRedirect(reverse('forum:show_discussions', args=[reply.discussion.makanan.id]))
    else:
        form = ReplyForm(instance=reply)
    return render(request, 'edit_reply.html', {'form': form, 'reply': reply})

@login_required(login_url='/login')
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    if reply.user != request.user:
        messages.error(request, "Anda tidak memiliki izin untuk menghapus balasan ini.")
        return HttpResponseRedirect(reverse('forum:show_discussions', args=[reply.discussion.makanan.id]))
    makanan_id = reply.discussion.makanan.id
    reply.delete()
    messages.success(request, "Balasan telah berhasil dihapus.")
    return HttpResponseRedirect(reverse('forum:show_discussions', args=[makanan_id]))
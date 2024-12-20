from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Discussion, Makanan, Reply
from .forms import DiscussionForm, ReplyForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseForbidden
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json





@login_required
def show_discussions(request, makanan_id):
    makanan = get_object_or_404(Makanan, id=makanan_id)
    discussions = makanan.discussion_set.all().order_by('-date_created')
    return render(request, 'show_discussions.html', {'makanan': makanan, 'discussions': discussions})

@csrf_exempt
@login_required
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
@login_required
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
@login_required
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

@login_required
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

@login_required
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

@login_required
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)
    if reply.user != request.user:
        messages.error(request, "Anda tidak memiliki izin untuk menghapus balasan ini.")
        return HttpResponseRedirect(reverse('forum:show_discussions', args=[reply.discussion.makanan.id]))
    makanan_id = reply.discussion.makanan.id
    reply.delete()
    messages.success(request, "Balasan telah berhasil dihapus.")
    return HttpResponseRedirect(reverse('forum:show_discussions', args=[makanan_id]))


#flutter

def list_discussions(request, makanan_id):
    discussions = Discussion.objects.filter(makanan_id=makanan_id)
    response = {
        "current_user": request.user.username,  # Tambahkan pengguna saat ini
        "discussions": [
            {
                'id': d.id,
                'title': d.title,
                'message': d.message,
                'user': d.user.username,
                'replies': [{'id': r.id, 'user': r.user.username, 'message': r.message} for r in d.replies.all()]
            }
            for d in discussions
        ],
    }
    return JsonResponse(response, safe=False)
    

@csrf_exempt
@login_required
def add_discussionflutter(request, makanan_id):
    if request.method == "POST":
        try:
            # Debugging request body dan header
            print(f"Request body: {request.body}")
            print(f"Request headers: {request.headers}")

            # Parse JSON
            data = json.loads(request.body)
            print(f"Parsed JSON: {data}")

            title = data.get("title")
            message = data.get("message")

            if not title or not message:
                return JsonResponse({"status": "error", "message": "Title and message are required"}, status=400)

            makanan = get_object_or_404(Makanan, id=makanan_id)
            discussion = Discussion.objects.create(
                user=request.user, makanan=makanan, title=title, message=message
            )
            return JsonResponse({"status": "success", "id": discussion.id}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)




@csrf_exempt
@login_required
def update_discussionflutter(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id, user=request.user)
    data = json.loads(request.body)
    discussion.title = data['title']
    discussion.message = data['message']
    discussion.save()
    return JsonResponse({"status": "success"})

@csrf_exempt
@login_required
def delete_discussionflutter(request, discussion_id):
    discussion = get_object_or_404(Discussion, id=discussion_id, user=request.user)
    discussion.delete()
    return JsonResponse({"status": "success"})

@csrf_exempt
@login_required
def add_replyflutter(request, discussion_id):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            message = data.get("message")

            if not message:
                return JsonResponse({"status": "error", "message": "Message is required"}, status=400)

            discussion = get_object_or_404(Discussion, id=discussion_id)

            # Create reply
            Reply.objects.create(user=request.user, discussion=discussion, message=message)
            return JsonResponse({"status": "success"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"status": "error", "message": "Invalid JSON format"}, status=400)
        except Exception as e:
            print(f"Error: {str(e)}")
            return JsonResponse({"status": "error", "message": str(e)}, status=500)

    return JsonResponse({"status": "error", "message": "Invalid request method"}, status=405)

@csrf_exempt
@login_required
def update_replyflutter(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id, user=request.user)
    data = json.loads(request.body)
    reply.message = data['message']
    reply.save()
    return JsonResponse({"status": "success"})

@csrf_exempt
@login_required
def delete_replyflutter(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id, user=request.user)
    reply.delete()
    return JsonResponse({"status": "success"})
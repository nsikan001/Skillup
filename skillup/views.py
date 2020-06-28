from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Category, Subject, Course, MyEnrolledCourses, Topic, ContactMessage, Instructor


def signup_view(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]
        if not password == password2:
            return render(request, "signup.html", {"message": "Passwords don't match."})
        user = User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        return render(request, "login.html", {"message": "Registered. You can log in now."})
    return render(request, "signup.html")


def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        if request.user.is_superuser:
            return HttpResponseRedirect(reverse("admin_area"))
        return HttpResponseRedirect(reverse("home"))
    else:
        return render(request, "login.html", {"msg": "Invalid credentials"})


def admin_area(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "admin_dashboard.html", context)


def manage_courses(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "manage_courses.html", context)


def edit_course(request, course_id):
    context = {
        "edit": Course.objects.get(id=course_id)
    }
    return render(request, "edit_course.html", context)


def edited_course(request, edit_id):
    if request.method == "POST":
        course_name = request.POST["course_name"]
        course_level = request.POST["course_level"]
        preview_text = request.POST["preview_text"]
        image_url = request.POST["image_url"]
        Course.objects.filter(id=edit_id).update(name=course_name, level=course_level, preview_text=preview_text,
                                                       image_url=image_url)
        context = {
            "message": "Your information was been updated",
            "courses": Course.objects.all()
        }

        return render(request, "manage_courses.html", context)
    return render(request, "edit_course.html")


def topics(request, course_id):
    context = {
        "topics": Topic.objects.filter(course=course_id)
    }
    return render(request, "edit_topics.html", context)


def edit_topic(request, topic_id):
    # edit_topic = Topic.objects.get(id=topic_id)
    # if edit_topic:
    #     return HttpResponse(topic_id)
    context = {
        "edit_topic": Topic.objects.get(id=topic_id)
    }
    return render(request, "edit_topic.html", context)


def edited_topic(request, edit_id):
    if request.method == "POST":
        title = request.POST["title"]
        vid_url = request.POST["vid_url"]
        Topic.objects.filter(id=edit_id).update(title=title, vid_url=vid_url)
        context = {
            "message": "Your information was updated",
            "courses": Course.objects.all()
        }

        return render(request, "manage_courses.html", context)


def contact_messages(request):
    context = {
        "messages": ContactMessage.objects.all()
    }

    return render(request, "contact_messages.html", context)


def home_view(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"msg": None})
    # current_user = request.user.id
    context = {
        "user": request.user,
        "myCourses": MyEnrolledCourses.objects.filter(user_id=request.user.id)
    }
    return render(request, "home.html", context)


def profile_view(request):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"msg": None})
    if request.user.is_superuser:
        return HttpResponseRedirect(reverse("admin_profile"))
    context = {
        "user": request.user,
        "profile": User.objects.filter(id=request.user.id)
    }
    return render(request, "profile.html", context)


def admin_profile(request):
    context = {
        "user": request.user
    }
    return render(request, "admin_profile.html", context)


def edit_profile(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        User.objects.filter(id=request.user.id).update(first_name=first_name, last_name=last_name, username=username, email=email)

        if request.user.is_superuser:
            return render(request, "admin_profile.html", {"message": "Your profile information has been updated"})
        return render(request, "profile.html", {"message": "Your profile information has been updated"})
    return render(request, "profile.html")


def index(request):
    context = {
        "architecture": Subject.objects.filter(category=1),
        "computing": Subject.objects.filter(category=2),
        "photography": Subject.objects.filter(category=3),
        "business": Subject.objects.filter(category=4)
    }
    return render(request, "index.html", context)


def subject(request, subject):
    context = {
        "courses": Course.objects.filter(subject=subject)
    }
    return render(request, "subject_courses.html", context)


def courses(request):
    context = {
        "courses": Course.objects.all()
    }
    if request.user.is_authenticated:
        return render(request, "user_courses.html", context)
    return render(request, "courses.html", context)


def search(request):
    if request.method == 'GET':
        search = request.GET.get('search_term')
        search_results = Course.objects.filter(name__icontains=search)
        if search_results:
            context = {
                "search": search,
                "results": Course.objects.filter(name__icontains=search)
            }
            return render(request, "search.html", context)
        else:
            return render(request, "empty_search.html", {"search":search})
    else:
        return render(request, "search.html", {})


def enroll(request, course_id):
    try:
        enroll = Course.objects.get(id=course_id)
    except ObjectDoesNotExist:
        return HttpResponse(status=404)
    return render(request, "enroll_confirm.html", {'enroll': enroll})


def enroll_confirm(request, course_id, name, level):
    if not request.user.is_authenticated:
        return render(request, "login.html", {"msg": None})
    current_user = request.user
    data = MyEnrolledCourses()
    data.user_id = current_user.id
    data.course_id = course_id
    data.course_name = name
    data.level = level
    data.save()
    return HttpResponseRedirect(reverse("home"))


def resume_course(request, course_id):
    context = {
        "topics": Topic.objects.filter(course_id=course_id)
    }
    return render(request, "topics.html", context)


def contact_message(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
        contactMessage = ContactMessage()
        contactMessage.name = name
        contactMessage.email = email
        contactMessage.message = message
        contactMessage.save()

        context = {
            "message": "Your message was sent",
            "architecture": Subject.objects.filter(category=1),
            "computing": Subject.objects.filter(category=2),
            "photography": Subject.objects.filter(category=3),
            "business": Subject.objects.filter(category=4)
        }
        return render(request, "index.html", context)
    return render(request, "index.html")


def logout_view(request):
    logout(request)
    return render(request, "login.html", {"msg": "logged out"})


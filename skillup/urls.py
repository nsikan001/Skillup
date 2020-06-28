from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path("subject/<int:subject>", views.subject, name="subject"),
    path("login", views.login_view, name="login"),
    path("signup", views.signup_view, name="signup"),
    path("home", views.home_view, name="home"),
    path("courses", views.courses, name="courses"),
    path("search", views.search, name="search"),
    path("profile", views.profile_view, name="profile"),
    path("edit_profile", views.edit_profile, name="edit_profile"),
    path("contact_message", views.contact_message, name="contact_message"),
    path("enroll/<int:course_id>", views.enroll, name="enroll"),
    path("enroll_confirm/<int:course_id>/<str:name>/<str:level>", views.enroll_confirm, name="enroll_confirm"),
    path("resume_course/<int:course_id>", views.resume_course, name="resume_course"),
    path("admin_area", views.admin_area, name="admin_area"),
    path("manage_courses", views.manage_courses, name="manage_courses"),
    path("edit_course/<int:course_id>", views.edit_course, name="edit_course"),
    path("edited_course/<int:edit_id>", views.edited_course, name="edited_course"),
    path("topics/<int:course_id>", views.topics, name="topics"),
    path("edit_topic/<int:topic_id>", views.edit_topic, name="edit_topic"),
    path("edited_topic/<int:edit_id>", views.edited_topic, name="edited_topic"),
    path("contact_messages", views.contact_messages, name="contact_messages"),
    path("admin_profile", views.admin_profile, name="admin_profile"),
    path("logout", views.logout_view, name="logout")
]
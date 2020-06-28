from django.contrib import admin
from .models import Category, Course, Enrollment, Subject, Instructor, MyEnrolledCourses, Topic, ContactMessage


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Category, CategoryAdmin)


class CourseAdmin(admin.ModelAdmin):
    model = Course
    list_display = ('id', 'name', 'get_category', 'get_subject', 'preview_text', 'level', 'image_url', 'get_instructor')

    def get_category(self, obj):
        return obj.category.name
    get_category.admin_order_field = 'category'
    get_category.short_description = 'Category Name'

    def get_subject(self, obj):
        return obj.subject.name
    get_subject.admin_order_field = 'subject'
    get_subject.short_description = 'Subject Name'

    def get_instructor(self, obj):
        return obj.instructor.fname
    get_instructor.admin_order_field = 'instructor'
    get_instructor.short_description = 'Instructor Name'


admin.site.register(Course, CourseAdmin)


class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')


admin.site.register(Enrollment, EnrollmentAdmin)


class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ['id', 'name', 'get_name', ]

    def get_name(self, obj):
        return obj.category.name
    get_name.admin_order_field = 'category'  
    get_name.short_description = 'Category Name'


admin.site.register(Subject, SubjectAdmin)


class InstructorAdmin(admin.ModelAdmin):
    list_display = ('fname', 'lname', 'email', 'password', 'designation')


admin.site.register(Instructor, InstructorAdmin)


class MyEnrolledCoursesAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'course_name', 'level')


admin.site.register(MyEnrolledCourses, MyEnrolledCoursesAdmin)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')


admin.site.register(ContactMessage, ContactMessageAdmin)


class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'vid_url')


admin.site.register(Topic, TopicAdmin)







# view to url mapping

from . import views
from django.urls import path
app_name = "polls"

urlpatterns = [
    path("main/", views.page, name="my-1st-page"),
    path("question/", views.info, name="question"),
    path("calculate/<int:principle>/<int:months>/<str:rate_of_interest>/", views.calculate, name="calculate"),
    path("simple-inst/<int:principle>/<int:months>/<str:rate_of_interest>/", views.simple_interset, name="simple-inst"),
    path("html/", views.html_render, name="My page"),
    path("my_page/", views.temp_data, name="my_data"),
    # Questions and Choices
    path("index/", views.index, name="questions"),
    path("question/<int:question_id>/", views.choices, name="choices"),

    path("create/question/", views.create_question, name="create-question"),
    path("create/<int:question_id>/choice/", views.create_choice, name="create-choice"),


    path("create/df/question/", views.question_djforms, name="df-create-question"),

    # email
    path("emails/", views.emails, name="all-emails"), # email listing page
    path("email/create", views.create_email, name="create-email"),
    path("email/<int:pk>/", views.email_detail, name="detail-email"),
    path("email/<int:pk>/update/", views.edit_email, name="edit-email"),
]

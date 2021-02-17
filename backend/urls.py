"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from tutor import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('login', views.login),
    path('registration', views.registration),
    path('profile', views.profile),
    path('profile_information', views.profile_information),
    path('forget_password', views.forget_password),
    path('resend_link', views.resend_link),
    path('alluser',views.task),
    path('user/<int:pk>',views.user_api),
    path('allclass',views.class_task),

#login
    path('new_password', views.new_password),
    path('reset_password', views.reset_password),
    # alpha (6th-Feb)
    path('create_class', views.ClassListCreateView.as_view()),
    path('class/<int:pk>/', views.ClassDetailEditDeleteView.as_view()),

#myteachers
    path('in_progress', views.in_progress),
    path('pending_review', views.pending_review),
    path('saved', views.saved),
    path('remove_invite', views.remove_invite),
    path('applied', views.applied),
    path('accept_inv', views.accept_inv),
    path('invite', views.invite),
    path('rate_tutor', views.rate_tutor),
    path('rate_submit', views.rate_submit),

#classes
    path('all_postings', views.all_postings),
    path('post_class', views.post_class),
    path('all_proposals', views.all_proposals),
    path('filter', views.filter),
    path('tutor_profile', views.tutor_profile),
    path('inv_tutor', views.inv_tutor),
    path('send_invite', views.send_invite),
    path('modify_offer', views.modify_offer),
    path('withdraw_offer', views.withdraw_offer),



#messages
    path('messagesText', views.messagesText),

#notification
    path('notification_mess', views.notification_mess),
    path('notification', views.notification),
    path('notification_supp', views.notification_supp),

#support
    path('support_submit', views.support_submit),
    path('support_num', views.support_num),



    path('supp', views.my_ticket),#1
    path('allsupport', views.my_ticket_view),# 1--> views-> (all_support list)
    path('support/<int:pk>', views.my_ticket_view_api),# 1--> views->  (user relevant support list)

    path('allreports/', views.my_reports), #alpha phase
    path('managereports', views.manage_reports), #alpha phase
    path('report/<int:pk>', views.my_report_api), #alpha phase

    path('allconnect/',views.connect_task),
    path('connect/<int:pk>',views.connect_api),
    path('allcnctmsg/',views.connect_msgtask),
    path('connectmsg/<int:pk>',views.connect_msgapi),
    path('allconnectmsgatt/',views.connect_msg_attachtask),
    path('connectmsgatt/<int:pk>',views.connect_msg_Attachapi),

]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

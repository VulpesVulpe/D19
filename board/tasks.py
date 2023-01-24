from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.sites.models import Site
from django.conf import settings
from datetime import datetime, timedelta
from .models import *




@shared_task
def task_send_mail_on_create_post(post_id, user_id):
    domain = Site.objects.get_current().domain
    post = Post.objects.get(pk=post_id)
    user = User.objects.get(pk=user_id)
    path = post.get_absolute_url()
    html_content = render_to_string(
        'post_created_mail.html',
        {
            'username': user.username,
            'message': post.text[:50] + '...',
            'post_url': f'http://{domain}:8000{path}',
        }
    )
    msg = EmailMultiAlternatives(
        subject=f'{post.title}',
        body=post.text[:50] + '...',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],  # это то же, что и recipients_list
    )
    msg.attach_alternative(html_content, "text/html")  # добавляем html
    msg.send()
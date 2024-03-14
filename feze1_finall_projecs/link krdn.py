from django.contrib import admin
from .models import FriendlyLink

admin.site.register(FriendlyLink)
from django.db import models

class FriendlyLink(models.Model):
    title = models.CharField(max_length=100, default='', verbose_name='title')
    url = models.CharField(max_length=100, default='', verbose_name='url')

    class Meta:
        verbose_name_plural = 'links'

    def __str__(self):
        return self.title
    

    
from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^links$', views.friendly_link, name='friendly_link'),
]
{% extends "base.html" %}

{% block title %}Links{% endblock %}

{% block content %}
<ul>
  {% for link in friendly_link %}
  <li><a href="{{ link.url }}">{{ link.title }}</a></li>
  {% empty %}
  {% endfor %}
</ul>
{% endblock %}




{% load i18n static %}<!DOCTYPE html>
<html>
<head>
...
</head>
<body>
...
{% block content %}{% endblock %}

<footer>
<ul>
  <!--This code doesn't work-->
  {% for link in friendly_link %}
  <li><a href="{{ link.url }}">{{ link.title }}</a></li>
  {% empty %}
  {% endfor %}
</ul>
</footer>
...
from django.contrib import admin
from .models import Artist, Music, Comment, Person
# Register your models here.

admin.site.register(Artist)
admin.site.register(Music)
admin.site.register(Comment)
admin.site.register(Person)

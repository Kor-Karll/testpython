from django.db import models

#from __future__ import unicode_literals
#from django.urls.encoding import python_2_unicode_compatible

from django.db import models
from django.core.urlresolvers import reverse
from tagging.fields import TagField


# Create your models here.

#@python_2_unicode_compatible
class Post(models.Model):
        title       = models.CharField('TITLE', max_length=50)
        slug        = models.SlugField('SLUG', unique=True, allow_unicode=True, help_text='one word for title alias.')
        description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple desciption text.')
        content     = models.TextField('CONTENT')
        create_date = models.DateTimeField('Create Date', auto_now_add=True)
        modify_date = models.DateTimeField('Modify Date', auto_now=True)

        # TagField 는 CharField를 상속받는다 디폴트(max_length=255,Blank=True)
        tag         = TagField()

        class Meta:
            verbose_name = 'post'
            verbose_name_plural = 'posts'
            db_table = 'my_post'
            ordering = ('-modify_date',)

        def __str__(self):
            return self.title

        def get_absolute_url(self):
            return reverse('blog2:post_detail', args=(self.slug,))

        def get_previous_post(self):
            return self.get_previous_by_modify_date()

        def get_next_post(self):
            return self.get_next_by_modify_date()

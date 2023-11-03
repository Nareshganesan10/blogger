from django.db import models

class BlogModel(models.Model):
    id = models.AutoField(primary_key=True)
    blog_content = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class CommentModel(models.Model):
    blog_id = models.ForeignKey(BlogModel,on_delete=models.CASCADE)
    comment = models.TextField()
    posted_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.blog_id, self.comment
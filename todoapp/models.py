from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField(default=1) # 디폴트값을 지정해주므로 마이그레이션에서 값 지정해 줄 필요없이 지나감
    due_date = models.DateTimeField(null=True, blank=True) # 빈값 허용 하므로 위와 마찬가지로 지나감

    def __str___(self):
        return self.title


class TodoStatusHistory(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    previous_status = models.BooleanField()
    new_status = models.BooleanField(default=False)
    changed_at = models.DateTimeField(auto_now_add=True)

class TodoComment(models.Model):
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
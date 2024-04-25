from django.db import models

CHOICE_PRIORITY = (
    (0, 'Alto'),
    (1, 'Médio'),
    (2, 'Baixo'),
)

class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    created_at = models.DateField(auto_now_add=True)
    priority = models.IntegerField(choices=CHOICE_PRIORITY)
    status = models.BooleanField(default=True)
    limite_date = models.DateField()

    
    def __str__(self):
        return self.name
    
    
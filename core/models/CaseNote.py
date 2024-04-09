from django.db import models

from core.models import Case, User


class CaseNote(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE, related_name='case_notes')
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='worker_notes')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    note = models.TextField()

    def __str__(self):
        return f'{self.worker.fullname}\'s note for {self.case}'

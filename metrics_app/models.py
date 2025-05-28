from django.db import models
from ansible_base.lib.abstract_models import CommonModel

class Metric(CommonModel):
    service = models.CharField(max_length=32)
    payload = models.JSONField(default=dict)
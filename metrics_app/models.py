from django.db import models
from ansible_base.lib.abstract_models import CommonModel

class Metric(CommonModel):
    SERVICE_CHOICES = [
        ('controller', 'Controller'),
        ('worker', 'Worker'),
        ('database', 'Database'),
        ('api_gateway', 'API Gateway'),
        ('scheduler', 'Scheduler'),
    ]
    
    service = models.CharField(max_length=32, choices=SERVICE_CHOICES)
    payload = models.JSONField(default=dict)
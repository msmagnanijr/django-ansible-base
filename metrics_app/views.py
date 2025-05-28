from rest_framework.viewsets import ModelViewSet
from ansible_base.lib.utils.views.ansible_base import AnsibleBaseView
from .models import Metric
from .serializers import MetricSerializer

class MetricViewSet(ModelViewSet, AnsibleBaseView):
    queryset = Metric.objects.all()
    serializer_class = MetricSerializer
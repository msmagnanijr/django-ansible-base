from ansible_base.lib.serializers.common import NamedCommonModelSerializer
from .models import Metric

class MetricSerializer(NamedCommonModelSerializer):
    class Meta:
        model = Metric
        fields = '__all__'
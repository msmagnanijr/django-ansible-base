import pytest
import time
from metrics_app.models import Metric

@pytest.mark.django_db
def test_create_metric_default_payload():
    result = Metric.objects.create(service="test")
    result.save()
    assert result.payload == dict()

@pytest.mark.django_db
def test_modifying_metric_updates_modified_time():
    metric = Metric.objects.create(service="test")
    original_modified = metric.modified
    
    time.sleep(0.1)
    metric.payload = {"updated": True}
    metric.save()
    
    assert metric.modified > original_modified

@pytest.mark.django_db
def test_metric_service_required():
    with pytest.raises(Exception):
        Metric.objects.create()
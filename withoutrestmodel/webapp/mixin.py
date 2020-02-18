from django.core.serializers import serialize
import json
from django.http import HttpResponse
class SerializeMixin(object):
    def serialize(self,qs):
        json_data = serialize('json', qs)
        p_data = json.loads(json_data)
        final_data=[]
        for obj in p_data:
            emp_data = obj['fields']
            final_data.append(emp_data)
        json_data= json.dumps(final_data)
        return json_data


class HttpResponseMixin(object):
    def render_to_http_response(self,json_data, status_code=200):
        return HttpResponse(json_data, content_type='application/json')

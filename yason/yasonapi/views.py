from rest_framework.parsers import JSONParser
from rest_framework_yaml.parsers import YAMLParser
from django.http.response import HttpResponse, JsonResponse
from rest_framework.decorators import parser_classes
from rest_framework.decorators import api_view
from rest_framework import status

import yaml
import json

@api_view(['POST'])
# API Method - Function that converts YAML to  JSON
@parser_classes([YAMLParser])
def yaml_to_json(request):
    received_yaml =  yaml.safe_load(request)
    transformed = json.dumps(received_yaml, indent=2)
    return HttpResponse(transformed)

@api_view(['POST'])
# API Method - Function that converts JSON to YAML
@parser_classes([JSONParser])
def json_to_yaml(request, format=None):
    json_received = request.data
    return HttpResponse(yaml.dump(json_received, sort_keys=False, default_flow_style=False))

@api_view(['GET'])
# API method - Health check
def getHealth(request):
    return JsonResponse({"Health": "Everything is OK"}, status=status.HTTP_200_OK)
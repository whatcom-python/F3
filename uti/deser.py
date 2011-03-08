from django.core import serializers

JSONSerializer = serializers.get_serializer("json")
json_serializer = JSONSerializer()

# hacks abound
for obj in serializers.deserialize("json", open('uti/f3_final.json', 'r')):
    obj.save()

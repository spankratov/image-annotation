import jsonschema.exceptions
from images.models import Image
from jsonschema import validate
from rest_framework import serializers


class AnnotationValidateMixin:
    annotation_schema = Image.annotation_schema

    def validate_annotation(self, value):
        print("Validation begin")
        try:
            if value:
                print("Validation end")
                validate(value, self.annotation_schema)
        except jsonschema.exceptions.ValidationError as e:
            raise serializers.ValidationError(e.message)
        return value


class ImageCreateSerializer(serializers.ModelSerializer,
                            AnnotationValidateMixin):
    annotation = serializers.JSONField(required=False)

    class Meta:
        model = Image
        fields = ['id', 'file', 'annotation']


class ImageUpdateSerializer(serializers.ModelSerializer,
                            AnnotationValidateMixin):
    class Meta:
        model = Image
        fields = ['id', 'annotation']


class ImageRetrieveSerializer(serializers.ModelSerializer):
    annotation = serializers.SerializerMethodField()

    class Meta:
        model = Image
        fields = ['id', 'file', 'annotation']

    def get_annotation(self, obj):
        if self.context['annotation_format'] == 'export':
            return obj.export_annotation
        else:
            return obj.annotation


class ImageURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'file']

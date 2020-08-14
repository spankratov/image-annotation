from django.db import models
from images.schemas import IMAGE_ANNOTATION_SCHEMA
from images.utils import default_annotation
from randomfilestorage.storage import RandomFileName


class Image(models.Model):
    file = models.ImageField(
        upload_to=RandomFileName('images/'),
    )

    annotation_schema = IMAGE_ANNOTATION_SCHEMA
    annotation = models.JSONField(default=default_annotation)

    @property
    def export_annotation(self):
        labels = []
        for label in self.annotation['labels']:
            if label['meta']['confirmed']:
                labels.append({
                    'id': label['id'],
                    'class_id': label['class_id'],
                    'surface': ''.join(label['surface']),
                })
        return {'labels': labels}

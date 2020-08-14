import os
import uuid

from django.utils.deconstruct import deconstructible


@deconstructible
class RandomFileName:
    def __init__(self, path):
        self.path = path

    def __call__(self, _, filename):
        extension = os.path.splitext(filename)[1]
        filename = uuid.uuid4()
        return f'{self.path}{filename}{extension}'

# Image annotation project
Simple test project: Django application with API for images and their annotations.

## Running
1. [Install Docker](https://docs.docker.com/get-docker/)
2. Run `docker-compose up` from project directory
3. Locally send API requests to `http://localhost:8000` (no authentication required for simplicity)

## API
1. Create image: `curl -v -F file=@yugz2apjanp41.png -F annotation='{"labels": {}}' http://localhost:8000/images/`
2. Update image annotation: `curl -H 'Content-Type: application/json' -X PUT -d '{"annotation": {"labels": []}}' http://localhost:8000/images/8/`
3. Get image data (url and annotation): `curl -X GET "http://localhost:8000/images/8/"`
4. Get image data in export format: `curl -X GET "http://localhost:8000/images/8/?format=export"`
5. Get image url: `curl -X GET "http://localhost:8000/images/8/url/"`

## Architecture
This project uses specific schema for image annotations (defined in `images.schemas.IMAGE_ANNOTATION_SCHEMA`). Main question during development was how to store this annotation.

We can use two different approaches: store everything as plain json or create separate tables for each entity in annotation. 

Reasons to store annotation in json field:
1. Annotations are self-contained (no links between images) and operated on the whole (document approach), not by specific labels (RDBMS approach).
2. Annotations are relatively small (up to 100 labels) and all operations can be easily done in-memory by Python.
3. No need for complex cross-image joins, aggregation or even gathering annotations for all images (e.g. for list view).
4. Easy writing and updating.

Should project requirement change, database schema must be migrated to separate tables to store annotation.

## Tests
Run `python manage.py test` inside `backend` container
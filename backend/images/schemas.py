IMAGE_ANNOTATION_SCHEMA = {
  "type": "object",
  "properties": {
    "labels": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "meta": {
            "type": "object",
            "properties": {
              "confirmed": {"type": "boolean"},
              "confidence_percent": {"type":  "number"},
            },
            "required": ["confirmed", "confidence_percent"],
            "additionalProperties": False,
          },
          "id": {"type": "string"},
          "class_id": {"type": "string"},
          "surface": {
            "type": "array",
            "items": {"type": "string"},
          },
          "shape": {
            "type": "object",
            "properties": {
              "endX": {"type": "number"},
              "endY": {"type": "number"},
              "startX": {"type": "number"},
              "startY": {"type": "number"},
            },
            "required": ["endX", "endY", "startX", "startY"],
            "additionalProperties": False,
          },
        },
        "required": ["meta", "id", "class_id", "shape"],
        "additionalProperties": False,
      },
    },
  },
  "required": ["labels"],
  "additionalProperties": False,
}

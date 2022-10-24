"""
Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
SPDX-License-Identifier: MIT-0
"""

import json
from transformers import pipeline

nlp = pipeline(model = "jairojg/true")

def handler(event, context):

    response = nlp(event['text'])[0]

    if response["label"] == "LABEL_0":
        response["label"] = "FAKE"
    else:
        response["label"] = "TRUE"

    response = {
        "statusCode": 200,
        "body": response
    }

    return response
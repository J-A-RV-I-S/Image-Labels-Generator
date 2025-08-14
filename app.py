from flask import Flask, request, render_template
import boto3
import os
import uuid

app = Flask(__name__)

BUCKET_NAME = 'image-labels-generator-jarvis'
s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')

@app.route('/', methods=['GET', 'POST'])
def index():
    labels = []
    image_url = None

    if request.method == 'POST':
        image = request.files['image_file']
        filename = f"{uuid.uuid4().hex}_{image.filename}"
        image.save(filename)

        # Upload to S3
        s3.upload_file(filename, BUCKET_NAME, filename)

        # Set public read permission
        # s3.put_object_acl(ACL='public-read', Bucket=BUCKET_NAME, Key=filename)

        # Rekognition
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': BUCKET_NAME, 'Name': filename}},
            MaxLabels=10,
            MinConfidence=75
        )

        labels = response['Labels']
        image_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{filename}"

        os.remove(filename)

    return render_template('index.html', labels=labels, image_url=image_url)

if __name__ == '__main__':
    app.run(debug=True)

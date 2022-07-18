from io import BytesIO
from flask import request, send_file
from . import routes
from PIL import Image

from config.s3Config import AWS_S3_BUCKET_NAME
from config.connection import s3_connection


# PIL 이미지를 http로 전송하는 함수
def serve_pil_image(pil_img):
    img_io = BytesIO()
    print(pil_img.format)
    pil_img.save(img_io, pil_img.format, quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/' + pil_img.format)


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
s3 = s3_connection()


@routes.route('/image', methods=['post'])
def post_image():
    file = request.files['file']
    file.name = 'poodle.png'
    print('header: ', file.headers, '\n')
    print('content-type:', file.content_type, '\n')

    s3.Bucket(AWS_S3_BUCKET_NAME).put_object(
        Body=file,
        Key='puppy/' + file.name,
        ContentType=file.content_type
    )
    response = 'ok'
    return response


@routes.route('/image', methods=['get'])
def get_image():
    bucket = s3.Bucket(AWS_S3_BUCKET_NAME)
    object = bucket.Object('puppy/poodle.jpg')
    response = object.get()
    file_stream = response['Body']
    img = Image.open(file_stream)

    return serve_pil_image(img)
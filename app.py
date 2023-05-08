from flask import Flask, request, send_file, render_template
from minio import Minio
import os
import io
import mimetypes
# from flask import Flask, redirect, url_for, render_template, request, flash
app = Flask(__name__)

# from minio.error import ResponseError
BUCKET_NAME = 'mybuck'
minio_client = Minio("localhost:9000",  # Change to local MinIO server address
    access_key='jBP6NcORieFWKUmk',
    secret_key='OT0ukyrWW2EJfKt3GQd7xX8cMQoesL9H',
    secure=False)
# Create client with secure connection to a locally running MinIO server.
@app.route('/upload', methods=['POST'])
def upload():
       
    try:
        minio_client.make_bucket(BUCKET_NAME)
    except:
        pass
    
    file = request.files['file']
    filename = file.filename
    print("--"*20)
    print(filename)
    print("--"*20)
    file_data = io.BytesIO(file.stream.read())
    minio_client.put_object(
        bucket_name=BUCKET_NAME,
        object_name=filename,
        data=file_data,
        length=len(file_data.getbuffer()),
        content_type=file.content_type,
    )
    

    return f'File uploaded to MinIO! {filename} '


@app.route('/download/<filename>')
def download(filename):
    try:
        data = minio_client.get_object(
            bucket_name=BUCKET_NAME,
            object_name=filename,
        )
        
        # determine the MIME type of the file
        mime_type, _ = mimetypes.guess_type(filename)
        return send_file(
            io.BytesIO(data.read()),
            as_attachment=True,
            download_name=filename,
            mimetype=mime_type
        )
    except Exception as e:
        return f'File not found in MinIO!  {e}'
# @app.route('/')
# def index():
#     return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

# Minio File Upload using Flask

This project demonstrates how to use Flask and Minio together to upload files to a local Minio instance. The application allows users to upload files and view the list of files that have been uploaded.

## Installation

To install the project, clone the repository and navigate to the project directory:
```bash
git clone https://github.com/oyekamal/minio-file-upload-using-flask.git

cd minio-file-upload-using-flask 
```
    
Run the minio.

```bash
docker-compose up --build
```
Minio is running with follwoing username and password.
```bash
localhost:9001
username: minioadmin
password: minioadmin
```

Install and run the flask app. 
```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python app.py
```

Use Postman for uploading file using follwoing url.
```bash
localhost:5000/upload
```

Use Postman for retriving file using follwoing url.
```bash
localhost:5000//download/<filename>
```
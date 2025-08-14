# 🖼️ Image Labels Generator 🔍  

![Python](https://img.shields.io/badge/Python-3.9+-blue?logo=python)  
![AWS](https://img.shields.io/badge/AWS-S3%20%7C%20Rekognition-orange?logo=amazon-aws)  
![Flask](https://img.shields.io/badge/Flask-2.x-black?logo=flask)  


A simple **Flask web application** that lets users upload an image, store it in **Amazon S3**, and automatically detect labels using **AWS Rekognition**. The results include object names, scenes, and confidence scores, all displayed on the web page.

---

## 🚀 Features
✅ Upload any image from your device.  
✅ Store the image securely in **AWS S3**.  
✅ Detect objects and scenes using **AWS Rekognition**.  
✅ Display labels with **confidence scores**.  
✅ Automatically remove temporary files from the server.  

---

## 🛠️ Tech Stack
- **Python (Flask)**
- **AWS S3** – Cloud storage for uploaded images.
- **AWS Rekognition** – Image analysis.
- **Boto3** – AWS SDK for Python.
- **HTML/CSS** – Simple frontend interface.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/image-labels-generator.git
cd image-labels-generator.

```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt

```

### 3️⃣ AWS Setup
- **Create S3 Bucket:** 
    - Go to AWS S3 console → "Create Bucket". 
    - Enable public object access or configure CloudFront.
- **Create IAM User:**
    - **Assign Permission:**
        - s3:PutObject, s3:GetObject
        - rekognition:DetectLabels
- **Configure AWS CLI:**
```bash
aws configure

```
### 4️⃣ Run the Application
```bash
python app.py

```

### 🖥️ How It Works
User uploads an image via the HTML form.

The image is stored temporarily on the server.

Boto3 uploads it to S3.

Rekognition detects labels and confidence scores.

Results + uploaded image are displayed.

Local temp file is deleted.

### 🏗️ Architecture Diagram
![Image Labels Generator Flow](images/flow-diagram.png)

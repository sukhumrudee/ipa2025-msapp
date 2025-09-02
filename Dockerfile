# ใช้ Python 3.12.3 official image
FROM python

# ตั้ง working directory
WORKDIR /app

# คัดลอกไฟล์ทั้งหมดเข้ามาใน container
COPY . .

# ติดตั้ง Flask
RUN pip install flask -r requirements.txt

# เปิดพอร์ต 8080
EXPOSE 8080

# สั่งรันแอป
CMD ["python", "app.py"]

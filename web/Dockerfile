FROM python:3.12-slim

WORKDIR /app

# ลดขนาด layer และติดตั้งแค่ที่ต้องใช้
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080
CMD [ "python", "app.py" ]

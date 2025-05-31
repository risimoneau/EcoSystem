FROM python:3.12
WORKDIR /EcoSystem
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY model.h5 .
COPY inferance.py .
COPY train_model.py .
CMD ["python", "inferance.py"]
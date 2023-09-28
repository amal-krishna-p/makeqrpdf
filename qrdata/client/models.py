from django.db import models

# Create your models here
class client_data(models.Model):
    username=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    photo=models.ImageField(upload_to="Client_data")
    status=models.BooleanField(default=False)

class client_info(models.Model):
    address=models.CharField(max_length=15)
    district=models.CharField(max_length=15)
    phone=models.CharField(max_length=15)
    city=models.CharField(max_length=15)
    aadhar=models.CharField(max_length=15)
    dob=models.DateField(null=True,blank=True,default=None)
    client=models.ForeignKey(client_data,on_delete=models.CASCADE)

class clientdocument(models.Model):
    pdfdata=models.FileField(upload_to="documents",null=True,blank=True)
    qrdata=models.ImageField(upload_to="qrcode",null=True,blank=True)
    client=models.ForeignKey(client_info,on_delete=models.CASCADE)
    

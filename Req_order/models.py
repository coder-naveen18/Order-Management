from django.db import models

# Create your models here.
class request_order(models.Model):
    
    Category = [
        ('books','Books'),
        ('sports', 'Sports'),
        ('stationary','Stationary'),
        ('electronic', 'electronic-items')
        
    ]
    
    books = [
        ('fiction-novels', 'Fictional-Novel'),
        ('non-fiction', 'Non-Fictional'),
        ('textbooks','Textbooks'),
        ('comic', 'Comic Books/Graphic Novels'),
        ('cook','Cookbooks'),
        
    ]
    
    sports = [
        ('balls','Balls'),
        ('bats','Bats-Racquets'),
        ('apparel','Apparels'),
        ('protective','Protective-Gears'),
        ('equipment','Equipments')
    ]
    
    stationary = [
        ('writing', 'Writing'),
        ('paper', 'Paper'),
        ('desk', 'Desk'),
        ('art', 'Art')
    ]
    
    electronic = [
        ('personal','Personal'),
        ('audio/video','Audio/Video'),
        ('computer','Computer'),
        ('accessories','Accessories')
    ]
    
    
    
    
    
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=10)
    pincode = models.CharField(max_length=6)
    type = models.CharField(max_length=20, choices=Category)
    ITEM_CHOICES = books + sports + stationary + electronic
    items = models.CharField(max_length=30, choices=ITEM_CHOICES)
    item_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='req_items/')
    description = models.TextField()
    
    
    def __str__(self):
        return self.name
    
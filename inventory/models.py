from django.db import models

# Create your models here.

units_status = (
    ('kg', 'kg'),
    ('litre', 'litre'),
    ('millilitre', 'millilitre'),
    ('cartons', 'cartons'),
    ('metre', 'metre'),
    ('gram', 'gram'),
    ('piece', 'piece'),
    ('centimetre', 'centimetre'),
    ('feet', 'feet'),
    ('ropani', 'ropani'),
    ('aana', 'squarefeet'),
    ('squarefeet', 'aana'),
)


class SupplierData(models.Model):
    name = models.CharField(max_length=99)
    contact = models.CharField(max_length=99, unique=True)
    email = models.EmailField(null=True)
    address = models.CharField(max_length=99, null=True)

    def __str__(self):
        return self.name
    
    
    
class Supply(models.Model):
    product_name = models.CharField(max_length=99)
    price = models.IntegerField()
    unit = models.CharField(choices=units_status,max_length=99)
    unit_value = models.IntegerField()
    supplier = models.ForeignKey(SupplierData, related_name='supply', on_delete=models.CASCADE ,null=True)
    
    def __str__(self):
        return self.product_name

        

class SupplyIssue(models.Model):
    issue_item = models.ForeignKey(Supply, on_delete=models.CASCADE)

    def __str__(self):
        data = "Issue #" + str(self.id) + " - " + str(self.issue_item)
        return data

    
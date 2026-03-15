from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProjectLawModel(models.Model):

    CompanyOne = [
        ('JC Attorneys ','JC Attorneys '),
        ('Daniel Thiery','Daniel Thiery '),
        ('Wright Rose-Innes','Wright Rose-Innes'),
        ('Yammin Hammond Inc','Yammin Hammond Inc'),
    ]

    TypeOfDocuments = [
        ('ClientInTakeForm','Client In Take Form'),
        ('ClientEngagementLetter','Client Engagement Letter'),
        ('ParalegalInvoice','Paralegal Invoice'),
        ('Non-disclosureAgreement','Non-disclosure Agreement'),
        ('MarketingDocuments','Marketing Documents'),
    ]

    TheUser = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    TheClient = models.CharField( max_length=50)
    TheCompany = models.CharField(choices=CompanyOne, max_length=50)
    TheFile = models.FileField(upload_to='documents')

    def __str__(self):
        return self.TheCompany
from django.db import models
from tracking.models import Visitor

class VisitorTotalManager(models.Manager):
    
    def create_total(self):
        """
        Create VisitorTotal record from the tracking.models.Visitor
        get the sum of users and page views from all Visitor instances
        """
        visitors = Visitor.objects.all()
        total_user_count = 0;
        total_page_view_count = 0;
        for visitor in visitors:
            total_user_count += 1
            total_page_view_count += visitor.page_views
        
        # create a new record
        visitorTotal = VisitorTotal(total_user=total_user_count, total_page_view=total_page_view_count)
        visitorTotal.save()
        return visitorTotal

class VisitorTotal(models.Model):
    class Meta:
        ordering = ('-date',)
        verbose_name = 'Total Number of Visitor'
    
    date = models.DateField(auto_now=True)
    total_user = models.PositiveIntegerField(default=0)
    total_page_view = models.PositiveIntegerField(default=0)
    
    objects = VisitorTotalManager()
    
"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from tracking.models import Visitor
from django.contrib.auth.models import User
import datetime
from models import VisitorTotal
import random

class ModelTest(TestCase):
    def setUp(self):
        
        user = User.objects.create_user("test_user", "test@gmail.com", "1234")
        user2 = User.objects.create_user("test_user2", "test2@gmail.com", "1234")
        user3 = User.objects.create_user("test_user3", "test3@gmail.com", "1234")
        self._create_visitor(user, 12, "192.168.1.11")
        self._create_visitor(user2, 20, "192.168.1.12")
        self._create_visitor(user3, 44, "192.168.1.13")
        
    def _create_visitor(self, user, page_views, ip_address):
        visitor = Visitor(
            user=user,
            url="/",
            page_views=page_views,
            session_start=datetime.datetime.now(),
            last_update=datetime.datetime.now(),
            ip_address = ip_address,
            session_key = random.randrange(1000000, 9999999999, 2)
            )
        visitor.save()
        return visitor
        
    def test_insert_total(self):
        """
        Tests that visitor count is copied to the VisitorTotal table
        """
        total = VisitorTotal.objects.create_total()
        
        self.assertEqual(3, total.total_user)
        self.assertEqual(12+20+44, total.total_page_view)

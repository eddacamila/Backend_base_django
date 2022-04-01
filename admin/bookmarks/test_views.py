from django.test import TestCase

# Create your tests here.

from .models import Bookmark, User
from django.urls import reverse

class BookmarkListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        user=User.objects.create(username='test', email='test@test.com', password='None@')
        #Create 13 authors for pagination tests
        number_of_bookmarks = 13
        for bookmark_num in range(number_of_bookmarks):
            Bookmark.objects.create(title ='Bookmark %s' % bookmark_num, url = 'bookmark%s@test.com' % bookmark_num, status='public', user=user)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/api/bookmarks')
        self.assertEqual(resp.status_code, 200)
        
    def test_view_for_crated_objets(self):
        resp = self.client.get('/api/bookmarks')
        print (resp.json()[0])
        self.assertEqual(len(resp.json()), 13)
        
    def test_view_for_crated_objets(self):
        bookmarktest={'title': 'Bookmark 0', 'url': 'bookmark0@test.com'}
        resp = self.client.get('/api/bookmarks')
        bookmarkresp=resp.json()[0]
        self.assertEqual(bookmarkresp['title'], bookmarktest['title'])
        self.assertEqual(bookmarkresp['url'], bookmarktest['url'])
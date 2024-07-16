from django.test import TestCase
from django.contrib.auth.models import User
from .models import New
from django.shortcuts import reverse


class MyTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='user69')
        cls.post69 = New.objects.create(
            title='titlr69',
            text='text69',
            authors=cls.user,
            status=New.MODES_OF_SAVING[0][0],
        )
        cls.post85 = New.objects.create(
            title='titl444reretet',
            text='lorem ipsjdnsfn',
            authors=cls.user,
            status=New.MODES_OF_SAVING[1][0],
        )

    def test_newagepost_str(self):
        pos = self.post85
        self.assertEqual(str(pos), pos.title)  #test mohem

    def test_herepostdate(self):
        self.assertEqual(self.post69.title, 'titlr69')
        self.assertEqual(self.post69.text, 'text69')

    def test_url(self): #hatman test ha ba test_ shoro shand
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_name(self):
        response = self.client.get(reverse('new_post'))
        self.assertEqual(response.status_code, 200)

    def test_justtitle(self):
        response = self.client.get(reverse('new_post'))
        self.assertContains(response, self.post69.title)

    def test_naame(self):
        response = self.client.get(f'/blog/{self.post69.id}/')
        self.assertEqual(response.status_code, 200)

    def test_detail_byname(self):
        response = self.client.get(reverse('new_pos', args=[self.post69.id]))
        self.assertEqual(response.status_code, 200)


    def test_detail(self):
        response = self.client.get(reverse('new_pos', args=[self.post69.id]))
        self.assertContains(response, self.post69.title)
        self.assertContains(response, self.post69.text)

    def test_eror404(self):
        response = self.client.get(reverse('new_pos', args=[909])) #test mohem
        self.assertEqual(response.status_code, 404)

    def test_notshowinfdraft(self):
        response = self.client.get(reverse('new_post'))
        self.assertContains(response, self.post69.title)
        self.assertNotContains(response, self.post85.title)

    def test_creation(self):
        response = self.client.post(reverse('creation'), {
            'title': 'new title',
            'text': 'new fuckin text',
            'status': 'pub',
            'authors': self.user.id,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(New.objects.last().title, 'new title')
        self.assertEqual(New.objects.last().text, 'new fuckin text')

    def test_updating(self):
        response = self.client.post(reverse('update', args=[self.post85.id]), {
            'title': 'title up to date',
            'text': 'text has updated',
            'status': 'pub',
            'authors': self.post85.authors.id,  # ya self.user.id
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(New.objects.last().title, 'title up to date')
        self.assertEqual(New.objects.last().text, 'text has updated')

    def test_delting(self):
        response = self.client.post(reverse('dil', args=[self.post69.id]))
        self.assertEqual(response.status_code, 302)



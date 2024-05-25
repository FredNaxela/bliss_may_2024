# main/tests.py
from .models import Banner, Services, Price, Blog, About, Reviews, Contact, Session
from django.test import TestCase, RequestFactory
from django.urls import reverse
from .views import IndexView
from .forms import ContactForm, SessionForm


# models tests
class ModelsTestCase(TestCase):
    def setUp(self):
        self.banner = Banner.objects.create(description='Test description', sort=1)
        self.service = Services.objects.create(name='Test service', description='Test description', sort=1)
        self.price = Price.objects.create(name='Test price', description='Test description', price=100, sort=1)
        self.blog = Blog.objects.create(name='Test blog', date='2024-05-25', description='Test description', sort=1)
        self.about = About.objects.create(name='Test about', description='Test description', sort=1)
        self.review = Reviews.objects.create(name='Test review', description='Test description', sort=1)
        self.contact = Contact.objects.create(name='Test contact', phone='+380123456789', email='test@example.com',
                                              message='Test message')
        self.session = Session.objects.create(name='Test session', phone='+380123456789', email='test@example.com',
                                              procedure='Test procedure', date='2024-05-25', time='12:00')

    def test_banner_model(self):
        self.assertEqual(self.banner.description, 'Test description')
        self.assertEqual(self.banner.sort, 1)

    def test_services_model(self):
        self.assertEqual(self.service.name, 'Test service')
        self.assertEqual(self.service.description, 'Test description')
        self.assertEqual(self.service.sort, 1)

    def test_price_model(self):
        self.assertEqual(self.price.name, 'Test price')
        self.assertEqual(self.price.description, 'Test description')
        self.assertEqual(self.price.price, 100)
        self.assertEqual(self.price.sort, 1)

    def test_blog_model(self):
        self.assertEqual(self.blog.name, 'Test blog')
        self.assertEqual(self.blog.date, '2024-05-25')
        self.assertEqual(self.blog.description, 'Test description')
        self.assertEqual(self.blog.sort, 1)

    def test_about_model(self):
        self.assertEqual(self.about.name, 'Test about')
        self.assertEqual(self.about.description, 'Test description')
        self.assertEqual(self.about.sort, 1)

    def test_reviews_model(self):
        self.assertEqual(self.review.name, 'Test review')
        self.assertEqual(self.review.description, 'Test description')
        self.assertEqual(self.review.sort, 1)

    def test_contact_model(self):
        self.assertEqual(self.contact.name, 'Test contact')
        self.assertEqual(self.contact.phone, '+380123456789')
        self.assertEqual(self.contact.email, 'test@example.com')
        self.assertEqual(self.contact.message, 'Test message')

    def test_session_model(self):
        self.assertEqual(self.session.name, 'Test session')
        self.assertEqual(self.session.phone, '+380123456789')
        self.assertEqual(self.session.email, 'test@example.com')
        self.assertEqual(self.session.procedure, 'Test procedure')
        self.assertEqual(self.session.date, '2024-05-25')
        self.assertEqual(self.session.time, '12:00')


# views tests
class IndexViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_index_view_get(self):
        Banner.objects.create(description='Banner 1', sort=1)
        Services.objects.create(name='Service 1', description='Service description', sort=1)
        About.objects.create(name='About us', description='About description', sort=1)
        Price.objects.create(name='Price 1', description='Price description', price=100, sort=1)
        Reviews.objects.create(name='Review 1', description='Review description', sort=1)
        Blog.objects.create(name='Blog 1', date='2024-05-25', description='Blog description', sort=1)

        request = self.factory.get(reverse('main:index'))
        response = IndexView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('banner' in response.context_data)
        self.assertTrue('services' in response.context_data)
        self.assertTrue('about' in response.context_data)
        self.assertTrue('price' in response.context_data)
        self.assertTrue('reviews' in response.context_data)
        self.assertTrue('blog' in response.context_data)
        self.assertTrue('contact_form' in response.context_data)
        self.assertTrue('session_form' in response.context_data)

    def test_index_view_post_contact_form_valid(self):
        data = {'submit_contact_form': 'submit', 'name': 'Test User', 'phone': '123456789', 'email': 'test@example.com',
                'message': 'Test message'}
        response = self.client.post(reverse('main:index'), data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('contact_form' in response.context)

        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your message was sent successfully!')

    def test_index_view_post_contact_form_invalid(self):
        data = {'submit_contact_form': 'submit', 'name': '', 'phone': '123', 'email': 'invalid_email', 'message': ''}
        response = self.client.post(reverse('main:index'), data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('contact_form' in response.context)

        contact_form = response.context['contact_form']
        self.assertFalse(contact_form.is_valid())
        self.assertTrue(contact_form.errors)

        messages = list(response.context['messages'])
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Please correct the errors.')


# forms tests
class ContactFormTestCase(TestCase):
    def test_valid_contact_form(self):
        data = {'name': 'Test User', 'phone': '+380123456789', 'email': 'test@example.com', 'message': 'Test message'}
        form = ContactForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_contact_form(self):
        data = {'name': '', 'phone': '123', 'email': 'invalid_email', 'message': ''}
        form = ContactForm(data=data)
        self.assertFalse(form.is_valid())


class SessionFormTestCase(TestCase):
    def test_valid_session_form(self):
        data = {'name': 'Test User', 'phone': '+380123456789', 'email': 'test@example.com',
                'procedure': 'Test Procedure', 'date': '2024-05-25', 'time': '12:00', 'message': 'Test message'}
        form = SessionForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_session_form(self):
        data = {'name': '', 'phone': '123', 'email': 'invalid_email',
                'procedure': '', 'date': '', 'time': '', 'message': ''}
        form = SessionForm(data=data)
        self.assertFalse(form.is_valid())
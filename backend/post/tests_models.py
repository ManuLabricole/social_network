from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from account.models import User
from .models import Post, PostAttachment


class PostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            name='testuser',
            email="test@gmail.com",
            password='testpassword')
        self.post = Post.objects.create(
            author=self.user,
            title='Test Post',
            body='This is a test post.'
        )

    def test_post_creation(self):
        self.assertEqual(self.post.__str__(), 'Test Post')
        self.assertEqual(self.post.author, self.user)
        self.assertEqual(self.post.title, 'Test Post')
        self.assertEqual(self.post.body, 'This is a test post.')


class PostAttachmentModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            name='testuser', 
            email="test@gmail.com",
            password='testpassword')
        self.image = SimpleUploadedFile(
            'test_image.jpg', b'file_content', content_type='image/jpeg')
        self.attachment = PostAttachment.objects.create(
            image=self.image,
            created_by=self.user
        )

    def test_attachment_creation(self):
        self.assertEqual(str(self.attachment.id), str(self.attachment))
        self.assertEqual(self.attachment.created_by, self.user)
        self.assertIsNotNone(self.attachment.image)

# Additional tests for models can be added as needed

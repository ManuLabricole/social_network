from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from account.models import User
from .models import Post, PostAttachment
from .serializers import PostSerializer, PostAttachmentSerializer


class PostSerializerTestCase(TestCase):
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

    def test_post_serializer(self):
        serializer = PostSerializer(instance=self.post)
        data = serializer.data
        self.assertEqual(data['title'], 'Test Post')


class PostAttachmentSerializerTestCase(TestCase):
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

    def test_attachment_serializer(self):
        serializer = PostAttachmentSerializer(instance=self.attachment)
        data = serializer.data
        self.assertEqual(data['created_by'], self.user.id)
        self.assertIsNotNone(data['image'])

from django.contrib.auth import get_user_model
from django.test import TestCase

from ..models import Group, Post

User = get_user_model()


class PostModelTest(TestCase):
    """Создаем тестовый пост"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='Some guy')
        cls.post = Post.objects.create(
            author=cls.user,
            text='Тестовый пост без группы'
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__"""
        post = PostModelTest.post
        self.assertEqual(str(post), post.text[:15])

    def test_models_have_verbose_name(self):
        """Проверяем, что verbose_name в полях совпадает с ожидаемым"""
        post = PostModelTest.post
        field_verboses = {
            'text': 'Текст',
            'group': 'Группа'
        }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).verbose_name, expected_value)

    def test_models_have_help_text(self):
        """help_text в полях совпадает с ожидаемым"""
        post = PostModelTest.post
        field_help_texts = {
            'text': 'Введите текст',
            'group': 'Введите название вашей группы'
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    post._meta.get_field(field).help_text, expected_value)


class GroupModelTest(TestCase):
    """Создаем тестовую группу"""
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.group = Group.objects.create(
            title='Любители пива',
            slug='Beer-cheer',
            description='А по названию непонятно?'
        )

    def test_models_have_correct_object_names(self):
        """Проверяем, что у моделей корректно работает __str__"""
        group = GroupModelTest.group
        self.assertEqual(str(group), group.title)

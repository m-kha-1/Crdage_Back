

# Create your tests here.
from django.test import TestCase
from django.contrib.auth.models import User
from .models import CgArtist3

class CgArtist3ModelTest(TestCase):

    def setUp(self):
        # Crée un utilisateur pour la relation ForeignKey
        self.user = User.objects.create_user(username='testuser', password='12345')
        
        # test une instance de CgArtist3
        self.artist = CgArtist3.objects.create(
            user=self.user,
            name='m b',
            role='LIGHT'
        )

    def test_artist_creation(self):
        # Test instance a été créée correctement
        self.assertEqual(self.artist.name, 'm b')
        self.assertEqual(self.artist.role, 'LIGHT')
        self.assertEqual(self.artist.user.username, 'testuser')

    def test_artist_str(self):
        # Test la méthode __str__
        self.assertEqual(str(self.artist), 'm b')

    def test_role_choices(self):
        # Test choix de rôle
        roles = dict(CgArtist3.types)
        self.assertIn(self.artist.role, roles)
        self.assertEqual(roles[self.artist.role], 'lighting')

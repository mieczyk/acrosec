from django.test import TestCase
from parameterized import parameterized

from .models import Flashcard, ModelNotInitializedError

class FlashcardTestCase(TestCase):
    @parameterized.expand([
        ('Denial-of-Service', True),
        ('Denial of Service', True),
        ('denial-of-service', True),
        ('denial of service', True),
        ('denial,of.service', True),
        ('denialofservice', False),
        ('Deenial-of-Service', False),
        ('Denial of Servic', False),
        ('denial-service', False),
        ('denial of serice', False),
    ])
    def test_is_answer_correct_compares_input_with_valid_answer(
        self, given_answer: str, expected_result: bool
    ):
        flashcard = Flashcard.objects.create(
            question='DoS', answer='Denial-of-Service'
        )

        self.assertEqual(
            flashcard.is_answer_correct(given_answer), 
            expected_result
        )

    def test_is_answer_correct_raises_exception_on_uninitialized_model(self):
        flashcard = Flashcard(question='DES')

        with self.assertRaises(ModelNotInitializedError):
            flashcard.is_answer_correct('anything')

    def test_is_answer_correct_returns_False_if_empty_answer_given(self):
        flashcard = Flashcard.objects.create(
            question='DHE', answer='Diffie-Hellman Ephemeral'
        )

        self.assertFalse(flashcard.is_answer_correct(''))
        self.assertFalse(flashcard.is_answer_correct('  '))
        self.assertFalse(flashcard.is_answer_correct(None))

    def test_is_answer_correct_ignores_conjunctions(self):
        flashcard = Flashcard.objects.create(
            question='AAA', answer='Authentication, Authorization, and Accounting'
        )
        
        self.assertTrue(
             flashcard.is_answer_correct('Authentication Authorization Accounting')
        )


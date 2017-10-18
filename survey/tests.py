import random

from otree.api import Currency as c, currency_range
from . import views, models
from ._builtin import Bot


def rand_val_from_choices(choices):
    return random.choice([k for k, _ in choices])


class PlayerBot(Bot):
    def play_round(self):
        yield (views.SurveyIntro, )

        yield (views.SurveyPage1, {
            'q1_a': random.randint(18, 100),
            'q1_b': rand_val_from_choices(models.GENDER_CHOICES),
        })

        yield (views.SurveyPage2, {
            'q2_a': rand_val_from_choices(models.YESNO_CHOICES),
            'q2_b': random.choice(('', 'foo', 'bar'))
        })

        yield (views.SurveyPage3, {
            'q3_a': rand_val_from_choices(models.YESNO_CHOICES),
        })

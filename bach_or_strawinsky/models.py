from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random


doc = """
This is a 2-player 2-strategy coordination game. The original name is battle of the sexes and story originated
from
<a href="http://books.google.ch/books?id=uqDDAgAAQBAJ&lpg=PP1&ots=S-DC4LemnS&lr&pg=PP1#v=onepage&q&f=false" target="_blank">
    Luce and Raiffa (1957)
</a>.

"""


class Constants(BaseConstants):
    name_in_url = 'bach_or_strawinsky'
    players_per_group = 2
    num_rounds = 1

    instructions_template = 'bach_or_strawinsky/Instructions.html'

    # """Amount rewarded when going together to the preferred concert"""
    bach_bachperson_payoff = strawinsky_strawinskyperson_payoff = c(300)

    # Amount rewarded when going together to the NOT preferred concert
    bach_strawinskyperson_payoff = strawinsky_bachperson_payoff = c(200)

    # amount rewarded to either if the choices don't match
    mismatch_payoff = c(0)


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    def set_payoffs(self):
        bachperson = self.get_player_by_role('bachperson')
        strawinskyperson = self.get_player_by_role('strawinskyperson')

        if bachperson.decision != strawinskyperson.decision:
            bachperson.payoff = Constants.mismatch_payoff
            strawinskyperson.payoff = Constants.mismatch_payoff

        else:
            if bachperson.decision == 'Bach':
                bachperson.payoff = Constants.bach_bachperson_payoff
                strawinskyperson.payoff = Constants.bach_strawinskyperson_payoff
            else:
                bach_bachperson_payoff.payoff = Constants.strawinsky_bachperson_payoff
                strawinskyperson.payoff = Constants.strawinsky_strawinskyperson_payoff


class Player(BasePlayer):
    decision = models.CharField(
        choices=['Bach', 'Strawinsky'],
        doc="""Either Bach or Strawinsky""",
        widget=widgets.RadioSelect()
    )

    def other_player(self):
        """Returns other player in group"""
        return self.get_others_in_group()[0]

    def role(self):
        if self.id_in_group == 1:
            return 'bachperson'
        if self.id_in_group == 2:
            return 'strawinskyperson'

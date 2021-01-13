from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants

#import random

class Introduction(Page):
    
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

class MyPage(Page):

    form_model ='player'
    form_fields = ['decision']
    
    def is_displayed(self):
        return self.round_number == 1

    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

class MyPage2(Page):

    form_model ='player'
    form_fields = ['decision']
    
    def is_displayed(self):
        return self.round_number == 2

    def vars_for_template(self):
        return dict(participant_id = self.participant.label)    

class MyPage3(Page):

    form_model ='player'
    form_fields = ['decision']
    
    def is_displayed(self):
        return self.round_number == 3

    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

class MyPage4(Page):

    form_model ='player'
    form_fields = ['decision']
    
    def is_displayed(self):
        return self.round_number == 4

    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

class MyPage5(Page):

    form_model ='player'
    form_fields = ['decision']
    
    def is_displayed(self):
        return self.round_number == 5

    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

class MyPage6(Page):

    form_model ='player'
    form_fields = ['decision']
    
    def is_displayed(self):
        return self.round_number == 6

    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

class MyPage7(Page):

    form_model ='player'
    form_fields = ['decision']
    
    def is_displayed(self):
        return self.round_number == 7

    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

class ResultsWaitPage(WaitPage):

    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

    after_all_players_arrive = 'set_payoffs'

class Results(Page):
    
    def vars_for_template(self):
        return dict(participant_id = self.participant.label)

class Pagos(Page):

    def vars_for_template(self):
        return dict(participant_id = self.participant.label)
        


page_sequence = [Introduction, MyPage, MyPage2, MyPage3, MyPage4, MyPage5, MyPage6, MyPage7, ResultsWaitPage, Results, Pagos]

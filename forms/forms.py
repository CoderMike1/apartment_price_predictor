# -*- coding: utf-8 -*-
from django import forms

class MainForm(forms.Form):
    DISTRICTS = [(0, 'Bieńczyce'),
    (1, 'Bieżanów-Prokocim'),
    (2, 'Bronowice'),
    (3, 'Czyżyny'),
    (4, 'Dębniki'),
    (5, 'Grzegórzki'),
    (6, 'Krowodrza'),
    (7, 'Mistrzejowice'),
    (8, 'Nowa Huta'),
    (9, 'Podgórze'),
    (10, 'Podgórze Duchackie'),
    (11, 'Prądnik Biały'),
    (12, 'Prądnik Czerwony'),
    (13, 'Stare Miasto'),
    (14, 'Swoszowice'),
    (15, 'Wzgórza Krzesławickie'),
    (16, 'Zwierzyniec'),
    (17, 'Łagiewniki-Borek Fałęcki')]

    district = forms.ChoiceField(choices=DISTRICTS,label="District")
    rooms = forms.ChoiceField(choices=[(i,i) for i in range(1,8)], label="Number of rooms")
    furnished= forms.ChoiceField(choices=[(1,"Yes"),(0,"No")], label="Furnished?")
    meters = forms.FloatField(label="Number of square meters",min_value=1, max_value=2000)
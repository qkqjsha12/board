from django.forms import *
from django import forms
from .models import Board

class BoardForm(forms.ModelForm):
    
    class Meta:
        model = Board
        fields = '__all__' 
        widgets = {
            'name': TextInput(attrs={
                'class': "",
                'style': '',
                'placeholder': '이름'
            }),
            'phone': NumberInput(attrs={
                'class': "",
                'style': '',
                'placeholder': '전화번호'
            }),
            'vdate': DateInput(attrs={
                'class': "",
                'style': '',
                'placeholder': '방문일자'
            }),
            'gdate': DateInput(attrs={
                'class': "",
                'style': '',
                'placeholder': '지급일자'
            }),
            'ap': NumberInput(attrs={
                'class': "",
                'style': '',
                'placeholder': '지급수량'
            }),
            'walletype': CheckboxInput(attrs={
                'class': "",
                'style': '',
                'placeholder': '지갑 타입'
            }),
            'awAd': TextInput(attrs={
                'class': "",
                'style': '',
                'placeholder': 'A 지갑 주소'
            }),
            'bwAd': TextInput(attrs={
                'class': "",
                'style': '',
                'placeholder': 'B 지갑 주소'
            }),
            'stakingW': CheckboxInput(attrs={
                'class': "",
                'style': '',
                'placeholder': '스테이킹 여부'
            }),
            'stakingSD': DateInput(attrs={
                'class': "",
                'style': '',
                'placeholder': '스테이킹 시작날짜'
            }),
            'stakingDate': DateInput(attrs={
                'class': "",
                'style': '',
                'placeholder': '스테이킹 기간'
            }),
            'stakingV': CheckboxInput(attrs={
                'class': "",
                'style': '',
                'placeholder': '스테이킹 지급여부'
            }),
            'content': TextInput(attrs={
                'class': "",
                'style': '',
                'placeholder': '비고'
            }),

        }


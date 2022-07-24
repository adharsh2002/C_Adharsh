from django import forms
from .models import Car, Order, PrivateMsg, payment, feedback

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "image",
            "car_name",
            "company_name",
            "num_of_seats",
            "cost_par_day",
            "content",
        ]

CarHOICES= [
    ('Maruti Alto 800', 'Maruti Alto 800'),
    ('Hyundai Verna', 'Hyundai Verna'),
    ('Skoda Rapid', 'Skoda Rapid'),
    ('Nissan Kicks', 'Nissan Kicks'),
    ('Renault Kiger', 'Renault Kiger'),
    ('Tata Altroz', 'Tata Altroz'),
    ('Toyota Fortuner', 'Toyota Fortuner'),
    ('Toyota Hilux C', 'Toyota Hilux C'),
    ('Mahindra XUV700', 'Mahindra XUV700'),
    ('Kia EV6', 'Kia EV6'),
    ('Maruti Swift', 'Maruti Swift'),
    ('Hyundai Santro', 'Hyundai Santro'),
    ('Hyundai i20', 'Hyundai i20'),
    ('Kia Seltos', 'Kia Seltos'),
    ('Maruti Ertiga', 'Maruti Ertiga'),

    ]    

class OrderForm(forms.ModelForm):
    car_name= forms.CharField(label='car_name', widget=forms.Select(choices=CarHOICES))
    date= forms.DateTimeField(widget= forms.TextInput
                           (attrs={'placeholder':'mm/dd/yyyy'}))
    to= forms.DateTimeField(widget= forms.TextInput
                           (attrs={'placeholder':'mm/dd/yyyy'}))
    class Meta:
        model = Order
        fields = [
            "car_name",
            "full_name",
            "cell_no",
            "address",
            "date",
            "to",
        ]
class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMsg
        fields = [
            "name",
            "email",
            "message",
        ]

class PaymentForm(forms.ModelForm):
    month_year= forms.CharField(label='Month and year',widget= forms.TextInput
                           (attrs={'placeholder':'mm/yy'}))
    card_num= forms.CharField(label='Card number',widget= forms.TextInput
                           (attrs={'placeholder':'0000 0000 0000 0000'}))
    CVV_code= forms.CharField(widget= forms.PasswordInput
                           (attrs={'autocomplete':'off'}))
    class Meta:
        model = payment
        fields = [
            # "total_amt",
            # "bill_date",
            "card_num",
            "month_year",
            "CVV_code"
            
        ]
       
CHOICES= [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ]       

class FeedbackForm(forms.ModelForm):
    rating= forms.CharField(label='Rating', widget=forms.Select(choices=CHOICES))

    class Meta:
        model = feedback
        fields = [
            # "username"
            # "date",
            "mssg",
            "rating"
            
        ]
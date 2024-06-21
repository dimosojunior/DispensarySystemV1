from hospital.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate



class FilterDoziSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(
        required=False, 
        widget=forms.DateTimeInput(attrs={'class': 'datepicker'}))

    end_date = forms.DateTimeField(
        required=False, 
        widget=forms.DateTimeInput(attrs={'class': 'datepicker'}))

    export_to_CSV = forms.BooleanField(required=False)

    TakenBy = forms.CharField(
        required=False, 
        widget=forms.TextInput(attrs={'id': 'doctorName'}))

    class Meta:
        model = Dozi
        fields = ['TakenBy', 'start_date', 'end_date']
# class FilterDoziSearchForm(forms.ModelForm):
#     start_date = forms.DateTimeField(
#         required=False, 
#         widget=forms.TextInput(attrs={'class': 'datepicker'}))

#     end_date = forms.DateTimeField(
#         required=False, 
#         widget=forms.TextInput(attrs={'class': 'datepicker'}))

#     export_to_CSV = forms.BooleanField(required=False)

#     TakenBy = forms.CharField(
#         required=False, 
#         widget=forms.TextInput(attrs={'id': 'doctorName'}))

    
         
#     class Meta:
#         model = Dozi
#         fields =['TakenBy','start_date','end_date']
#         #fields =['user']





class ClinicServicesSearchForm(forms.ModelForm):
    
    ServiceName = forms.CharField(
        label = False,
        widget = forms.TextInput(attrs={'placeholder':'Service Name', 'id':'ServiceName'})
    )
     


    class Meta:
        model = ClinicServices
        fields = ["ServiceName"]







choose_huduma = (
    ('dawa', 'dawa'),
    ('vipimo', 'vipimo')

    )
choose_huduma_vipimo_watoto = (
    ('vipimo', 'vipimo'),
    ('dawa', 'dawa')

    )
accepti = (
    ('yes', 'yes'),
    ('no', 'no')

    )
tribe_choices = (
        
        ('', 'CHOICE TRIBE'),
        ('LUGURU', 'LUGURU'),
        ('SUKUMA', 'SUKUMA'),
        ('HAYA', 'HAYA'),
        ('NYAMWEZI', 'NYAMWEZI'),
        ('NYAKYUSA', 'NYAKYUSA'),
        ('FIPA', 'FIPA'),
        ('SHIRAZI', 'SHIRAZI'),
        ('MANYEMA', 'MANYEMA'),
        ('WAHA', 'WAHA'),
        ('HEHE', 'HEHE'),
        ('POGOLO', 'POGOLO'),
        ('IRAKI', 'IRAKI'),
        ('KULIA', 'KULIA'),
        ('GOGO', 'GOGO'),
        ('SAFWA', 'SAFWA'),
        ('MWELA', 'MWELA'),
        ('HINDI', 'HINDI'),
        ('NGONI', 'NGONI'),
        ('ZARAMO', 'ZARAMO'),
        ('MAKONDE', 'MAKONDE'),
        ('JITA', 'JITA'),
        ('SUKUMA', 'SUKUMA')
    )


class PatientRegistrationForm(ModelForm):

    fname = forms.CharField(
            label='First Name',
            required=True,
            widget=forms.TextInput(attrs={'placeholder' :'First Name'})

        )
    tname = forms.CharField(
            label='Last Name',
            required=True,
            widget=forms.TextInput(attrs={'placeholder' :'Last Name'})

        )
    year = forms.CharField(
            label='Age',
            required=False,
            widget=forms.TextInput(attrs={'placeholder' :' Age'})
       ) 

    Address = forms.CharField(
            label='Address',
            required=True,
            widget=forms.TextInput(attrs={'placeholder' :'Address'})

        )
    
    class Meta:
        model = RegisteredPatients
        fields = [

            "fname",
            "Category",
            "tname",
            "gender",
            "year",
            "Address"
            
            ]


class ClinicServicesForm(forms.ModelForm):
    
    

    class Meta:
        model = ClinicServices
        fields = '__all__'

class ClinicServicesForm(forms.ModelForm):
    
    

    class Meta:
        model = ClinicServices
        fields = '__all__'

class MyUserForm(UserCreationForm):
    
    

    class Meta:
        model = MyUser
        fields = [
        "email",
        "username",
        "password1",
        "password2",
         "first_name", 
         "middle_name",
         "last_name",
         "company_name",
         "phone",
         "is_admin",
         "is_active",
         "is_staff",
         "is_superuser",
         "is_doctor",
         "is_accountancy"



         ]
        
class UserLoginForm(forms.ModelForm):
    password=forms.CharField(
        
        widget = forms.PasswordInput(attrs={'placeholder':'password', 'class':'input'})

    ) 
    username=forms.CharField(
        
        widget = forms.TextInput(attrs={'placeholder':'Username', 'class':'input'})

    )  

    class Meta:
        model=MyUser
        fields=('username', 'password')

    def clean(self):
        if self.is_valid():
            username=self.cleaned_data['username']
            password=self.cleaned_data['password']

            if not authenticate(username=username, password=password):
                raise forms.ValidationError("username or password incorrect")





class DoziForm(forms.ModelForm):

    name = forms.CharField(
            label='Patient Name',
            widget=forms.TextInput(attrs={'id' :'tag'})
      
       )
    huduma = forms.ChoiceField(
        label='Aina Ya Huduma',
        required=False,
        choices = choose_huduma
  
       )
    paid = forms.BooleanField(
            required=False,
            label="Accept Payment"
        )

    line_one = forms.CharField(
            label="Medicine 1",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_one','class' :'input'})
      
       )
    line_one_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_one_description','class' :'input'})
      
       )
    line_one_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_one_quantity','class' :'input'})
      
       )
    line_one_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_one_unit_price','class' :'input'})
      
       )
    line_one_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_one_total_price','class' :'input'})
      
       )
    

    line_two = forms.CharField(
            label="Medicine 2",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_two','class' :'input'})
      
       )
    line_two_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_two_description','class' :'input'})
      
       )
    line_two_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_two_quantity','class' :'input'})
      
       )
    line_two_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_two_unit_price','class' :'input'})
      
       )
    line_two_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_two_total_price','class' :'input'})
      
       )


    line_three = forms.CharField(
            label="Medicine 3",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_three','class' :'input'})
      
       )
    line_three_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_three_description','class' :'input'})
      
       )
    line_three_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_three_quantity','class' :'input'})
      
       )
    line_three_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_three_unit_price','class' :'input'})
      
       )
    line_three_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_three_total_price','class' :'input'})
      
       )


    line_four = forms.CharField(
            label="Medicine 4",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_four','class' :'input'})
      
       )
    line_four_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_four_description','class' :'input'})
      
       )
    line_four_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_four_quantity','class' :'input'})
      
       )
    line_four_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_four_unit_price','class' :'input'})
      
       )
    line_four_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_four_total_price','class' :'input'})
      
       )

    line_five = forms.CharField(
            label="Medicine 5",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_five','class' :'input'})
      
       )
    line_five_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_five_description','class' :'input'})
      
       )
    line_five_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_five_quantity','class' :'input'})
      
       )
    line_five_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_five_unit_price','class' :'input'})
      
       )
    line_five_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_five_total_price','class' :'input'})
      
       )

    line_six = forms.CharField(
            label="Medicine 6",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_six','class' :'input'})
      
       )
    line_six_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_six_description','class' :'input'})
      
       )
    line_six_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_six_quantity','class' :'input'})
      
       )
    line_six_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_six_unit_price','class' :'input'})
      
       )
    line_six_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_six_total_price','class' :'input'})
      
       )


    line_seven = forms.CharField(
            label="Medicine 7",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_seven','class' :'input'})
      
       )
    line_seven_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_seven_description','class' :'input'})
      
       )
    line_seven_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_seven_quantity','class' :'input'})
      
       )
    line_seven_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_seven_unit_price','class' :'input'})
      
       )
    line_seven_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_seven_total_price','class' :'input'})
      
       )

    line_eight = forms.CharField(
            label="Medicine 8",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_eight','class' :'input'})
      
       )
    line_eight_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_eight_description','class' :'input'})
      
       )
    line_eight_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_eight_quantity','class' :'input'})
      
       )
    line_eight_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_eight_unit_price','class' :'input'})
      
       )
    line_eight_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_eight_total_price','class' :'input'})
      
       )

    line_nine = forms.CharField(
            label="Medicine 9",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_nine','class' :'input'})
      
       )
    line_nine_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_nine_description','class' :'input'})
      
       )
    line_nine_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_nine_quantity','class' :'input'})
      
       )
    line_nine_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_nine_unit_price','class' :'input'})
      
       )
    line_nine_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_nine_total_price','class' :'input'})
      
       )


    line_ten = forms.CharField(
            label="Medicine 10",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_ten','class' :'input'})
      
       )
    line_ten_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_ten_description','class' :'input'})
      
       )
    line_ten_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_ten_quantity','class' :'input'})
      
       )
    line_ten_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_ten_unit_price','class' :'input'})
      
       )
    line_ten_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_ten_total_price','class' :'input'})
      
       )

    
    total = forms.IntegerField(
            required=False,
            label='Total Amount',
            widget=forms.NumberInput(attrs={'id' : 'div_id_total','class' :'input'})
      
       )


    
    class Meta:
        model = Dozi
        fields = [
            
            'name',
            'accepted',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type',
            'comments',
            'doctor_comments'

        ]

        
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name


class DoziSearchForm(forms.ModelForm):
    generate_invoice = forms.BooleanField(required=False)
    name = forms.CharField(
            label='Patient Name',
            widget=forms.TextInput(attrs={'id' :'tage'})
      
       )
    class Meta:
        model = Dozi
        fields = ['name', 'generate_invoice']

class SearchForm(forms.ModelForm):
    #generate_invoice = forms.BooleanField(required=False)
    line_one_quantity = forms.IntegerField(
            label=False,
            widget=forms.NumberInput(attrs={'name' :'date'})
      
       )
    class Meta:
        model = Dozi
        fields = ['line_one_quantity']







class DoziUpdateForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'tag'})
      
       )
    huduma = forms.ChoiceField(
        label='Aina Ya Huduma',
        required=False,
        choices = choose_huduma
  
       )
    paid = forms.BooleanField(
            required=False,
            label="Accept Payment"
        )

    line_one = forms.CharField(
            label="Medicine 1",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_one','class' :'input'})
      
       )
    line_one_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_one_description','class' :'input'})
      
       )
    line_one_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_one_quantity','class' :'input'})
      
       )
    line_one_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_one_unit_price','class' :'input'})
      
       )
    line_one_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_one_total_price','class' :'input'})
      
       )
    

    line_two = forms.CharField(
            label="Medicine 2",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_two','class' :'input'})
      
       )
    line_two_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_two_description','class' :'input'})
      
       )
    line_two_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_two_quantity','class' :'input'})
      
       )
    line_two_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_two_unit_price','class' :'input'})
      
       )
    line_two_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_two_total_price','class' :'input'})
      
       )


    line_three = forms.CharField(
            label="Medicine 3",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_three','class' :'input'})
      
       )
    line_three_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_three_description','class' :'input'})
      
       )
    line_three_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_three_quantity','class' :'input'})
      
       )
    line_three_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_three_unit_price','class' :'input'})
      
       )
    line_three_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_three_total_price','class' :'input'})
      
       )


    line_four = forms.CharField(
            label="Medicine 4",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_four','class' :'input'})
      
       )
    line_four_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_four_description','class' :'input'})
      
       )
    line_four_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_four_quantity','class' :'input'})
      
       )
    line_four_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_four_unit_price','class' :'input'})
      
       )
    line_four_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_four_total_price','class' :'input'})
      
       )

    line_five = forms.CharField(
            label="Medicine 5",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_five','class' :'input'})
      
       )
    line_five_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_five_description','class' :'input'})
      
       )
    line_five_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_five_quantity','class' :'input'})
      
       )
    line_five_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_five_unit_price','class' :'input'})
      
       )
    line_five_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_five_total_price','class' :'input'})
      
       )

    line_six = forms.CharField(
            label="Medicine 6",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_six','class' :'input'})
      
       )
    line_six_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_six_description','class' :'input'})
      
       )
    line_six_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_six_quantity','class' :'input'})
      
       )
    line_six_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_six_unit_price','class' :'input'})
      
       )
    line_six_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_six_total_price','class' :'input'})
      
       )


    line_seven = forms.CharField(
            label="Medicine 7",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_seven','class' :'input'})
      
       )
    line_seven_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_seven_description','class' :'input'})
      
       )
    line_seven_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_seven_quantity','class' :'input'})
      
       )
    line_seven_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_seven_unit_price','class' :'input'})
      
       )
    line_seven_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_seven_total_price','class' :'input'})
      
       )

    line_eight = forms.CharField(
            label="Medicine 8",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_eight','class' :'input'})
      
       )
    line_eight_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_eight_description','class' :'input'})
      
       )
    line_eight_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_eight_quantity','class' :'input'})
      
       )
    line_eight_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_eight_unit_price','class' :'input'})
      
       )
    line_eight_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_eight_total_price','class' :'input'})
      
       )

    line_nine = forms.CharField(
            label="Medicine 9",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_nine','class' :'input'})
      
       )
    line_nine_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_nine_description','class' :'input'})
      
       )
    line_nine_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_nine_quantity','class' :'input'})
      
       )
    line_nine_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_nine_unit_price','class' :'input'})
      
       )
    line_nine_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_nine_total_price','class' :'input'})
      
       )


    line_ten = forms.CharField(
            label="Medicine 10",
            required=False,
            widget=forms.TextInput(attrs={'id' : 'div_id_line_ten','class' :'input'})
      
       )
    line_ten_description = forms.CharField(
            label="Description",
            required=False,
            widget=forms.Textarea(attrs={'id' : 'div_id_line_ten_description','class' :'input'})
      
       )
    line_ten_quantity = forms.IntegerField(
            label="Quantity",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_ten_quantity','class' :'input'})
      
       )
    line_ten_unit_price = forms.IntegerField(
            label="Unit Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_ten_unit_price','class' :'input'})
      
       )
    line_ten_total_price = forms.IntegerField(
            label="Total Price",
            required=False,
            widget=forms.NumberInput(attrs={'id' : 'div_id_line_ten_total_price','class' :'input'})
      
       )

    
    total = forms.IntegerField(
            label='Total Amount',
            widget=forms.NumberInput(attrs={'id' : 'div_id_total','class' :'input'})
      
       )
    class Meta:
        model = Dozi
        fields = [
            'name',
            'huduma',
            'accepted',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type',
            'comments',
            'doctor_comments'

        ]



class VipimoForm(forms.ModelForm):

    name = forms.CharField(
        label='Patient Name',
        widget=forms.TextInput(attrs={'id' :'tag'})
  
       )
    huduma = forms.ChoiceField(
        label='TYPE OF INFORMATIONS',
        choices = choose_huduma_vipimo_watoto
  
       )
    class Meta:
        model = Vipimo
        fields = [
            'name',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]

        
    def clean_invoice_number(self):
        invoice_number = self.cleaned_data.get('invoice_number')
        if not invoice_number:
            raise forms.ValidationError('This field is required')
        return invoice_number

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError('This field is required')
        return name
        

class VipimoUpdateForm(forms.ModelForm):

    name = forms.CharField(
            label=False,
            widget=forms.TextInput(attrs={'id' :'tag'})
      
       )
    huduma = forms.ChoiceField(
        label='TYPE OF INFORMATIONS',
        required=False,
        choices = choose_huduma_vipimo_watoto
  
       )
    line_one = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_one_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_one_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_two_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_two_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_three_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_three_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_four_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_four_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_five_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_five_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_six_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_six_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_seven_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_seven_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_eight_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_eight_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_nine_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_nine_total_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_description = forms.CharField(
            label=False,
            required=False,
            widget=forms.TextInput(attrs={'class' :'input'})
      
       )
    line_ten_quantity = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_unit_price = forms.IntegerField(
            label=False,
            required=False,
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    line_ten_total_price = forms.IntegerField(
            label=False,
            required=False,

            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    total = forms.IntegerField(
            label='Total Amount',
            widget=forms.NumberInput(attrs={'class' :'input'})
      
       )
    class Meta:
        model = Vipimo
        fields = [
            'name',
            'huduma',
            'accepted_quantity',
            'accepted_date',
            'phone_number',
            'invoice_date',
            'line_one',
            'line_one_description',
            'line_one_quantity',
            'line_one_unit_price',
            'line_one_total_price',
            'accepted_line_one',


            'line_two',
            'line_two_description',
            'line_two_quantity',
            'line_two_unit_price',
            'line_two_total_price',
            'accepted_line_two',
            
            'line_three',
            'line_three_description',
            'line_three_quantity',
            'line_three_unit_price',
            'line_three_total_price',
            'accepted_line_three',

            'line_four',
            'line_four_description',
            'line_four_quantity',
            'line_four_unit_price',
            'line_four_total_price',
            'accepted_line_four',

            'line_five',
            'line_five_description',
            'line_five_quantity',
            'line_five_unit_price',
            'line_five_total_price',
            'accepted_line_five',

            'line_six',
            'line_six_description',
            'line_six_quantity',
            'line_six_unit_price',
            'line_six_total_price',
            'accepted_line_six',

            'line_seven',
            'line_seven_description',
            'line_seven_quantity',
            'line_seven_unit_price',
            'line_seven_total_price',
            'accepted_line_seven',

            'line_eight',
            'line_eight_description',
            'line_eight_quantity',
            'line_eight_unit_price',
            'line_eight_total_price',
            'accepted_line_eight',

            'line_nine',
            'line_nine_description',
            'line_nine_quantity',
            'line_nine_unit_price',
            'line_nine_total_price',
            'accepted_line_nine',

            'line_ten',
            'line_ten_description',
            'line_ten_quantity',
            'line_ten_unit_price',
            'line_ten_total_price',
            'accepted_line_ten',

            'total',
            'paid',
            'invoice_type'

        ]






class AvailableMedicinesForm(forms.ModelForm):

    medicine_name = forms.CharField(
        label='Medicine Name ',
        widget=forms.TextInput(attrs={'id' :'medicine_name'})
  
       )
    
    class Meta:
        model = AvailableMedicines
        fields = '__all__'
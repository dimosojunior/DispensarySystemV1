from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# Create your models here.
def generated_reg_no():
    last_reg_no = RegisteredPatients.objects.all().order_by('id').last()
    if not last_reg_no:
        return '1'
    reg_no = last_reg_no.reg_no
    new_reg_no = int(reg_no) + 1
    return new_reg_no


class MyUserManager(BaseUserManager):
    def create_user(self, email,username, first_name, middle_name, last_name, company_name, phone, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("username is required")
        if not first_name:
            raise ValueError("Your first name is required")
        if not middle_name:
            raise ValueError("Your middle name is required")
        if not last_name:
            raise ValueError("Your last name is required")
        if not company_name:
            raise ValueError("Company name  is required")
        if not phone:
            raise ValueError("phone is required")

        user=self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            company_name=company_name,
            phone=phone,
            username=username,
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email,username, first_name, middle_name, last_name, company_name, phone, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            company_name=company_name,
            phone=phone,
            password=password,

        )
        user.is_admin=True
        user.is_staff=True
        user.is_doctor=True
        user.is_accountancy=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

    

        


class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    username=models.CharField(verbose_name="username", max_length=500, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name", max_length=100, unique=False)
    phone=models.CharField(verbose_name="phone", max_length=15)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_doctor=models.BooleanField(default=False)
    is_accountancy=models.BooleanField(default=False)


    USERNAME_FIELD="username"
    REQUIRED_FIELDS=['email','first_name','middle_name','last_name','company_name','phone']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True



class ClinicServicesCategories(models.Model):
    #ServiceCategory = models.ForeignKey('ClinicServices', on_delete=models.CASCADE,null=True, blank=True)

    CategoryName = models.CharField(verbose_name="Category Name", max_length=500)
   

    
    def __str__(self):
        return self.CategoryName 


class ClinicServices(models.Model):
    Category = models.ForeignKey(ClinicServicesCategories, on_delete=models.CASCADE,null=True, blank=True)
    ServiceName = models.CharField(verbose_name="Service Name", max_length=500)
   
    ServicePrice = models.CharField(verbose_name="Service Price", max_length=200,blank=True,null=True)
    Quantity = models.IntegerField(verbose_name="Total Quantity",default=0, blank=True, null=True)

    
    
    
    def __str__(self):
        return self.ServiceName


class PatientCategories(models.Model):
    CategoryName = models.CharField(max_length=500)
   
    
    def __str__(self):
        return self.CategoryName




class Tribe(models.Model):
    
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
    tribe = models.CharField(max_length=100, choices=tribe_choices)
    

       
    def __str__(self):
        return self.tribe 








class Doctors(models.Model):
    title = models.CharField(max_length=200)
   
    status = models.CharField(max_length=200)
    
    description = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='productImages')
   
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title


class MorningWorkersShift(models.Model):
    title = models.CharField(max_length=200)
   
    place = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    def __str__(self):
        return self.title

class AfternoonWorkersShift(models.Model):
    title = models.CharField(max_length=200)
   
    place = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    def __str__(self):
        return self.title




class RegisteredPatients(models.Model):
    Category = models.ForeignKey(PatientCategories, on_delete=models.CASCADE,null=True, blank=True)
    fname = models.CharField(max_length=100, blank=False, null=False)
    sname = models.CharField(max_length=100, blank=True, null=True)
    tname = models.CharField(max_length=100, blank=False, null=False)
    gender_choices = (
        ('', 'Choose Gender'),
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    gender = models.CharField(max_length=100, choices=gender_choices,blank=True, null=True)
    reg_no= models.CharField(max_length=200, default=generated_reg_no, unique=True, editable=False)

    year = models.CharField(max_length=100,blank=False, null=False)
    tribe = models.CharField(max_length=100,blank=True, null=True)
    residence = models.CharField(max_length=100,blank=True, null=True)
    next_kin = models.CharField(max_length=100,blank=True, null=True)
    next_kin_residence = models.CharField(max_length=100,blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    Address = models.CharField(max_length=100, blank=False, null=False)

    payment_choices = (
        
        ('Under Five', 'Under Five'),
        ('Above 60', 'above 60'),
        ('Under Five', 'under five'),
        ('SelfRefferal', 'SelfRefferal'),
        ('Pregnancy Mother', 'pregnancy mother'),
        ('Nhif', 'Nhif'),
        ('Chf', 'Chf')
    )
    payment_type = models.CharField(max_length=100, default="Under Five",blank=True, null=True,  choices=payment_choices)
    patient_choices = (
    	('Children', 'Children'),
      
        ('Mzee', 'Mzee'),
        
        ('Mjamzito', 'Mjamzito'),
        ('Wa kawaida', 'Wa kawaida')
        
    )
    patient_type = models.CharField(max_length=100,blank=True, null=True, default="Children", choices=patient_choices)
    service_choices = (
        ('', 'choice----'),
        ('For the First Time', 'For the First Time'),
        ('Returning', 'Returning')
      
        
    )
    service_time = models.CharField(max_length=100,blank=True, null=True, choices=service_choices)
    opd_choices = (
        
        ('', 'choice----'),
        ('OPD', 'OPD')
      
        
    )
    opd = models.CharField(max_length=100, default="OPD",blank=True, null=True, choices=opd_choices)
    created=models.DateTimeField(auto_now_add=True)
    accepted=models.BooleanField(default=False, null=True, blank=True)
    accepted_date=models.DateTimeField(auto_now_add=False, blank=True,null=True)


   
    def __str__(self):
        return self.fname + ""  "" + "" + self.tname


class Medicine(models.Model):
    RegisteredPatients = models.ForeignKey(RegisteredPatients, on_delete=models.CASCADE,null=True)

    name =models.CharField(max_length=100, blank=False)
    quantity =models.IntegerField(null=True, blank=True)
    price =models.IntegerField(null=True, blank=True)
    
    description =models.TextField(max_length=200,null=True, blank=True)
    
    
    complete =models.BooleanField(default=False)
    
    created =models.DateTimeField(auto_now_add=True)

    accepted=models.BooleanField(default=False, null=True, blank=True)
    accepted_date=models.DateTimeField(auto_now_add=False, blank=True,null=True)

    def _str_ (self):
        return self.name


class Dozi(models.Model):
    Service = models.ForeignKey(ClinicServices, on_delete=models.CASCADE,null=True, blank=True)
    TakenBy = models.CharField(max_length=200, default='', blank=True, null=True)

    #toto_amount= models.IntegerField( default=toto, unique=False, editable=False)
    accepted=models.BooleanField(default=False, null=True, blank=True)
    accepted_date=models.DateTimeField(auto_now_add=False, blank=True,null=True)
    since_join=models.DateTimeField(auto_now_add=True, blank=True,null=True)
    accepted_quantity=models.BooleanField(default=False, null=True, blank=True)
  
    comments =models.TextField(max_length=10000, default='', blank=True, null=True)
    doctor_comments =models.TextField(max_length=10000, default='', blank=True, null=True)
    invoice_number =models.IntegerField(blank=True, null=True)
    invoice_date =models.DateField(auto_now_add=False, blank=True, null=True)
    name =models.CharField('Customer Name', max_length=200, default='', blank=True, null=True)
    line_one =models.CharField('Line 1', max_length=200, default='', blank=True, null=True)
    line_one_description=models.TextField('Description', max_length=200,blank=True, null=True)
    line_one_quantity =models.IntegerField('Quantity', default=1, blank=True, null=True)
    line_one_unit_price =models.IntegerField('Unit Price',default=0, blank=True, null=True)
    line_one_total_price =models.IntegerField('Line Total Price', default=0, blank=True, null=True)
    accepted_line_one=models.BooleanField(default=False, null=True, blank=True)

    line_two =models.CharField('Line 2', max_length=200, default='', blank=True, null=True)
    line_two_description=models.TextField('Description', max_length=200,blank=True, null=True)
    line_two_quantity =models.IntegerField('Quantity', default=1, blank=True, null=True)
    line_two_unit_price =models.IntegerField('Unit Price',default=0, blank=True, null=True)
    line_two_total_price =models.IntegerField('Line Total Price', default=0, blank=True, null=True)
    accepted_line_two=models.BooleanField(default=False, null=True, blank=True)

    line_three =models.CharField('Line 3', max_length=200, default='', blank=True, null=True)
    line_three_description=models.TextField('Description', max_length=200,blank=True, null=True)
    line_three_quantity =models.IntegerField('Quantity', default=1, blank=True, null=True)
    line_three_unit_price =models.IntegerField('Unit Price',default=0, blank=True, null=True)
    line_three_total_price =models.IntegerField('Line Total Price', default=0, blank=True, null=True)
    accepted_line_three=models.BooleanField(default=False, null=True, blank=True)

    line_four =models.CharField('Line 4', max_length=200, default='', blank=True, null=True)
    line_four_description=models.TextField('Description', max_length=200,blank=True, null=True)
    line_four_quantity =models.IntegerField('Quantity', default=1, blank=True, null=True)
    line_four_unit_price =models.IntegerField('Unit Price',default=0, blank=True, null=True)
    line_four_total_price =models.IntegerField('Line Total Price', default=0, blank=True, null=True)
    accepted_line_four=models.BooleanField(default=False, null=True, blank=True)


    line_five =models.CharField('Line 5', max_length=200, default='', blank=True, null=True)
    line_five_description=models.TextField('Description', max_length=200,blank=True, null=True)
    line_five_quantity =models.IntegerField('Quantity', default=1, blank=True, null=True)
    line_five_unit_price =models.IntegerField('Unit Price',default=0, blank=True, null=True)
    line_five_total_price =models.IntegerField('Line Total Price', default=0, blank=True, null=True)
    accepted_line_five=models.BooleanField(default=False, null=True, blank=True)

    line_six =models.CharField('Line 6', max_length=200, default='', blank=True, null=True)
    line_six_description=models.TextField('Description', max_length=200,blank=True, null=True)
    line_six_quantity =models.IntegerField('Quantity', default=1, blank=True, null=True)
    line_six_unit_price =models.IntegerField('Unit Price',default=0, blank=True, null=True)
    line_six_total_price =models.IntegerField('Line Total Price', default=0, blank=True, null=True)
    accepted_line_six=models.BooleanField(default=False, null=True, blank=True)

    line_seven =models.CharField('Line 7', max_length=200, default='', blank=True, null=True)
    line_seven_description=models.TextField('Description', max_length=200,blank=True, null=True)
    line_seven_quantity =models.IntegerField('Quantity', default=1, blank=True, null=True)
    line_seven_unit_price =models.IntegerField('Unit Price',default=0, blank=True, null=True)
    line_seven_total_price =models.IntegerField('Line Total Price', default=0, blank=True, null=True)
    accepted_line_seven=models.BooleanField(default=False, null=True, blank=True)

    line_eight =models.CharField('Line 8', max_length=200, default='', blank=True, null=True)
    line_eight_description=models.TextField('Description', max_length=200,blank=True, null=True)
    line_eight_quantity =models.IntegerField('Quantity', default=1, blank=True, null=True)
    line_eight_unit_price =models.IntegerField('Unit Price',default=0, blank=True, null=True)
    line_eight_total_price =models.IntegerField('Line Total Price', default=0, blank=True, null=True)
    accepted_line_eight=models.BooleanField(default=False, null=True, blank=True)

    line_nine =models.CharField('Line 9', max_length=200, default='', blank=True, null=True)
    line_nine_description=models.TextField('Description', max_length=200,blank=True, null=True)
    line_nine_quantity =models.IntegerField('Quantity', default=1, blank=True, null=True)
    line_nine_unit_price =models.IntegerField('Unit Price',default=0, blank=True, null=True)
    line_nine_total_price =models.IntegerField('Line Total Price', default=0, blank=True, null=True)
    accepted_line_nine=models.BooleanField(default=False, null=True, blank=True)

    line_ten =models.CharField('Line 10', max_length=200, default='', blank=True, null=True)
    line_ten_description=models.TextField('Description', max_length=200,blank=True, null=True)
    line_ten_quantity =models.IntegerField('Quantity', default=1, blank=True, null=True)
    line_ten_unit_price =models.IntegerField('Unit Price',default=0, blank=True, null=True)
    line_ten_total_price =models.IntegerField('Line Total Price', default=0, blank=True, null=True)
    accepted_line_ten=models.BooleanField(default=False, null=True, blank=True)


    phone_number = models.CharField(max_length=120, default='', blank=True, null=True)

    total = models.IntegerField( default='0', blank=True, null=True)
    balance = models.IntegerField(default='0', blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    reg_date= models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    paid = models.BooleanField(default=False)
    invoice_type_choice = (
        ('Receipt', 'Receipt'),
        
        ('invoice', 'invoice'),
    )
    invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)
    chagua_huduma = (
        ('vipimo', 'vipimo'),
        
        ('dawa', 'dawa'),
    )
    huduma = models.CharField(max_length=50, default='', blank=True, null=True, choices=chagua_huduma)

    #def __unicode__(self):
        #return self.invoice_number
    class Meta:
        db_table='DOZI'


    def __str__(self):
        return  self.name 





class Vipimo(models.Model):
    #toto_amount= models.IntegerField( default=toto, unique=False, editable=False)
    accepted=models.BooleanField(default=False, null=True, blank=True)
    accepted_date=models.DateTimeField(auto_now_add=False, blank=True,null=True)
    accepted_quantity=models.BooleanField(default=False, null=True, blank=True)
  
    comments =models.TextField(max_length=200, default='', blank=True, null=True)
    invoice_number =models.IntegerField(blank=True, null=True)
    invoice_date =models.DateField(auto_now_add=False, blank=True, null=True)
    name =models.CharField('Customer Name', max_length=200, default='', blank=True, null=True)
    line_one =models.CharField('Line 1', max_length=200, default='', blank=True, null=True)
    line_one_description=models.CharField('Description 1', max_length=200,blank=True, null=True)
    line_one_quantity =models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_one_unit_price =models.IntegerField('Unit Price (D)',default=0, blank=True, null=True)
    line_one_total_price =models.IntegerField('Line Total Price (D)', default=0, blank=True, null=True)
    accepted_line_one=models.BooleanField(default=False, null=True, blank=True)

    line_two =models.CharField('Line 2', max_length=200, default='', blank=True, null=True)
    line_two_description=models.CharField('Description 2', max_length=200,blank=True, null=True)
    line_two_quantity =models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_two_unit_price =models.IntegerField('Unit Price (D)',default=0, blank=True, null=True)
    line_two_total_price =models.IntegerField('Line Total Price (D)', default=0, blank=True, null=True)
    accepted_line_two=models.BooleanField(default=False, null=True, blank=True)

    line_three =models.CharField('Line 3', max_length=200, default='', blank=True, null=True)
    line_three_description=models.CharField('Description 3', max_length=200,blank=True, null=True)
    line_three_quantity =models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_three_unit_price =models.IntegerField('Unit Price (D)',default=0, blank=True, null=True)
    line_three_total_price =models.IntegerField('Line Total Price (D)', default=0, blank=True, null=True)
    accepted_line_three=models.BooleanField(default=False, null=True, blank=True)

    line_four =models.CharField('Line 4', max_length=200, default='', blank=True, null=True)
    line_four_description=models.CharField('Description 4', max_length=200,blank=True, null=True)
    line_four_quantity =models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_four_unit_price =models.IntegerField('Unit Price (D)',default=0, blank=True, null=True)
    line_four_total_price =models.IntegerField('Line Total Price (D)', default=0, blank=True, null=True)
    accepted_line_four=models.BooleanField(default=False, null=True, blank=True)


    line_five =models.CharField('Line 5', max_length=200, default='', blank=True, null=True)
    line_five_description=models.CharField('Description 5', max_length=200,blank=True, null=True)
    line_five_quantity =models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_five_unit_price =models.IntegerField('Unit Price (D)',default=0, blank=True, null=True)
    line_five_total_price =models.IntegerField('Line Total Price (D)', default=0, blank=True, null=True)
    accepted_line_five=models.BooleanField(default=False, null=True, blank=True)

    line_six =models.CharField('Line 6', max_length=200, default='', blank=True, null=True)
    line_six_description=models.CharField('Description 6', max_length=200,blank=True, null=True)
    line_six_quantity =models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_six_unit_price =models.IntegerField('Unit Price (D)',default=0, blank=True, null=True)
    line_six_total_price =models.IntegerField('Line Total Price (D)', default=0, blank=True, null=True)
    accepted_line_six=models.BooleanField(default=False, null=True, blank=True)

    line_seven =models.CharField('Line 7', max_length=200, default='', blank=True, null=True)
    line_seven_description=models.CharField('Description 7', max_length=200,blank=True, null=True)
    line_seven_quantity =models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_seven_unit_price =models.IntegerField('Unit Price (D)',default=0, blank=True, null=True)
    line_seven_total_price =models.IntegerField('Line Total Price (D)', default=0, blank=True, null=True)
    accepted_line_seven=models.BooleanField(default=False, null=True, blank=True)

    line_eight =models.CharField('Line 8', max_length=200, default='', blank=True, null=True)
    line_eight_description=models.CharField('Description 8', max_length=200,blank=True, null=True)
    line_eight_quantity =models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_eight_unit_price =models.IntegerField('Unit Price (D)',default=0, blank=True, null=True)
    line_eight_total_price =models.IntegerField('Line Total Price (D)', default=0, blank=True, null=True)
    accepted_line_eight=models.BooleanField(default=False, null=True, blank=True)

    line_nine =models.CharField('Line 9', max_length=200, default='', blank=True, null=True)
    line_nine_description=models.CharField('Description 9', max_length=200,blank=True, null=True)
    line_nine_quantity =models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_nine_unit_price =models.IntegerField('Unit Price (D)',default=0, blank=True, null=True)
    line_nine_total_price =models.IntegerField('Line Total Price (D)', default=0, blank=True, null=True)
    accepted_line_nine=models.BooleanField(default=False, null=True, blank=True)

    line_ten =models.CharField('Line 10', max_length=200, default='', blank=True, null=True)
    line_ten_description=models.CharField('Description 10', max_length=200,blank=True, null=True)
    line_ten_quantity =models.IntegerField('Quantity', default=0, blank=True, null=True)
    line_ten_unit_price =models.IntegerField('Unit Price (D)',default=0, blank=True, null=True)
    line_ten_total_price =models.IntegerField('Line Total Price (D)', default=0, blank=True, null=True)
    accepted_line_ten=models.BooleanField(default=False, null=True, blank=True)


    phone_number = models.CharField(max_length=120, default='', blank=True, null=True)

    total = models.IntegerField( default='0', blank=True, null=True)
    balance = models.IntegerField(default='0', blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    reg_date= models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True, blank=True)
    paid = models.BooleanField(default=False)
    invoice_type_choice = (
        ('Receipt', 'Receipt'),
        
        ('invoice', 'invoice'),
    )
    invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

    #def __unicode__(self):
        #return self.invoice_number


    def __str__(self):
        return  self.name 






#ADMIN APPLICATION


class AvailableMedicines(models.Model):
    
  
    comments =models.TextField(max_length=200, default='', blank=True, null=True)
    
    created =models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated =models.DateTimeField(auto_now=True, blank=True, null=True)
    medicine_name =models.CharField('Medicine Name', max_length=200, default='', blank=True, null=True)
    
    description=models.TextField('Description', max_length=1000,blank=True, null=True)
    quantity =models.IntegerField('Quantity', default=0, blank=True, null=True)
    price =models.IntegerField('Price', default=0, blank=True, null=True)

    def __str__(self):
        return  self.medicine_name + ' - ' + str(self.created)


class Appointment(models.Model):
    fname = models.CharField(max_length=50)
    sname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    message = models.TextField(max_length=50)
    sent_tarehe = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False, null=True, blank=True)
    accepted_tarehe = models.DateField(auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return  self.fname
    class Meta:

        ordering = ['-id']

    
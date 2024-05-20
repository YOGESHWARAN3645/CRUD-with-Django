import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE','api.settings')
import django 
django.setup()

from CRUD.models import User
from faker import Faker

fake_employee_list = Faker()

for i in range(5):
    emp_name= fake_employee_list.name()
    emp_id = fake_employee_list.random_int(min=1000,max=9999)
    employee_record = User.objects.create(emp_name=emp_name, emp_id=emp_id)
    employee_record.save()


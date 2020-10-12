from django.db import models  # import model class from django database


class Employee(models.Model):           # create Employee table
    resource = models.IntegerField()
    mgr_id = models.IntegerField()
    role_rollup_1 = models.IntegerField()
    role_rollup_2 = models.IntegerField()
    role_deptname = models.IntegerField()
    role_title = models.IntegerField()
    role_family_desc = models.IntegerField()
    role_family = models.IntegerField()
    # ROLE_CODE = models.IntegerField()


class Access(models.Model):             # create Access table
    status = models.CharField(max_length=20)
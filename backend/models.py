from django.db import models

class Contract(models.Model):
    name = models.CharField(max_length=100, verbose_name='合同名')
    company = models.CharField(max_length=50, verbose_name='供应商')
    date = models.DateField(verbose_name='签订日期')

    class Meta:
        verbose_name = "合同"
        verbose_name_plural = "合同"

    def __str__(self):
        return self.name


class Payment(models.Model):
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='合同')
    date = models.DateField(verbose_name='付款日期')
    percentage = models.PositiveIntegerField(verbose_name='付款百分比')
    sum = models.PositiveIntegerField(verbose_name='付款金额')

    class Meta:
        verbose_name = "付款"
        verbose_name_plural = "付款"


class Department(models.Model):
    number = models.CharField(max_length=10, verbose_name='部门编号')
    name = models.CharField(max_length=30, verbose_name='部门名称')

class Staff(models.Model):
    name = models.CharField(max_length=10, verbose_name='姓名')
    number = models.CharField(max_length=10, verbose_name='员工号')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='部门')

    class Meta:
        verbose_name = "员工"
        verbose_name_plural = "员工"

    def __str__(self):
        return self.name

class Category(models.Model):
    number = models.CharField(max_length=10)
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name = "资产分类"
        verbose_name_plural = "资产分类"

    def __str__(self):
        return self.name

class Asset(models.Model):
    name = models.CharField(max_length=50, verbose_name='设备名')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类')
    s_num = models.CharField(max_length=10, verbose_name='设备号')
    z_num = models.CharField(max_length=12, verbose_name='资产号')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='合同')
    date_in = models.DateField(verbose_name='入库日期')
    date_out = models.DateField(verbose_name='出库日期')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='使用人')
    memo = models.TextField(verbose_name='备注')

    class Meta:
        verbose_name = "资产"
        verbose_name_plural = "资产"

    def __str__(self):
        return self.name


class Consumable(models.Model):
    name = models.CharField(max_length=50, verbose_name='耗材名')
    contract = models.ForeignKey(Contract, on_delete=models.CASCADE, verbose_name='合同')
    date_in = models.DateField(verbose_name='入库日期')
    date_out = models.DateField(verbose_name='出库日期')
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, verbose_name='领用人')

    class Meta:
        verbose_name = "耗材"
        verbose_name_plural = "耗材"

    def __str__(self):
        return self.name
    



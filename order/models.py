from django.db import models

# Create your models here.
from db.base_model import BaseModel
from product.models import Products
from user.models import User, Userinfo


class Order(BaseModel):
    ORDER_status = (
        (1, '待支付'),
        (2, '待发货'),
        (3, '待收货'),
        (4, '待评价'),
        (5, '已完成'),
    )
    order_no = models.CharField(max_length=128, blank=True, verbose_name='订单编号')

    user_id = models.ForeignKey(User, related_name='order', verbose_name='用户')

    # user_address = models.ForeignKey(Userinfo, related_name='info', verbose_name='地址')
    # 订单总价格，字段类型10进制，取小数点后两位
    total_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, verbose_name='订单总价格')

    total_count = models.IntegerField(verbose_name='订单商品总数量', blank=True)
    # 订单创建时间
    create_time = models.DateTimeField(blank=True, null=True, verbose_name='创建时间')

    pay_time = models.DateTimeField(blank=True, null=True, verbose_name='付款时间')

    confirm_time = models.DateTimeField(blank=True, null=True, verbose_name='确认时间')

    reply_time = models.DateTimeField(blank=True, null=True, verbose_name='评价时间')

    order_status = models.SmallIntegerField(choices=ORDER_status, default=1, blank=True, verbose_name='订单状态')

    snap_img = models.ImageField(upload_to='snap_img', verbose_name='订单快照图片', null=True)

    sanp_name = models.CharField(max_length=32, verbose_name='订单快照名称', null=True)

    order_notes = models.CharField(max_length=32, blank=True, verbose_name='订单备注', null=True)

    class Meta:
        db_table = 'order'
        verbose_name = '订单信息'
        verbose_name_plural = verbose_name


class order_product(BaseModel):

    order_id = models.ForeignKey(Order, max_length=11,related_name='order_id', verbose_name='订单')

    product_id = models.ForeignKey(Products, max_length=11,related_name='product_id' ,verbose_name='商品')

    count = models.IntegerField(verbose_name='商品数量', blank=True)

    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True,default=0, verbose_name='商品价格')


    class Meta:
        managed = True
        db_table = 'order_product'
        verbose_name = '订单产品'
        verbose_name_plural = verbose_name

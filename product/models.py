from django.db import models

# Create your models here.
from tinymce.models import HTMLField

from db.base_model import BaseModel


# 商品模型类SPU
class Products(BaseModel):
    name = models.CharField(max_length=20, verbose_name='商品SPU名称')
    detail = models.CharField(max_length=128,blank=True, verbose_name='商品详情')

    class Meta:
        managed = True
        db_table = 'products'
        verbose_name = '商品SPU'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 商品类型类
class ProductCategory(BaseModel):
    category_name = models.CharField(max_length=20, verbose_name='分类名称')
    image = models.ImageField(upload_to='category', verbose_name='商品类型图片')

    class Meta:
        managed = True
        db_table = 'product_category'
        verbose_name = '商品分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.category_name


# 商品模型类SKU
class ProductSKU(BaseModel):
    PRODUCT_STATUS = (
        (0, '下线'),
        (1, '上线')
    )
    name = models.CharField(max_length=50, verbose_name='商品名称')
    desc = models.CharField(max_length=100, verbose_name='商品简介')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='商品价格')
    unite = models.CharField(max_length=20, verbose_name='单位')
    image = models.CharField(max_length=128, verbose_name='商品图片')
    inventory = models.IntegerField(default=1, verbose_name='库存')
    sales = models.IntegerField(default=0, verbose_name='销量')
    status = models.SmallIntegerField(default=1, choices=PRODUCT_STATUS, verbose_name='商品状态')
    type = models.ForeignKey(ProductCategory, verbose_name='所属分类')
    products = models.ForeignKey(Products, verbose_name='商品SPU')

    class Meta:
        managed = True
        db_table = 'product_sku'
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ProductImage(BaseModel):
    url = models.ImageField(upload_to='products', verbose_name='商品图片路径')
    product = models.ForeignKey(ProductSKU, verbose_name='商品')

    class Meta:
        managed = True
        db_table = 'product_image'
        verbose_name = '商品图片'
        verbose_name_plural = verbose_name


class ProductBanner(BaseModel):
    name = models.CharField(max_length=50, verbose_name='轮播图名称')
    description = models.CharField(max_length=100, verbose_name='轮播图描述')

    class Meta:
        managed = True
        db_table = 'product_banner'
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ProductBannerItem(BaseModel):
    # 确定轮播板块
    banner_id = models.ForeignKey(ProductBanner, max_length=11, verbose_name='轮播板块')
    img_id = models.ForeignKey(ProductImage, verbose_name='轮播图片')
    key_word = models.SmallIntegerField(default=1, verbose_name='轮播图顺序')

    class Meta:
        managed = True
        db_table = 'product_banner_item'
        verbose_name = '轮播图详情'
        verbose_name_plural = verbose_name

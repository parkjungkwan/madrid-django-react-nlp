import os
import django
import csv
import sys
from common.models import ValueObject, Printer, Reader
# system setup
from product.models import Vendor, Category, Product
# SET FOREIGN_KEY_CHECKS = 0;
class DbUploader():
    def __init__(self):
        vo = ValueObject()
        reader = Reader()
        self.printer = Printer()
        vo.context = 'product/data/'
        vo.fname='product.csv'
        self.csvfile = reader.new_file(vo)

    def insert_data(self):
        print('############ 2 ##########')
        self.insert_vendor()
        print('############ 3 ##########')
        self.insert_category()
        print('############ 4 ##########')
        self.insert_product()

    def insert_vendor(self):
        with open(self.csvfile, newline='', encoding='utf8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                if not Vendor.objects.filter(name=row['vendor']).exists():
                    vendor = Vendor.objects.create(name=row['vendor'])
        print('VENDOR DATA UPLOADED SUCCESSFULY!')

    def insert_category(self):
        with open(self.csvfile, newline='', encoding='utf8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                if not Category.objects.filter(name=row['category']).exists():
                    category_id = Category.objects.create(name=row['category'])
                    print(f' 2 >>>> {category_id}')
        print('CATEGORY DATA UPLOADED SUCCESSFULY!')

    def insert_product(self):
        with open(self.csvfile, newline='', encoding='utf8') as csvfile:
            data_reader = csv.DictReader(csvfile)
            for row in data_reader:
                category_id = Category.objects.get(id=row['category'])
                products = row['product'].split(',')

                if not Product.objects.filter(name=row['product'],
                                              category=category_id).exists():
                    Product.objects.create(name=row['product'] if row['product'] else category_id.name,
                                           price=row['price'],
                                           category=category_id, )
            print('PRODUCT DATA UPLOADED SUCCESSFULY!')





#!/usr/bin/env python3
#coding=utf-8
'''
name : Jack Ma
date : 2018-10-13
email: ...
modules: pymysql
This is a module for creating hotel DB
'''
import pymysql
# import sys
import config

# if len(sys.argv) < 2:
#     print("argv is error!")
#     sys.exit('请在控制台输入数据库密码．')
    
#创建酒店数据库(如果不存在)
try:
    db = pymysql.connect(host=config.HOST,\
                         user = config.USER,\
                         password= config.PASSWORD,\
                         database='',\
                         use_unicode=True,\
                         charset="utf8")
    cursor = db.cursor()
    sql = 'create database if not exists hotelDB default character set utf8'
    cursor.execute(sql)
    cursor.execute('use hotelDB')
    print("创建/连接酒店数据库成功！")
except Exception as e:
    sys.exit("创建/连接数据库失败！")

# 创建用户信息表
try:
    sql = "create table user_info(id int primary key auto_increment, name varchar(50), pwd varchar(20));"
    cursor.execute(sql)
    print("创建用户表信息成功！")
except Exception as e:
    print(e)
    sys.exit("创建用户表信息表失败，程序退出！")

#创建房间表
sql = "create table room_info( 房间类型 varchar(50),房间号 int,押金 int,价格 int,\
    会员价 int,房间状态 varchar(25),楼层 int)character set utf8;"
cursor.execute(sql)
print("创建客房信息表成功！")

#插入房间信息
try:
    n = 6101
    while n <= 6130:
        cursor.execute("insert into room_info values('单间','%s',100,188,168,'空闲',1)" % n)
        n += 1

    n = 6201
    while n <= 6230:
        cursor.execute("insert into room_info values('标准间','%s',100,288,258,'空闲',2)" % n)
        n += 1

    n = 6301
    while n <= 6320:
        cursor.execute("insert into room_info values('豪华标准间','%s',200,588,548,'空闲',3)" % n)
        n += 1

    n = 6401
    while n <= 6420:
        cursor.execute("insert into room_info values('商务间','%s',200,688,638,'空闲',4)" % n)
        n += 1

    n = 6501
    while n <= 6510:
        cursor.execute("insert into room_info values('行政间','%s',300,1388,1328,'空闲',5)" % n)
        n += 1

    n = 6601
    while n <= 6610:
        cursor.execute("insert into room_info values('双套间','%s',300,1888,1818,'空闲',6)" % n)
        n += 1

    n = 6701
    while n <= 6705:
        cursor.execute("insert into room_info values('高级套房','%s',500,3888,3808,'空闲',7)" % n)
        n += 1

    n = 6801
    while n <= 6802:
        cursor.execute("insert into room_info values('总统套房','%s',2000,18888,18888,'空闲',8)" % n)
        n += 1
    db.commit()
    print("初始化客房成功！")
except Exception as e:
    print(e)
    db.rollback()
    sys.exit("插入房间信息失败！")

#创建顾客预定信息表
try:
    sql = "create table book_info(\
            id int primary key auto_increment,\
            name varchar(30),\
            phone_num char(11),\
            room_num char(4),\
            start_date datetime default now(),\
            end_date varchar(30))charset = utf8;"
    cursor.execute(sql)
    db.commit()
    print("创建顾客预定信息表成功！")
except Exception as e:
    db.rollback()
    print("创建顾客预定表失败",e)

#创建入住信息表
try:
    sql = "create table check_in_info(\
            id int primary key auto_increment,\
            name varchar(30),\
            phone_num char(11),\
            ID_num char(18),\
            gender enum('男','女'),\
            room_num char(4),\
            deposit int,\
            price int,\
            vip_price int,\
            people_count int,\
            start_date datetime default now(),\
            end_date varchar(30))charset = utf8;"
    cursor.execute(sql)
    db.commit()
    print("创建顾客入住信息表成功！")
except Exception as e:
    db.rollback()
    print("创建入住信息表失败！",e)

#创建历史入住信息表
try:
    sql = "create table live_history(\
            id int primary key auto_increment,\
            name varchar(10),\
            phone_num char(11),\
            ID_num char(18),\
            gender enum('男','女'),\
            room_num char(4),\
            deposit int,\
            price int,\
            people_count int,\
            start_date varchar(30),\
            end_date varchar(30))charset = utf8;"
    cursor.execute(sql)
    db.commit()
    print("创建入住历史信息表成功！")
except Exception as e:
    db.rollback()
    print("创建顾客入住表失败！",e)


#创建vip信息表
sql = "create table vip_info(\
        ID int primary key auto_increment, \
        name varchar(20) not null, \
        sex enum('男','女'), \
        tel char(11) unique, \
        YE int not null,\
        open_time datetime default now())auto_increment=100001,character set utf8"
try:
    cursor.execute(sql)
    print("创建vip客户信息表成功！")
except Exception as e:
    print(e)
    print("创建vip表失败")

cursor.close()
db.close()
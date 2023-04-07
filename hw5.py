#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 과제

number = input('세 자리 정수 입력 : ')

def read_single_digit(n) :
    if n == '1' :
        return '일'
    if n == '2' :
        return '이'
    if n == '3' :
        return '삼'
    if n == '4' :
        return '사'
    if n == '5' :
        return '오'
    if n == '6' :
        return '육'
    if n == '7' :
        return '칠'
    if n == '8' :
        return '팔'
    if n == '9' :
        return '구'
    if n == '0' :
        return '영'

def read_number(number) :
    a = read_single_digit(number[0]) # 백의 자리 숫자 
    b = read_single_digit(number[1]) # 십의 자리 숫자
    c = read_single_digit(number[2]) # 일의 자리 숫자
    print(a, b, c)

read_number(number)


# In[ ]:





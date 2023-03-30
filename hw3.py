#!/usr/bin/env python
# coding: utf-8

# In[3]:


def get_fixed_price_A() : # A의 할인 전 가격
    fix_A = 100 * 1/(100 - rate) * dis_A
    return fix_A
    

def get_fixed_price_B() : # B의 할인 전 가격
    fix_B = 100 * 1/(100 - rate) * dis_B
    return fix_B


rate = int(input('할인율은? '))
dis_A = int(input('A 상품의 할인된 가격은? '))
dis_B = int(input('B 상품의 할인된 가격은? '))

print('A 상품의 정가는', get_fixed_price_A(), '원')
print('B 상품의 정가는', get_fixed_price_B(), '원')


# In[ ]:





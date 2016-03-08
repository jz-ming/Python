# -*- coding:utf-8 -*-
#height =1.75
#weight =80.5
#s=weight/(height*height)
height=input("请输入您的身高(m):")
weight=input("请输入您的体重(kg):")
bmi= float(weight)/(float(height)**2)
if bmi<=18.5:
    print(bmi)
    print('过轻')
elif  18.5<bmi<=25:
    print(bmi)
    print('正常')
elif 25<bmi<=28:
    print(bmi)
    print('过重')
elif 28<bmi<=32:
    print('肥胖')
else:
    print('严重肥胖')
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 23:24:36 2018

@author: wewu
"""

"""
answer for exereice #1: Write a python function to sort any list of integers. 
(You could not use any built-in sort functions.)

"""
def bubble_sort(int_list):
    list_size = len(int_list)
    
    sorted_num = 0
    while sorted_num < list_size -1:
        idx = 0
        while idx < list_size - 1 - sorted_num :
            if int_list[idx] > int_list[idx + 1] :
                int_list[idx], int_list[idx + 1] = int_list[idx + 1], int_list[idx]
            idx += 1
        sorted_num += 1
        
    return int_list
    
def bubble_sort_recursion(int_list):
    list_size = len(int_list)
    
    if list_size < 2:
        return int_list
    
    idx = 0
    while idx < list_size -1:
        if int_list[idx] > int_list[idx + 1]:
            int_list[idx], int_list[idx + 1] = int_list[idx + 1], int_list[idx]
        idx += 1
    
    rest_list =  bubble_sort_recursion(int_list[:-1])
    rest_list.append(int_list[-1])
    return rest_list

x = bubble_sort_recursion([3, -1])
x
/**
 * @file rectangle.cpp
 * @author tarunr (tarunr@email.sc.edu)
 * @brief 
 * @version 0.1
 * @date 2024-02-06
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include <iostream>
#include "rectangle.h"

Rectangle::Rectangle(double length, double width)
{
    
    this->length = length;
    this->width = width;
}

double Rectangle::calculateArea() 
{
    return length*width;
}

double Rectangle::calculatePerimeter()
{
    return 2*(length+width);
}



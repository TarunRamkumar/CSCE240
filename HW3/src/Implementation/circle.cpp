/**
 * @file circle.cpp
 * @author tarunr (tarunr@email.sc.edu)
 * @brief 
 * @version 0.1
 * @date 2024-02-06
 * 
 * @copyright Copyright (c) 2024
 * 
 */
#include <iostream>
#include "circle.h"

Circle::Circle(double radius)
{
    
    this->radius = radius;
}

double Circle::calculateArea() 
{
    return PI*radius*radius;
}

double Circle::calculatePerimeter()
{
    return 2*PI*radius;
}





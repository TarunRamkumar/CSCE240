/**
 * @file shape.cpp
 * @author tarunr
 * @brief 
 * @version 0.1
 * @date 2024-02-06
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#include <iostream>
#include "shape.h"

Shape::Shape()
{
    this->errorMessage = "Not enough information to calculate";
    this->area = 0;
    this->perimeter = 0;
}
double Shape::getArea()
{
    return area;
}

double Shape::getPerimeter()
{
    return perimeter;
}

string Shape::getErrorMessage()
{
    return errorMessage;
}

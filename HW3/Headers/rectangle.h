/**
 * @file rectangle.h
 * @author tarunr
 * @brief 
 * @version 0.1
 * @date 2024-02-06
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#ifndef RECTANGLE_H_
#define RECTANGLE_H_

#include <iostream>
#include <string>
#include "shape.h"

using namespace std;

class Rectangle: public Shape
{
    private:
        double length;
        double width;

    public:
        Rectangle(double length, double width);
        virtual double calculateArea();
        virtual double calculatePerimeter();
        virtual ~Rectangle();


};

#endif /*RECTANGLE_H_*/
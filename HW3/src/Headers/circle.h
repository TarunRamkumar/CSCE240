/**
 * @file circle.h
 * @author tarunr
 * @brief 
 * @version 0.1
 * @date 2024-02-06
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#ifndef CIRCLE_H_
#define CIRCLE_H_

#include <iostream>
#include <string>
#include <math.h>
#include "shape.h"
using namespace std;

class Circle: public Shape
{
    private:
        double radius;
        double const PI = M_PI;

    public:
        Circle(double radius);
        virtual double calculateArea();
        virtual double calculatePerimeter();
        virtual ~Circle();


};

#endif /*CIRCLE_H_*/
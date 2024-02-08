/**
 * @file triangle.h
 * @author tarunr
 * @brief 
 * @version 0.1
 * @date 2024-02-06
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#ifndef TRIANGLE_H_
#define TRIANGLE_H_

#include <iostream>
#include <string>
#include "shape.h"

using namespace std;

class Triangle: public Shape
{
    private:
        double sideA;
        double sideB;
        double sideC;

    public:
        Triangle(double sideA, double sideB, double sideC);
        virtual double calculateArea();
        virtual double calculatePerimeter();
        virtual ~Triangle();


};

#endif /*TRIANGLE_H_*/
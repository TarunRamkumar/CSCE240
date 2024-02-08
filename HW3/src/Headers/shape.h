/**
 * @file shape.h
 * @author tarunr
 * @brief 
 * @version 0.1
 * @date 2024-02-06
 * 
 * @copyright Copyright (c) 2024
 * 
 */

#ifndef SHAPE_H_
#define SHAPE_H_

#include <iostream>
#include <string>
using namespace std;

class Shape
{
    
    protected:
        double area;
        double perimeter;
        string errorMessage;
    
    public:
        Shape();

        virtual ~Shape();

        double getArea();
        double getPerimeter();
        virtual double calculateArea() = 0;
        virtual double calculatePerimeter() = 0;
        string getErrorMessage();





};

#endif /* SHAPE_H_ */
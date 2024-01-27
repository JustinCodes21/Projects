#include <iostream>
#include <cmath>
#include "functionPrototypes.h"

using namespace std;
const double PI = 3.14;

int main()
{
    cout << "\n----------------------------------------------------------" << endl;
    cout << "             Welcome to my math calculator                  " << endl << endl;
    cout << "             Enter 1: Quadratic equation                    " << endl;
    cout << "             Enter 2: Area of a circle                      " << endl;
    cout << "             Enter 3: Volume of a sphere                    " << endl;
    cout << "             Enter 4: Fibonacci sequence                    " << endl;
    cout << "  ----------------------------------------------------------" << endl;

    int response;
    cout << "Answer: ";
    cin >> response;

    if(response == 1)
    {
        double a, b, c, x1, x2, y, discriminantResult, vertex;

        getUserInputForQuadraticEquation(a, b, c);
        discriminantResult = calculateDiscriminant(a, b, c);
        x1 = findFirstXIntercept(discriminantResult, a, b);
        x2 = findSecondXIntercept(discriminantResult, a, b);
        vertex = calculateVertex(a, b, c);
        y = calculateYIntercept(a, b, c);

        if(discriminantResult > 0)
        {
            cout << "\nReal parabola with two roots" << endl;
            parabolaWithTwoRealRoots(a, b, c, discriminantResult);
        }
        else if(discriminantResult == 0)
        {
            cout << "\nReal parabola with one root" << endl;
            parabolaWithOneRealRoot(a, b, c, discriminantResult);
        }
        else
        {
            cout << "\nImaginary parabola with zero roots" << endl;
            parabolaWithZeroRoots(a, b, c, discriminantResult);
        }
    }
    else if(response == 2)
    {
        computeAreaOfACircle();
    }
    else if(response == 3)
    {
        computeVolumeOfASphere();
    }
    else if(response == 4)
    {
        findFibonacciNumber();
    }

    return 0;
}

void getUserInputForQuadraticEquation(double &a, double &b, double &c)
{
    cout << "Enter the coefficients of your quadratic equation" << endl;
    cout << "a: ";
    cin >> a;
    cout << "b: ";
    cin >> b;
    cout << "c: ";
    cin >> c;
}

//TODO - can further clean this function up
void parabolaWithTwoRealRoots(double a, double b, double c, double discriminantResult)
{
    cout << "Discriminant: " << calculateDiscriminant(a, b, c) << endl;
    cout << "Roots: x = " << findFirstXIntercept(discriminantResult, a, b) << ", " << findSecondXIntercept(discriminantResult, a, b) << endl;
    cout << "Axis of symmetry: " << axisOfSymmetry(a, b) << endl;
    cout << "Vertex: (" << axisOfSymmetry(a, b) << ", " << calculateVertex(a, b, c) << ")" << endl;
    cout << "Y-intercept: (0, " << calculateYIntercept(a, b, c) << ")" << endl;
    domainAndRange(a, calculateVertex(a, b, c));
}

//TODO - can further clean this function up
void parabolaWithOneRealRoot(double a, double b, double c, double discriminantResult)
{
    cout << "Discriminant: " << calculateDiscriminant(a, b, c) << endl;
    cout << "Root: x = " << findFirstXIntercept(discriminantResult, a, b) << endl;
    cout << "Axis of symmetry: " << axisOfSymmetry(a, b) << endl;
    cout << "Vertex: (" <<  axisOfSymmetry(a, b) << ", " << calculateVertex(a, b, c) << ")" << endl;
    cout << "Y-intercept: (0, " << calculateYIntercept(a, b, c) << ")" << endl;
    domainAndRange(a, calculateVertex(a, b, c));
}

//TODO - can further clean this function up
void parabolaWithZeroRoots(double a, double b, double c, double discriminantResult)
{
    cout << "Discriminant: " << calculateDiscriminant(a, b, c) << endl; 
    cout << "Imaginary roots: \nx = " 
        << findFirstImaginaryRoot(discriminantResult, a, b) << "i, " << findSecondImaginaryRoot(discriminantResult, a, b) << "i" << endl;
    cout << "Vertex: (" << axisOfSymmetry(a, b) << ", " << calculateVertex(a, b, c) << ")" << endl;
    cout << "Y-intercept: (0, " << calculateYIntercept(a, b, c) << ")" << endl;
    domainAndRange(a, calculateVertex(a, b, c));
}

double calculateDiscriminant(double a, double b, double c)
{
    return b*b - 4*a*c;
}

double findFirstXIntercept(double discriminant, double a, double b)
{
    double x1;
    x1 = (-b + sqrt(discriminant)) / (2*a);

    return x1;
}

double findSecondXIntercept(double discriminant, double a, double b)
{
    double x2;
    x2 = (-b - sqrt(discriminant)) / (2*a);

    return x2;
}

double axisOfSymmetry(double a, double b)
{
    return abs((-b)/(2*a));
}

double calculateVertex(double a, double b, double c)
{
    double x, vertex;
    x = -b / 2*a;
    vertex = a*x*x + b*x + c;

    return vertex;
}

double calculateYIntercept(double a, double b, double c)
{
    return a*0 + b*0 + c;
}

double findFirstImaginaryRoot(double discriminant, double a, double b)
{
    double x1;
    x1 = (-b)/(2*a) + (sqrt(abs(discriminant))) / (2*a);

    return x1;
}

double findSecondImaginaryRoot(double discriminant, double a, double b)
{
    double x2;
    x2 = (-b)/(2*a) - (sqrt(abs(discriminant))) / (2*a);

    return x2;
}

void domainAndRange(double a, double vertex)
{
    cout << "Domain: (-infinity, infinity)" << endl;
    if(a >= 1)
    {
        cout << "Range: [" << vertex << ", infinity)" << endl;
    }
    else
    {
        cout << "Range: (-infinity, " << vertex << "]" << endl;
    }
}

void computeAreaOfACircle()
{
    double radius, area;
    cout << "\nEnter radius: ";
    cin >> radius;
    area = PI * radius * radius;
    cout << "Area: " << area << endl;
}

void computeVolumeOfASphere()
{
    double radius, volume;
    cout << "\nEnter radius: ";
    cin >> radius;
    volume = (4/3)*(PI * radius * radius * radius);
    cout << "Volume: " << volume << endl;
}

long int calculateFibonacciNumber(int n)
{
    if(n == 0 || n == 1)
    {
        return n;
    }
    return calculateFibonacciNumber(n - 1) + calculateFibonacciNumber(n - 2);
}

void findFibonacciNumber()
{
    int target;
    cout << "Enter the term number to sum up to: ";
    cin >> target;
    cout << "Fibonacci number at the " << target << "th term: " << calculateFibonacciNumber(target) << endl;
}


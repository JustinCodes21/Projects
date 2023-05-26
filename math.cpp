
#include <iostream>
#include <cmath>
//#include <math>
using namespace std;
const double PI = 3.14;

double discriminant(double a, double b, double c)
{

    return (b*b - 4*a*c);
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
            cout << "(-infinity, " << vertex << "]" << endl;
    }

}

void quadraticEquation()
{

    double a, b, c;
    cout << "Enter the coefficients of your quadratic equation" << endl;

    cout << "a: ";
    cin >> a;
    cout << "b: ";
    cin >> b;
    cout << "c: ";
    cin >> c;

    double disc = discriminant(a, b, c);
    
        //Quadratic formula
    double x1 = (-b + sqrt(disc)) / (2*a);
    double x2 = (-b - sqrt(disc)) / (2*a);
    
       //Calculate vertex of parabola
    double x = -b / 2*a;
    double vertex = a*x*x + b*x + c;
    
      //Calculate y-intercept
    double y = a * 0 + b * 0 + c;


    if(disc > 0)
    {
        cout << "\nReal parabola" << endl;
        cout << "Discriminant: " << disc << endl;
        cout << "Roots: x = " << x1 << ", " << x2 << endl;
        cout << "Vertex: (" << x << ", " << vertex << ")" << endl;
        cout << "Y-intercept: (0, " << y << ")" << endl;
        domainAndRange(a, vertex);
    }
    else if(disc == 0)
    {
        cout << "\nReal parabola" << endl;
        cout << "Discriminant: " << disc << endl;
        cout << "Root: x = " << x1 << endl;
        cout << "Vertex: (" << x << ", " << vertex << ")" << endl;
        cout << "Y-intercept: (0, " << y << ")" << endl;
        domainAndRange(a, vertex);
    }
    else
    {
        cout << "\nImaginary parabola" << endl;
        cout << "Discriminant: " << disc << endl;
        cout << "Imaginary roots: ";
        double x1 = (-b)/(2*a) + (sqrt(abs(disc))) / (2*a);
        double x2 = (-b)/(2*a) - (sqrt(abs(disc))) / (2*a);

        cout << "x = " << x1 << "i, " << x2 << "i" << endl;
        cout << "Vertex: (" << x << ", " << vertex << ")" << endl;
        cout << "Y-intercept: (0, " << y << ")" << endl;
        domainAndRange(a, vertex);
    }
}

void areaOfCircle()
{
    double radius;
    cout << "\nEnter radius: ";
    cin >> radius;

    double area = PI * radius * radius;

    cout << "Area: " << area << endl;
}

void volumeOfSphere()
{
    double radius;
    cout << "\nEnter radius: ";
    cin >> radius;

    double volume = (4/3)*(PI * radius * radius * radius);

    cout << "Volume: " << volume << endl;
}

void fibonacci(int target = 0)
{
    

}


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

    switch(response)
    {
        case 1:
            quadraticEquation();
        break;
        case 2:
            areaOfCircle();
        break;
        case 3:
            volumeOfSphere();
        break;
        case 4:
            fibonacci();
        break;
    }

    return 0;
}
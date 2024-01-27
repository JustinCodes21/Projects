#ifndef FUNCTIONS_H
#define FUNCTIONS_H

void computeParabola();
void getUserInputForQuadraticEquation(double &a, double &b, double &c);
void parabolaWithTwoRealRoots(double a, double b, double c, double discriminantResult);
void parabolaWithOneRealRoot(double a, double b, double c, double discriminantResult);
void parabolaWithZeroRoots(double a, double b, double c, double discriminantResult);
double findFirstXIntercept(double discriminant, double a, double b);
double findSecondXIntercept(double discriminant, double a, double b);
double calculateVertex(double a, double b, double c);
double findFirstImaginaryRoot(double discriminant, double a, double b);
double findSecondImaginaryRoot(double discriminant, double a, double b);
double calculateDiscriminant(double a, double b, double c);
double axisOfSymmetry(double a, double b);
double calculateYIntercept(double a, double b, double c);
void domainAndRange(double a, double vertex);
void computeAreaOfACircle();
void computeVolumeOfASphere();
long int calculateFibonacciNumber(int n);
void findFibonacciNumber();

#endif 
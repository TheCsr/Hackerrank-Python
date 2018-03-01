HackerLand University has the following grading policy:

Every student receives a  in the inclusive range from  to .
Any  less than  is a failing grade.
Sam is a professor at the university and likes to round each student's  according to these rules:

If the difference between the  and the next multiple of  is less than , round  up to the next multiple of .
If the value of  is less than , no rounding occurs as the result will still be a failing grade.
For example,  will be rounded to  but  will not be rounded because the rounding would result in a number that is less than .

Given the initial value of  for each of Sam's  students, write code to automate the rounding process. Complete the function solve that takes an integer array of all grades, and return an integer array consisting of the rounded grades. For each , round it according to the rules above and print the result on a new line.

Input Format

The first line contains a single integer denoting  (the number of students). 
Each line  of the  subsequent lines contains a single integer, , denoting student 's grade.





#include <bits/stdc++.h>

using namespace std;

vector < int > solve(vector < int > grades){
    vector<int> g1;
    
     int multiple;
    for(int i=0 ; i< grades.size(); i++)
    {
        if(grades[i]>=38)
        {
        for(int j=0; j<5;j++)
        {
            if((grades[i]+j)%5==0)
            {
                multiple=grades[i]+j;
            }
            else{
                continue;
            }
        }
        if(multiple-grades[i]<3)
            {
                g1.push_back(multiple);
            }
            else{
                g1.push_back(grades[i]);
            }
        
        }
        else
        {
             g1.push_back(grades[i]);
        }
    }
    return g1;
    
    
}

int main() {
    int n;
    cin >> n;
    vector<int> grades(n);
    for(int grades_i = 0; grades_i < n; grades_i++){
       cin >> grades[grades_i];
    }
    vector < int > result = solve(grades);
    for (ssize_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i != result.size() - 1 ? "\n" : "");
    }
    cout << endl;
    

    return 0;
}

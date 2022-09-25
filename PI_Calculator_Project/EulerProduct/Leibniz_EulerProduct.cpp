//after looking over these old programs I came across another method and it didn't seem like a normal series. 
//also I decided to write it in c++ because I like it a lot more than the baby language which calls itself python. 
//after researching, I found out that the Leibniz formula can be converted to a Dirichlet series. After researching more about that, it seems like it is a series with 
// complex (lateral) components, apologizes to any math major reading this if im wrong.  

//It is also called an euler product. 
//the series isn't adding every term, but rather multiplying. 
//Each term is: 
//                      (the next prime number)
//                   _____________________________      (divided by)

//              (closest multiple of 4 to the prime number)

//example: (3/4)*(5/4)*(7/8)*(11/12)*(13/12) etc. 

#include <iostream>
#include <string>
#include <cmath>
#include <thread>
#include <chrono>

using namespace std::this_thread;
using namespace std::chrono;


using namespace std;

int is_prime(int num){
    //getting rid of the possible factors.
    if (num <= 1){
        return false; 
    }
    else if (num % 2 == 0){
        return false;
    }
    else if (num ==1 || num ==2){ //the reason 2 is included as "not a prime number" is because 2 isn't the first prime in the series.
        return false;
    }
    

    int k = 3; 

    while (k <= sqrt(num)){ //going up to the sqrt of the number is the most efficient way I found to test for a prime number 
        if (num % k == 0){
            return false;
        }
        k += 2;
    }

    return true; //once the program reaches here then the number is a prime number
}

int main(){

    float pi_part = 1;
    int num = 1;
    float prime;
    float near_four_mult;
    float next_term; 
    
    
    cout << "Hello, this program will allow you to calculate pi. " << endl;
    
    //Generating prime numbers
    while (true){
        if (is_prime(num)){
            prime = num;
            if (num % 4 == 1){
                near_four_mult = ((num - 1));
            }
            else if (num % 4 == 3){
                near_four_mult = ((num + 1));
            }

            next_term = prime / near_four_mult;
            
            pi_part *= next_term;
            float pi = pi_part * 4;
            cout << pi << endl;
            
        }
        num++;
        
        
    }
    // if(is_prime(num)){
    //     printf("Number is prime");
    // }
    // else {
    //     printf("Not prime");
    // }
    return 0;
}
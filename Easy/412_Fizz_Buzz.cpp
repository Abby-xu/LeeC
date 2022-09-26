# include<bits/stdc++.h>
using namespace std;

vector<string> fizzBuzz(int n){ 
    // method 1
    vector<string> out;
    for (int i=1; i<=n; i++) {
        if(!(i%3)) {
            if (!(i%5))
                out.push_back("FizzBuzz");
            else
                out.push_back("Fizz");
        } else if (!(i%5))
            out.push_back("Buzz");
        else
            out.push_back(to_string(i));
    }   
    // return out;
     
    // method 2
    vector<string> res(n);
    for (int j = 1; j <= n; j++)
        res[j-1] = to_string(j);
    for (int j = 2; j <= n; j+= 3)
        res[j] = "Fizz";
    for (int j = 4; j <= n; j += 5)
        res[j] = "Buzz";
    for (int j = 14; j <= n; j += 15) 
        res[j] = "FizzBuzz";
    return res;
}
int main() {}
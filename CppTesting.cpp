#include <iostream>
using namespace std;

int main() {
    int counter = 0;
    
    // for loop
    for(counter = 0; counter < 10; ++counter) {
        //this is for counting to ten
        cout << "The counter is: " << counter << endl;
    };
    
    //reset counter to 0 and while loop
    counter = 0;
    while (true) {
        cout << "While loop counter is: " << counter << endl;
        counter++;
        if (counter < 10) {
            break;
        }
    };
    
    // do while loop
    counter = 0;
    do {
        cout << "Do while loop counter is: " << counter << endl;
        counter++;
    } while (counter < 10);
    
    cout << "All loops passed" << endl;
    
    return 0;
}
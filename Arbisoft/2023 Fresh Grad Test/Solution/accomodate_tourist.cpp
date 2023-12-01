#include <iostream>
#include <vector>
#include <algorithm>

int accommodateTourists(std::vector<int>& tourists, std::vector<int>& seats) {
   int touristsSum = 0;
   int seatsNum = 0;
   for(int i=0;i<tourists.size();i++)
            touristsSum  += tourists[i];
    sort(seats.rbegin(),seats.rend());
   
    
    int seatIndex = 0;
     while(touristsSum > 0){
        touristsSum -= seats[seatIndex++];
        seatsNum++;
     }
     
     return seatsNum;
}

int main() {
    // instead of reading from file example is taken

     std::vector<int> tourists = {1,2,3,4};
     std::vector<int> seats = {1,2,3,4};
    // vectors are array in cpp 

    int result = accommodateTourists(tourists, seats);

    std::cout << "Number of groups accommodated: " << result << std::endl;

    return 0;
}

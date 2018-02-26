#include <iostream>
#include <stdlib.h>
using namespace std;

float doorRevealer(bool choice, float trials) {
	int stay = 0;
	int swit = 0;
	int cnt = 0;

	while (cnt < trials) { //to repeat process N times
		//randomly generate the doors
		int winner = rand()%3;
		int switchedDoor = rand()%3;
		int firstChoice = rand()%3;
		int revealedDoor = rand()%3;

		//these two loops ensure the same door isn't used twice
		while (firstChoice == revealedDoor || winner == revealedDoor) {
			revealedDoor = rand()%3;
		}
		while (firstChoice == switchedDoor || revealedDoor == switchedDoor) {
			switchedDoor = rand()%3;
		}

		//increment
		if (choice) { //stay
			if (firstChoice == winner) {
				stay++;
			}
		}
		else { //switch
			if (switchedDoor == winner) {
				swit++;
			}
		}
		cnt++;
	}

	//return precentages
	if (choice) {
		return (stay/trials)*100;
	} 
	else {
		return (swit/trials)*100;
	}
}

void print(float stay, float swit, int tot) { //print the stuff out obviously
	cout << "Out of " << tot << " trials:" << endl;
	cout << "The contestant won " << stay << "%" << " of the time by staying." << endl;
	cout << "The contestant won " << swit << "%" << " of the time by switching." << endl << endl;
}

int main() {
	//switch trials
	float Sw100 = doorRevealer(false,100);
	float Sw1000 = doorRevealer(false,1000);
	float Sw10000 = doorRevealer(false,10000);
	float Sw100000 = doorRevealer(false,100000);

	//stay trials
	float St100 = doorRevealer(true,100);
	float St1000 = doorRevealer(true,1000);
	float St10000 = doorRevealer(true,10000);
	float St100000 = doorRevealer(true,100000);
	
	//print
	print(St100,Sw100,100);
	print(St1000,Sw1000,1000);
	print(St10000,Sw10000,10000);
	print(St100000,Sw100000,100000);
	return 0;
}
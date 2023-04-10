#include <stdio.h>

int main(){
	int a = 85;
	int b = 15;
	int sum = a + b;

	if (sum != (a+b)){
		printf("a+b와 sum값이 다릅니다:)");
	}
	else {
		printf("a+b와 sum값이 같습니다!!");
	}
	return 0;
}

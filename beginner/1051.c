#include <stdio.h>

int main(int argc, char const *argv[])
{
	float salary;
	scanf("%f", &salary);

	float tax_sum = 0;

	if (salary > 4500.0) {
		tax_sum += (salary - 4500.0) * 0.28;
	}

	if (salary > 3000.0) {
		if (salary - 3000.0 > 1500.0) {
			tax_sum += 1500.0 * 0.18;
		} else {
			tax_sum += (salary - 3000.0) * 0.18;
		}
	}

	if (salary > 2000.0) {
		if (salary - 2000.0 > 1000.0) {
			tax_sum += 1000.0 * 0.08;
		} else {
			tax_sum += (salary - 2000.0) * 0.08;
		}
	}

	if (tax_sum > 0) {
		printf("R$ %.2f\n", tax_sum);
	} else {
		printf("Isento\n");
	}

	return 0;
}
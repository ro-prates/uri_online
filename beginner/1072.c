#include<stdio.h>
int main()
{
    int i, dentro = 0, fora = 0, teste, n;
        scanf("%d", &n);


            for(i = 0; i < n; i++){
                scanf("%d", &teste);
                if(teste >= 10 && teste <= 20){
                    dentro++;
                }else fora++;
            }

        printf("%d in\n", dentro);
        printf("%d out\n", fora);
    return 0;
}
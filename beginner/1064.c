#include<stdio.h>
int main()
{
    int count=0,n=0;
    float a, soma = 0, resultado = 0;
    while(n!=6){
        scanf("%f",&a);
        if(a>=0){
            soma += a;
            count++;
        }
        n++;
    }
    resultado = soma / count;
    printf("%d valores positivos\n",count);
    printf("%.1f\n",resultado);
    return 0;
}
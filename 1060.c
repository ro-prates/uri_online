#include<stdio.h>
int main()
{
    int count=0,n=0;
    float a;
    while(n!=6){
        scanf("%f",&a);
        if(a>=0){
            count++;
        }
        n++;
    }
    printf("%d valores positivos\n",count);
    return 0;
}
#include <stdio.h>
int main(void)
{
   int satirsayisi;
    int sutunsayisi;
    printf("Lutfen yazmak istediginiz satir sayisini yaziniz..\n");
    scanf("%d",&satirsayisi);
    printf("Lutfen yazmak istediginiz sutun sayisini yaziniz..\n");
    scanf("%d",&sutunsayisi);
    int cokboyutlu[satirsayisi][sutunsayisi];
    for(int i = 0;i<satirsayisi;i++){
        for(int j = 0;j<sutunsayisi;j++){
            printf("%d satirinin %d sutunundaki sayi...\n",i+1,j+1);
            scanf("%d",&cokboyutlu[i][j]);
        }
    }
     for(int i = 0;i<satirsayisi;i++){
        for(int j = 0;j<sutunsayisi;j++){
            printf("%d \n",cokboyutlu[i][j]);
        }
    }  /*
    for(int i = 1 ; i<=10;i++){
        printf("1 x %d = %d\t",i,i*1);
        printf("2 x %d = %d\t",i,i*2);
        printf("3 x %d = %d\t",i,i*3);
        printf("4 x %d = %d\t",i,i*4);
        printf("5 x %d = %d\t",i,i*5);
        printf("6 x %d = %d\t",i,i*6);
        printf("7 x %d = %d\t",i,i*7);
        printf("8 x %d = %d\t",i,i*8);
        printf("9 x %d = %d\t",i,i*9);
        printf("10 x %d = %d\n",i,i*10);
    }
*/
}
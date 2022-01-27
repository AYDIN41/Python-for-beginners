#include <iostream>

using namespace std;

int main()
{
    char isim[8] = "Emirhan";
    isim[4] = 'a';
    for(int i = 0;i<8;i++){
            cout << isim[i] << endl;
    }

  /*  int sayi;
    int yuzbinler,onbinler,binler,yuzler,onlar,birler,toplam=0;
    cout<< "Lutfen 6 haneli bir sayi giriniz.." << endl;
    cin>>sayi;
    yuzbinler = sayi / 100000;
    onbinler = (sayi % 100000) / 10000;
    binler = (sayi % 10000) / 1000;
    yuzler = (sayi % 1000) / 100;
    onlar = (sayi % 100) / 10;
    birler = (sayi % 10);
    toplam = yuzbinler + onbinler + binler + yuzler + onlar +birler;
    cout << "Girmis oldugunuz sayi degerleri: " << yuzbinler << "   " << onbinler << "      " << binler << "    " << yuzler << "    " << onlar << "     " << birler << endl;
    cout << "Girmis oldugunuz sayi degerlerinin toplami: " << toplam << endl;*/
}
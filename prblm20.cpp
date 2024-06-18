//create a datastructure for set - add(no repetition), remove, print (ascending order)
#include <iostream>
using namespace std;

long long x=0; //32bit
void add(){
    int n=0;
    cout<<"Enter num: ";
    cin>>n;
    x=x|(1<<n);
    
}
void remove(){
    int n=0;
    cout<<"Enter num: ";
    cin>>n;
    x=x&(~(1<<n));
}
void print_s(){
    for (int i=0;i<32;i++)
    {
        if ((x&(1<<i)))
        {  
           cout<<i<<" "; }
    }
    cout<<endl;
}
int main()
{  
    char c='a';
    do{
        cout<<"Enter choice: ";
        cin>>c;
        switch(c){
            case 'a':
                 add();
                 break;
            case 'r':
                 remove();
                 break;
            case 'p':
                 print_s();
                 break;
            case 'q':
                 break;
            default:
                 cout<<"Invalid choice!";
        }
    }while(c!='q');
    
    return 0;
}
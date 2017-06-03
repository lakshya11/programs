//http://www.geeksforgeeks.org/reverse-words-in-a-given-string/

#include<iostream>
#include<cstring>

using namespace std;

void reverse(int start,int end,char * str){
  if(start>=0 && end >=0){
    while(start<end){
      char  temp = str[start];
      str[start]= str[end];
      str[end] = temp;
      start++;end--;
    }
  }

}

void reverse_word(char * str){
cout <<str<<endl;
  int end,start= strlen(str)-1;
  for(int i = start;i>=0;){
    while(str[i]==' ')--i;
    start = i;
    while(str[i]!=' ' && i>=0)--i;
    end = i+1;
    reverse(end,start,str);
    cout <<str<<endl;
    --i;

  }

}



int main(){
  char sentence[] = " ";
  cout<<sentence<<endl;
  reverse_word(sentence);
  for(int i = strlen(sentence)-1;i>=0;--i){
    cout<< sentence[i];
  }

  return 0;
}

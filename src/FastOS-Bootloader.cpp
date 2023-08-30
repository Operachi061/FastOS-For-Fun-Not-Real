#include <iostream>
#include <stdio.h>
#include <cstdlib>
#include <curses.h>

using namespace std;

char choice;

int main()
{
          cout <<"-----------------------------------------------------------------------------------------" << endl;
          cout <<"|                                                                                       |" << endl;
          cout <<"|           1. FastOS-Not-Real                                                          |" << endl;
          cout <<"|           2. Exit                                                                     |" << endl;
          cout <<"|                                                                                       |" << endl;
          cout <<"|                                                                                       |" << endl;
          cout <<"|                                                                                       |" << endl;
          cout <<"|                                                                                       |" << endl;
          cout <<"|                                                                                       |" << endl;
          cout <<"|        ^~^^~  .^^^^^   ^^^^^..~^7~^.:^     ^^^^^.   :!    !^^^^  .!^^^  !^^~:         |" << endl;
          cout <<"|        !~.^? .?.   ^7 7:   :?.  ?.  ^!    7:   :?. :!:7   ?   :? :?.:. .?..~7         |" << endl;
          cout <<"|        !~.^!~^7    .?.J     ?.  ?.  ^!   .J     ?.:?^:!7  ?    ? :?.:. .J^~?^         |" << endl;
          cout <<"|        !~::~^ !~:::!: ^!:::~^   ?.  ^7::^ ^!:::~^.7.   ^! ?::^~: :?::^..?   7:        |" << endl;
          cout <<"|         ...    .::.     .:.     .    ....   .:.         . ....    ..... .    .        |" << endl;
          cout <<"-----------------------------------------------------------------------------------------" << endl;

          choice = getchar();
          switch (choice)
          {
          case '1':
                  system("./FastOS-Shell");
          case '2':
                  exit(0);
          }
    return 0;
}

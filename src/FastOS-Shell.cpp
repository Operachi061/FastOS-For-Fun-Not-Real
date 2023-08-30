#include <iostream>
#include <stdio.h>

using namespace std;

int Turbo;
string commandline;
string computer;
string name;

int main()
{
   cout << "Your name: ";
   cin >> name;
   cout << "Computer name: ";
   cin >> computer;
    //Turbo - Package manager
    //Turbo-make-install
    //Turbo-make-delete
    //Turbo-make-sync

    //Command line and simple commands
while (true)
{
      cout << computer << "@" << name << ":";
      cin >> commandline;
       if (commandline == "turbo-make-help")
       {
          cout << "delete - remove/unistall package" << endl;
          cout << "install - install package" << endl;
          cout << "sync - sync/update packages" << endl;
       }
       else cout << "Error" << endl;
       if (commandline == "turbo-make-install")
       {
          cout << "delete - remove/unistall package" << endl;
       }
       else
       {
          cout << "Error" << endl;
       }
       if (commandline == commandline)
       {
         //cout << computer << "@" << name << ":";
         cin >> commandline;
       }
       if (commandline == "exit")
       {
         exit(0);
       } else cout << "Error" << endl;
}

  return 0;
}

//
//  main.cpp
//  Midtermq2
//
//  Created by Landon Dare on 10/20/16.
//  Copyright © 2016 Landon Dare. All rights reserved.
//

#include <iostream>
#include <fstream>
#include "sha1.h"

using namespace std;

void logWinner(string log,string input, string hash){
    cout << "############ WINNER FOUND ##############"<< endl;
    cout << "input string : \n" << input << endl;
    cout << "hash string : \n" << hash << endl;

    
    ofstream logFile;
    logFile.open (log);
    logFile.flush();
    logFile << "############ WINNER FOUND ##############"<< endl;
    logFile << "input string : \n" << input << endl;
    logFile << "hash string : \n" << hash << endl;
    logFile.close();

    
}

void sha1Trun(string logFile, string primer){
    string base = "DARE2095";
    SHA1 sha1;
    bool found = false;
    
    string input = base + primer;
    string hash = sha1(input);
    
    long counter = 0;
    
    while(!found){
        // check if a winner has been found
        if(counter % 10000000 == 0){
            cout << " counter at " << counter << endl;
        }
        if(hash.substr(0,2) == "0000"){
            //winner found
            logWinner(logFile, input, hash);
            found = true;
            
            
        }
        else{
            input = base + hash;
            hash = sha1(input);
        }
        counter++;
    }
    
    
}





int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    sha1Trun(argv[1], argv[2]);
    return 0;
}

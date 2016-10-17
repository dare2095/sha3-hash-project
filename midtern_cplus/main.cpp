//
//  main.cpp
//  midtern_cplus
//
//  Created by Landon Dare on 10/17/16.
//  Copyright © 2016 Landon Dare. All rights reserved.
//
// http://create.stephan-brumme.com/hash-library/


#include <iostream>
#include <fstream>
#include "sha3.h"

using namespace std;

struct Winner{
    int prefix =0;
    string str1 = "";
    string str1Hash = "";
    string str2 = "";
    string str2Hash = "";
    string logFile = "";
};

int findPrefixLength(string str1, string str2){
    int counter = 0;
    while(counter< str1.length() && str1[counter] == str2[counter]){
        counter++;
    }
    
    return counter;
}

void winnerFound(Winner win){
    cout << "############ NEW WINNER FOUND ##############"<< endl;
    cout << win.str1 << "  ==>  " << win.str1Hash << endl;
    cout << win.str2 << "  ==>  " << win.str2Hash << endl;
    cout << win.prefix << "  or  " << 4 * win.prefix << " bits " << endl;
    
    ofstream logFile;
    logFile.open (win.logFile);
    logFile.flush();
    logFile << "############ NEW WINNER FOUND ##############"<< endl;
    logFile << win.str1 << "  ==>  " << win.str1Hash << endl;
    logFile << win.str2 << "  ==>  " << win.str2Hash << endl;
    logFile << win.prefix << "  or  " << 4 * win.prefix << " bits " << endl;
    logFile.close();
    
}

void pollardRho(string logFile){
    string base = "112932095";
    string primer = "112932095abcdef";
    SHA3   sha3  (SHA3  ::Bits224);
    
    //tortoise
    string tortoise = primer;
    string tortoiseHash = sha3(primer);
    
    //hares
    string hare1 = base + tortoiseHash;
    string hare1Hash = sha3(hare1);
    string hare2 = base + hare1Hash;
    string hare2Hash = sha3(hare2);
    
    Winner win;
    win.logFile = logFile;
    int p1 = 0;
    int p2 = 0;
    
    //infinite execution loop
    while(true){
        //check for winner
        p1 = findPrefixLength(tortoiseHash, hare1Hash);
        p2 = findPrefixLength(tortoiseHash, hare2Hash);
        if(p1 > win.prefix && tortoise != hare1){
            win.prefix = p1;
            win.str1 = tortoise;
            win.str1Hash = tortoiseHash;
            win.str2 = hare1;
            win.str2Hash = hare1Hash;
            winnerFound(win);
        }else if (p2 > win.prefix && tortoise != hare2){
            win.prefix = p2;
            win.str1 = tortoise;
            win.str1Hash = tortoiseHash;
            win.str2 = hare2;
            win.str2Hash = hare2Hash;
            winnerFound(win);
        }
        
        //update hashes
        tortoise = base + tortoiseHash;
        tortoiseHash = sha3(tortoise);
        
        hare1 = base + hare1Hash;
        hare1Hash = sha3(hare1);
        
        hare2 = base + hare2Hash;
        hare2Hash = sha3(hare2);
        
    }
    
    
}

int main(int argc, const char * argv[]) {
    // insert code here...
    /*
    SHA3   sha3  (SHA3  ::Bits224);
    std::cout << "Hello, World!\n";
    std::string hashOutput = sha3("112932095");
    std::cout << sha3("112932095") << std::endl;
    std::cout << findPrefixLength(hashOutput, hashOutput) << std::endl;
    std::cout << findPrefixLength(hashOutput, hashOutput) << std::endl;
    
    //real deal test
    string test1 = "11293209579c9f9474249121fedd4cdbe72d9d8d65215fd2a2a0747ea075dc477";
    string test2 = "11293209578b1548eb362e5c04a3e07291343702afe1f49411670a5f98cbe8c59";
    string h1 = sha3(test1);
    string h2 = sha3(test2);
    
    cout << "should be 8 :" << findPrefixLength(h1, h2) << endl;
     */
    pollardRho(argv[1]);
    return 0;
}

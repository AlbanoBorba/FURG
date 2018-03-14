#include <bits/stdc++.h>
using namespace std;

char str[] = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<graphml xmlns=\"http://graphml.graphdrawing.org/xmlns\"\nxmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"\nxsi:schemaLocation=\"http://graphml.graphdrawing.org/xmlns\nhttp://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd\">";
int main(){
    ofstream myfile;
    myfile.open("test");
    myfile << str;
    myfile.close();
    return 0;
}

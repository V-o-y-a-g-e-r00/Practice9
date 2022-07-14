#include <iostream>
#include <string>
#include <iomanip>

#include "Funcs.h"

//#include <cpprest/http_client.h>

/*#include <mysql-cppconn-8/mysqlx/xdevapi.h>

using ::std::cout;
using ::std::endl;
using namespace ::mysqlx;
*/
int main(int argc, const char* argv[]){
/* 
    std::vector<std::pair<double, double>> vecRes;
    GetCoordByTag("РеспубликаКрым", vecRes, "TouristPlaces1");
    
    std::cout << std::fixed;
    std::cout << std::setprecision(8);
    for(std::pair<double, double> &entity: vecRes)
    {
        std::cout<<"lat="<<entity.first<<" long="<<entity.second<<std::endl;
    }
*/    
    entity Entity;
    GetEntity("3", Entity, "TouristPlaces1");
    Print(Entity);





    return 0;
} 
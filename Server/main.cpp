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
    std::vector<std::pair<double, double>> vecRes;
    GetCoordByTag("TouristPlaces1", "РеспубликаКрым", vecRes);
    
    std::cout << std::fixed;
    std::cout << std::setprecision(8);
    for(std::pair<double, double> &entity: vecRes)
    {
        std::cout<<"lat="<<entity.first<<" long="<<entity.second<<std::endl;
    }
    
    return 0;



/*    try
    {
        const char   *url = (argc > 1 ? argv[1] : "mysqlx://root:qwertyz@127.0.0.1");

        cout << "Creating session on " << url
            << " ..." << endl;

        Session sess(url);

        cout <<"Session accepted, creating collection..." <<endl;

        Schema sch= sess.getSchema("TouristPlaces1");
        Table tlPlaces = sch.getTable("Places", true);
        RowResult rres = tlPlaces.select("*").execute();
        std::string str=(std::string)rres.fetchOne().get(1);
        cout<<"str="<<str<<endl;


        cout <<"Done!" <<endl;
    }
    catch (const mysqlx::Error &err)
    {
        cout <<"ERROR: " <<err <<endl;
        return 1;
    }
    catch (std::exception &ex)
    {
        cout <<"STD EXCEPTION: " <<ex.what() <<endl;
        return 1;
    }
    catch (const char *ex)
    {
        cout <<"EXCEPTION: " <<ex <<endl;
        return 1;
    }
*/
} 
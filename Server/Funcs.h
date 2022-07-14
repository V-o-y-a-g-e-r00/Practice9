#ifndef FUNCS_H
#define FUNCS_H

#include <iostream>
#include <string>
#include <utility>
#include <vector>

#include <mysql-cppconn-8/mysqlx/xdevapi.h> //cpp Коннектор для mySQL

//Возрващает вектор пар координат всех точек в регионе
int GetCoordByTag(const std::string &DBName, const std::string &StrTag, std::vector<std::pair<double, double>> &Coord)
{
    using ::std::cout;
    using ::std::endl;
    using namespace ::mysqlx;
    try
    {
        std::string StrTegTemp=StrTag;
        StrTegTemp.insert(0, "\"");
        StrTegTemp.append("\"");

        const char* url = "mysqlx://root:qwertyz@127.0.0.1";

        cout << "Creating session on " << url << " ..." << endl;
        Session sess(url);
        cout <<"Session accepted, getting"<< DBName << "schema ..." <<endl;
        Schema sch= sess.getSchema(DBName);
        cout <<"Schema got, getting Places Table ..." <<endl;
        Table tlPlaces = sch.getTable("Places", true);
        cout <<"Places Table got, getting rows ..." <<endl;
        
        std::string strReq("Tag=");
        strReq.append(StrTegTemp);
        cout<<"strReq:"<<strReq<<endl;

        RowResult rres = tlPlaces.select("*").where(strReq).execute();
        
        for(Row row: rres)
        {
           // cout<<(double)row.get(4)<<endl;
            
            //cout<<"id:"<<row.get(0)<<"; name:"<<row.get(1)<<endl;;
            Coord.push_back(std::make_pair((double)row.get(4), (double)row.get(5)));
        }
        
        //std::string str=(std::string)rres.fetchOne().get(1);
        //cout<<"str="<<str<<endl;


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
    return 0;
}

#endif /* FUNCS_H */

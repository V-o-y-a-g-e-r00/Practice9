#include <iostream>
//#include <cpprest/http_client.h>

#include <mysql-cppconn-8/mysqlx/xdevapi.h>

using ::std::cout;
using ::std::endl;
using namespace ::mysqlx;

int main(int argc, const char* argv[]){
    std::cout << "Hello, world!\n";
    try
    {
        const char   *url = (argc > 1 ? argv[1] : "mysqlx://root@127.0.0.1");

        cout << "Creating session on " << url
            << " ..." << endl;

        Session sess(url);

        cout <<"Session accepted, creating collection..." <<endl;

        Schema sch= sess.getSchema("test");
        Collection coll= sch.createCollection("c1", true);

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

} 
#include <mysql-cppconn-8/mysqlx/xdevapi.h> //cpp Коннектор для mySQL
#define _TURN_OFF_PLATFORM_STRING
#include <cpprest/http_listener.h> 
#include <cpprest/base_uri.h>
#include <cpprest/json.h> 

using namespace web::http;                  // Common HTTP functionality
using namespace web::http::client;          // HTTP client features
using namespace concurrency::streams;       // Asynchronous streams
using namespace web::http::experimental::listener;
//#include <cpprest/http_client.h>

int main(int argc, const char* argv[]){
    http_listener listener("http://localhost:12345");
    
    int count = 0;

    listener.support([count] (http_request request) mutable
    {
        //std::cout << "GET "<< request.request_uri().to_string() << std::endl;


        // 
        auto http_get_vars = uri::split_query(request.request_uri().query());
        http_get_vars.at("param1");

        std::cout<< "http_get_vars.at(\"param1\")="<<http_get_vars.at("param1")<<std::endl;
        std::string str=web::uri::decode(http_get_vars.at("param1"));
        std::cout<< "str="<<str<<std::endl;
/*  

        // так анализируются параметры
        auto param_end = http_get_vars.find("end");
        if (param_end != end(http_get_vars)) {
            auto request_name = param_end->second;
            std::cout << "Received \"end\": " << request_name << std::endl;
        }

        auto param_start = http_get_vars.find(utility::conversions::to_string_t("start"));
        if (param_start != end(http_get_vars)) {
            auto request_name = param_start->second;
            std::cout << "Received \"start\": " << request_name << std::endl;
        }
*/      web::json::value jsonObj;
        jsonObj["latitude"]= web::json::value::number(10.203040);
        jsonObj["longitude"]= web::json::value::number(99.223344);

        web::json::value jsonarr;
        jsonarr[0]=jsonObj;
        jsonarr[1]=jsonObj;

        std::cout<<"jsonObj.serialize.c_str()=" <<jsonObj.serialize().c_str()<<std::endl;
        std::cout<<"jsonarr.serialize.c_str()=" <<jsonarr.serialize().c_str()<<std::endl;


        web::http::http_response response(200);
        response.headers().set_content_type(utility::conversions::to_string_t("application/json"));
        response.set_body(jsonarr);
        request.reply(response);




        //request.reply(status_codes::OK, jsonObj.serialize() ,utility::conversions::to_string_t("application/json"));
    }
    );

    listener.open().wait();
	std::cout << "Web server started on: " << listener.uri().to_string() << std::endl;

    getchar();

	std::cout << "Terminating JSON listener." << std::endl;
	listener.close().wait();
    return 0;
}   
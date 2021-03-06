#include <mysql-cppconn-8/mysqlx/xdevapi.h> //cpp Коннектор для mySQL
#define _TURN_OFF_PLATFORM_STRING
#include <cpprest/http_listener.h> 
#include <cpprest/base_uri.h>
#include <cpprest/json.h> 

#include "Funcs.h"

using namespace web::http;                  // Common HTTP functionality
using namespace web::http::client;          // HTTP client features
using namespace concurrency::streams;       // Asynchronous streams
using namespace web::http::experimental::listener;

int main(int argc, const char* argv[]){
    std::string DBName("TouristPlaces");
    http_listener listener("http://localhost:12345");

    listener.support([DBName] (http_request request) mutable
    {
        web::http::http_response response(200); //Формируемый ответ на запрос

        auto http_get_vars = uri::split_query(request.request_uri().query()); //map пары ключ значение
        switch (http_get_vars.size())
        {
            case 0: //Отправляем пользователю страницу
                
                break;
            case 1: //Отправляем пары координат всех точек в выбранном регионе
                {
                    std::cout<<"The number of param is" <<http_get_vars.size()<<" Sending pairs of coordinates of all places in region..."<<std::endl;

                    web::json::value jsonArr;
                    std::string StrTag=web::uri::decode(http_get_vars.at("tag")); //Строка с тегом, который мы получили в запросе в раскодированном виде

                    std::vector<PointEntity> Coord;
                    GetCoordByTag(StrTag, Coord, DBName);
                    for(int i=0; i<Coord.size(); i++)
                    {
                        web::json::value jsonObj;
                        jsonObj["id"]= web::json::value::number(Coord.at(i).id);
                        jsonObj["latitude"]= web::json::value::number(Coord.at(i).x);
                        jsonObj["longitude"]= web::json::value::number(Coord.at(i).y);
                        jsonArr[i]=jsonObj;
                    }
                    response.set_body(jsonArr);
                    response.headers().set_content_type(utility::conversions::to_string_t("application/json"));
                    std::cout<<"The data sent"<<std::endl;
                    break;
                }
            case 2: //Отправляем всю инормацию о выбранной точке
                {
                    web::json::value jsonObj;

                    std::string DBid=web::uri::decode(http_get_vars.at("id")); //Строка с id

                    entity Entity;
                    GetEntity(DBid, Entity, DBName);

                    jsonObj["id"]=web::json::value::number(Entity.id);
                    jsonObj["name"]=web::json::value::string(utility::conversions::to_string_t(Entity.name));
                    jsonObj["tag"]=web::json::value::string(utility::conversions::to_string_t(Entity.tag));
                    jsonObj["description"]=web::json::value::string(utility::conversions::to_string_t(Entity.description));
                    jsonObj["latitude"]= web::json::value::number(Entity.latitude);
                    jsonObj["longitude"]= web::json::value::number(Entity.longitude);
                    jsonObj["grouped_id"]= web::json::value::string(utility::conversions::to_string_t(Entity.grouped_id));


                    response.set_body(jsonObj);
                    response.headers().set_content_type(utility::conversions::to_string_t("application/json"));
                    break;
                }
            default:
                break;
        }
        request.reply(response);

        std::cout<< "http_get_vars.at(\"param1\")="<<http_get_vars.at("param1")<<std::endl;
        std::string str=web::uri::decode(http_get_vars.at("param1"));
        std::cout<< "str="<<str<<std::endl;

        std::cout<< "http_get_vars.size()="<<http_get_vars.size()<<std::endl;

    /*
        web::json::value jsonObj;
        jsonObj["id"]=web::json::value::number(101);
        jsonObj["latitude"]= web::json::value::number(10.203040);
        jsonObj["longitude"]= web::json::value::number(99.223344);


        std::cout<<"jsonObj.serialize.c_str()=" <<jsonObj.serialize().c_str()<<std::endl;
        std::cout<<"jsonarr.serialize.c_str()=" <<jsonarr.serialize().c_str()<<std::endl;
    */
    }
    );

    listener.open();
	std::cout << "Web server started on: " << listener.uri().to_string() << std::endl;

    getchar();

	std::cout << "Terminating JSON listener." << std::endl;
	listener.close();
    return 0;
}   
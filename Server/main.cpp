#include <cpprest/http_listener.h> 

using namespace web::http;                  // Common HTTP functionality
using namespace web::http::client;          // HTTP client features
using namespace concurrency::streams;       // Asynchronous streams
using namespace web::http::experimental::listener;
//#include <cpprest/http_client.h>

int main(int argc, const char* argv[]){
    http_listener listener("http://localhost:12345");
    
    int count = 0;

    listener.support(methods::GET, [count] (http_request request) mutable {
	std::cout << "GET "<< request.request_uri().to_string() << std::endl;





    });
    return 0;
}   
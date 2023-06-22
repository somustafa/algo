#include <iostream>
#include <string>

int main(){
    int n;
    std::cin >> n;
    std::string s;
    for (int i = 0; i < n; ++i){
        std::cin >> s;
        if (s.size() > 10){
            std::cout << s[0] << s.size() - 2 << s[s.size() - 1] << "\n";
        } else {
            std::cout << s << "\n";
        }
    }
}
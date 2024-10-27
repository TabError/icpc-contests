#include<bits/stdc++.h>
using namespace std;
namespace rr = ranges;

#define F(i, s, e) for(int i = (s); i < (e); i++)
#define R(i, n) F(i, 0, n)

typedef long long ll;
typedef pair<int, int> pii;
typedef double lf;
typedef complex<lf> cp;



void solve(){
    int f;
    vector<pair<pii, pii>> fences;
    cin >> f;
    R(i, f){
        int x, y, xx, yy;
        cin >> x >> y >> xx >> yy;
        fences.push_back({{x, y}, {xx, yy}});
    }

    set<pii> icorners;
    for(auto [a, b] : fences){
        icorners.insert(a);
        icorners.insert(b);
    }

    vector<cp> corners;
    for( auto [x, y] : icorners )
        corners.emplace_back(x, y);

    vector<int> used(size(corners), 2);



}



int main(){
    solve();
}



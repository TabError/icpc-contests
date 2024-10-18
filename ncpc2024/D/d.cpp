#include<bits/stdc++.h>
using namespace std;
const int INF = 1<<30;
// T, NEUTRAL and m() depend on f
typedef int T;
const T NEUTRAL = -INF;
T m(T l, T r){ return max(l, r); }
struct interval_tree {
  int N;
  vector<T> t;
  interval_tree(vector<T> &a)
    : N(bit_ceil(size(a) + 1)), t(2 * N, NEUTRAL){
    copy(begin(a), end(a), begin(t) + N - 1);
    for(int i = N - 2; i >= 0; i--)
      t[i] = m(t[lc(i)], t[rc(i)]);
  }
  T get(int l, int r){
    l += N - 1, r += N - 1;
    T res = NEUTRAL;
    while(l <= r && (l != 0 || r != 0)){
      if(l % 2 == 0) res = m(res, t[l++]);
      if(r % 2 == 1) res = m(res, t[r--]);
      l = pa(l), r = pa(r);
    }
    return res;
  }
  void set(int p, T val){
    p += N - 1, t[p] = val;
    while(p > 0) // <=> while p != pa(p)
      p = pa(p), t[p] = m(t[lc(p)], t[rc(p)]);
  }
  int pa(int x){ return (x - 1) / 2; }
  int lc(int x){ return 2 * x + 1; }
  int rc(int x){ return 2 * x + 2; }
};
#define R(i, N) for(int i=0;i<(N);i++)
int N, K;
map<int,vector<int>> d;
int main(){
    cin>>N>>K;
    vector<int> a(N * K),b(N * K);
    R(i,N*K)cin >> a[i];
    R(i,N*K)cin >> b[i];
    R(i,N) d[i+1] = vector<int>();
    R(i,N*K) d[b[i]].push_back(i+1);

    vector<int> matches(N*K+8,-INF);
    matches[0] = 0;
    auto it = interval_tree(matches);

    for(auto card: a)
    for(auto pos: ranges::views::reverse(d[card]))
    it.set(pos,it.get(0, pos-1) + 1);
    cout<<it.get(0,N*K)<<endl;
}


# Rabin Karp + Polynomial rolling hash

## Method 1 - Sliding hash with inverse

``` cpp
#include <bits/stdc++.h>
#define int long long int
using namespace std;
const int mod = 1e9+7;
const int p = 31;

int powr(int a, int b){
    int res = 1;
    while(b){
        if (b & 1ll){
            res *= a;
            res %= mod;
        }
        b /= 2;
        a *= a;
        a %= mod;
    }
    return res;
}

int inv(int a){
    return powr(a, mod-2);
}

int polyHashString(string s){
    int p_power = 1;
    int hash = 0;
    for (int i=0; i<s.size(); i++){
        hash += (p_power * (s[i]-'a' + 1));
        p_power *= p;
        p_power %= mod;
        hash %= mod;
    }
    return hash;
}

int32_t main()
{
    string s= "ababab";
    string pat = "aba";
    int patHash = polyHashString(pat);
    int n = s.size();
    int m = pat.size();
    int txthash = polyHashString(s.substr(0,m));
    
    if (txthash == patHash) {
        cout<<'0'<<endl;
    }
    
    for (int i=1; i + m <= n; i++){
        int newhash = txthash;
        // remove the (i-1)th char
        newhash = (newhash - (s[i-1]-'a'+1) + mod) % mod;
        
        // second step 
        newhash *= inv(p);
        newhash %= mod;
        
        // third step
        newhash = (newhash + (s[i+m-1]-'a'+1) * powr(p, m-1));
        newhash %= mod;
        
        if (newhash == patHash){
            cout<<i<<endl;
        }
        txthash = newhash;
        
    }

    return 0;
}
```

## Method 2 - prefix hash comparison

``` cpp
#include <bits/stdc++.h>
#define int long long int
using namespace std;
const int mod = 1e9+7;
const int p = 31;

int powr(int a, int b){
    int res = 1;
    while(b){
        if (b & 1ll){
            res *= a;
            res %= mod;
        }
        b /= 2;
        a *= a;
        a %= mod;
    }
    return res;
}

int inv(int a){
    return powr(a, mod-2);
}

int polyHashString(string s){
    int p_power = 1;
    int hash = 0;
    for (int i=0; i<s.size(); i++){
        hash += (p_power * (s[i]-'a' + 1));
        p_power *= p;
        p_power %= mod;
        hash %= mod;
    }
    return hash;
}

int32_t main()
{
    string s= "abaabab";
    string pat = "aba";
    int patHash = polyHashString(pat);
    int n = s.size();
    int m = pat.size();
    
    int pref[n];
    
    for (int i=0; i<n; i++){
        pref[i] = (s[i]-'a'+1) * powr(p,i);
        pref[i] %= mod;
    }
    
    for (int i=1; i<n; i++){
        pref[i] += pref[i-1];
        pref[i] %= mod;
    }
    
    for (int i=0; i+m <= n; i++){
        int newhash = pref[i+m-1];
        if (i-1 >= 0){
            newhash -= pref[i-1];
        }
        newhash += mod;
        newhash %= mod;
        if (newhash == (patHash * powr(p,i)) % mod){
            cout<<i<<endl;
        }
        
    }
    

    return 0;
}
```

[!Note]

- Method 2 is faster and safer
- In Method 1, modular inverse is expensive

## Double Hashing

``` cpp
#include <bits/stdc++.h>
#define int long long
using namespace std;

const int p = 31;
const int mod1 = 1000000007;
const int mod2 = 1000000009;

int32_t main() {
    string s = "abaabab";
    string pat = "aba";

    int n = s.size();
    int m = pat.size();

    vector<int> power1(n+1), power2(n+1);
    vector<int> pref1(n), pref2(n);

    // Precompute powers
    power1[0] = power2[0] = 1;
    for (int i = 1; i <= n; i++) {
        power1[i] = (power1[i-1] * p) % mod1;
        power2[i] = (power2[i-1] * p) % mod2;
    }

    // Prefix hashes for string s
    for (int i = 0; i < n; i++) {
        int val = (s[i] - 'a' + 1);

        pref1[i] = (val * power1[i]) % mod1;
        pref2[i] = (val * power2[i]) % mod2;

        if (i > 0) {
            pref1[i] = (pref1[i] + pref1[i-1]) % mod1;
            pref2[i] = (pref2[i] + pref2[i-1]) % mod2;
        }
    }

    // Pattern hash
    int patHash1 = 0, patHash2 = 0;
    for (int i = 0; i < m; i++) {
        int val = (pat[i] - 'a' + 1);
        patHash1 = (patHash1 + val * power1[i]) % mod1;
        patHash2 = (patHash2 + val * power2[i]) % mod2;
    }

    // Find matches
    for (int i = 0; i + m <= n; i++) {
        int curHash1 = pref1[i + m - 1];
        int curHash2 = pref2[i + m - 1];

        if (i > 0) {
            curHash1 = (curHash1 - pref1[i - 1] + mod1) % mod1;
            curHash2 = (curHash2 - pref2[i - 1] + mod2) % mod2;
        }

        // Align hashes
        if (curHash1 == (patHash1 * power1[i]) % mod1 &&
            curHash2 == (patHash2 * power2[i]) % mod2) {
            cout << i << endl;
        }
    }

    return 0;
}

```


/* Idea: Expand from center for as much as possible
 *		 We have 2n-1 centers to expand from
 */
#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string longestPalindrome(string s) {
        string res = "";
        for (int i = 0; i < s.size(); ++i) {
            int l1 = expandPal(s, i, i, -1);
            int l2 = expandPal(s, i-1, i, 0);
            if (res.size() < l1) res = s.substr(i - l1 / 2, l1);
            if (res.size() < l2) res = s.substr(i - l2 / 2, l2);
        }
        return res;
    }
    int expandPal(const string &s, int left, int right, int len) {
        while (left != -1 && right != s.size() && s[left--] == s[right++]) len += 2;
        return len;
    }
};

int main(int argc, char const *argv[])
{
	/* code */
	Solution s;
	cout << s.longestPalindrome("abbc") << endl;
	return 0;
}

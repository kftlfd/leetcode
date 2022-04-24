"""
Leetcode
535. Encode and Decode TinyURL (medium)
2022-04-24

"""

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))



# https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/1110529/Python-Use-two-dictionaries-explained
class Codec:
    def __init__(self):
        self.long_short = {}
        self.short_long = {}
        self.alphabet = "abcdefghijklmnopqrstuvwzyz"

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        while longUrl not in self.long_short:
            code = "".join(choices(self.alphabet, k=6))
            if code not in self.short_long:
                self.short_long[code] = longUrl
                self.long_short[longUrl] = code
        return 'http://tinyurl.com/' + self.long_short[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.short_long[shortUrl[-6:]]
        


# s = Solution()
# tests = []
# for t in tests:
#     print(t)
#     print()
#     print()

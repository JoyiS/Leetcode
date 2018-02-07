'''
1. How the system should be used ?
    full web app or API?
    Feature and Use cases?
    1) url shortening
    2) short url redirecting
    3) custom url
2. Constraints based on webhost big data analytics and predictions
    amount of traffic of the web services
    amount of data to handle in the database
    Query per second QPS
    Query per month QPM
3. Abstract Design and Data Models
    main entity:
    Name: ShortLink
        : a mapping between slug<short_Link> and destination<long_Link>
    code sketching: sprinting to a naive first draft design
'''

class Solution():

    def shortlink(request):
        if request['method'] is not 'POST':
            return Response(501)  # HTTP 501 NOT IMPLEMENTED

        destination = request['data']['destination']

        # if they included a slug, use that
        if 'slug' in request['data']:
            slug = request['data']['slug']

        # else, make them one
        else:
            slug = generate_random_slug()

        DB.insert({'slug': slug, 'destination': destination})

        response_body = {
            'slug': slug,
        }

        return Response(200, json.dumps(response_body))  # HTTP 200 OK

    def redirect(request):
        destination = DB.get({'slug': request['path']})['destination']
        return Response(302, destination)


'''
slug generation:
1. How many slugs do we need?
2. ballpark estimate?
QPS :
QPM : 1BN
'''
    import random
    def generate_random_slug():
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        num_chars = 7
        return ''.join([random.choice(alphabet) for _ in xrange(num_chars)])

    # Using base conversion to generate slugs


    def generate_random_slug():
        global current_random_slug_id
        slug = base_conversion(current_random_slug_id, base_62_alphabet)
        current_random_slug_id += 1
        return slug


    def generate_random_slug():
        global current_random_slug_id
        while True:
            slug = base_conversion(current_random_slug_id, base_62_alphabet)
            current_random_slug_id += 1

            # make sure the slug isn't already used
            existing = DB.get({'slug': slug})
            if not existing:
                return slug  # !/usr/bin/env python


class Codec:
    import string
    letters = string.ascii_letters + string.digits
    full_tiny = {}
    tiny_full = {}
    global_counter = 0

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """

        def decto62(dec):
            ans = ""
            while 1:
                ans = self.letters[dec % 62] + ans
                dec //= 62
                if not dec:
                    break
            return ans

        suffix = decto62(self.global_counter)
        if longUrl not in self.full_tiny:
            self.full_tiny[longUrl] = suffix
            self.tiny_full[suffix] = longUrl
            self.global_counter += 1
        return "http://tinyurl.com/" + suffix

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        idx = shortUrl.split('/')[-1]
        if idx in self.tiny_full:
            return self.tiny_full[idx]
        else:
            return None
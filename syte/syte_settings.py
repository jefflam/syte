
DEPLOYMENT_MODE = 'prod'
COMPRESS_REVISION_NUMBER = '1.0'

#Blog Integration: Tumblr
TUMBLR_BLOG_URL = 'jefflam.tumblr.com'
TUMBLR_API_URL = 'http://api.tumblr.com/v2/blog/{0}'.format(TUMBLR_BLOG_URL)
TUMBLR_API_KEY = '2ZyHUYJdmPPoO1vrj8yyGUkTPVg6gPOK2cfy4kJJ6cTjOTmBaT'

#RSS Feed Integration: (by default use Tumbrl rss feed)
RSS_FEED_ENABLED = True
RSS_FEED_URL = 'http://{0}/rss'.format(TUMBLR_BLOG_URL)

#Twitter Integration
TWITTER_INTEGRATION_ENABLED = True
TWITTER_API_URL = 'http://api.twitter.com/1/statuses/user_timeline.json?include_rts=false&exclude_replies=true&count=50&screen_name='
TWITTER_CONSUMER_KEY = 'gurkcjZbPUnefeG9bZ0hMA'
TWITTER_CONSUMER_SECRET = 'rl0C4TLuxkp67Mj3JYZMfY7HJDftSSvSoReuHJ8aZI'
TWITTER_USER_KEY = '58200902-AFhpnlJYV3WKQMb6a9ozFbebYe6SAD5K3XOjyYKyZ'
TWITTER_USER_SECRET = 'ud3vjZWoHwEdwUd4kFRm9czVe9eYig9lf5jthLFdk'


#Github Integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_API_URL = 'https://api.github.com/'
GITHUB_ACCESS_TOKEN = '[ENTER GITHUB ACCESS TOKEN HERE, SEE GITHUB SETUP INSTRUCTIONS]'

GITHUB_OAUTH_ENABLED = True
GITHUB_CLIENT_ID = '[ENTER GITHUB CLIENT ID HERE, SEE GITHUB SETUP INSTRUCTIONS]'
GITHUB_CLIENT_SECRET = '[ENTER GITHUB CLIENT SECRET HERE, SEE GITHUB SETUP INSTRUCTIONS]'
GITHUB_OAUTH_AUTHORIZE_URL = 'https://github.com/login/oauth/authorize'
GITHUB_OAUTH_ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'


#Dribbble Integration
DRIBBBLE_INTEGRATION_ENABLED = True
DRIBBBLE_API_URL = 'http://api.dribbble.com/players/'


#Instagram Integration
INSTAGRAM_INTEGRATION_ENABLED = True
INSTAGRAM_API_URL = 'https://api.instagram.com/v1/'
INSTAGRAM_ACCESS_TOKEN = '3766630.be4d75a.73bc91e265d6472887106e0ff8d67bc1'
INSTAGRAM_USER_ID = '3766630'

INSTAGRAM_OAUTH_ENABLED = False
INSTAGRAM_CLIENT_ID = 'be4d75a2420345ac859738ad3cb9f17a'
INSTAGRAM_CLIENT_SECRET = '7f50e98ed15a4df8aa4c3108fcdcdb4d'
INSTAGRAM_OAUTH_AUTHORIZE_URL = 'https://api.instagram.com/oauth/authorize'
INSTAGRAM_OAUTH_ACCESS_TOKEN_URL = 'https://api.instagram.com/oauth/access_token'


#Google Analytics
GOOGLE_ANALYTICS_TRACKING_ID = ''


#Disqus Integration
DISQUS_INTEGRATION_ENABLED = True
DISQUS_SHORTNAME = 'jefflamth'



if DEPLOYMENT_MODE == 'dev':
    SITE_ROOT_URI = 'http://127.0.0.1:8000/'
    DEBUG = True
else:
    DEBUG = False
    SITE_ROOT_URI = 'http://jefflamth.herokuapp.com/'

MEDIA_URL = SITE_ROOT_URI + 'static/'

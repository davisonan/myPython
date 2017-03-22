## Use_YouTube_API.py

import gdata.youtube
import gdata.youtube.service

yt_service = gdata.youtube.service.YouTubeService()

# Turn on HTTPS/SSL access.
# Note: SSL is not available at this time for uploads.
yt_service.ssl = True

def GetAuthSubUrl():
	next = 'http://www.example.com/video_upload.pyc'
	scope = 'http://gdata.youtube.com'
	secure = False
	session = True

yt_service = gdata.youtube.service.YouTubeService()
return yt_service.GenerateAuthSubURL(next, scope, secure, session)

authSubUrl = GetAuthSubUrl()
print '<a href="%s">Login to your Google account</a>' % authSubUrl


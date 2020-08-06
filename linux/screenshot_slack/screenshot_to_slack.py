import sys
from slack import WebClient
from slack.errors import SlackApiError


## Parameters ##
API_TOKEN=''
CHANNEL_NAME=''

client = WebClient(token=API_TOKEN)

try:
    filepath=sys.argv[1]
    response = client.files_upload(
        channels=CHANNEL_NAME,
        file=filepath)
    assert response["file"]  # the uploaded file
except SlackApiError as e:
    # You will get a SlackApiError if "ok" is False
    assert e.response["ok"] is False
    assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
    print(f"Got an error: {e.response['error']}")

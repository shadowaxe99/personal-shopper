```python
import json
import requests

# DOM Element ID
socialShareButton = "socialShareButton"

# Message Name
socialShareMessage = "socialShareMessage"

def shareOnSocialMedia(userProfileData, productData):
    """
    Function to share on social media.
    """
    # Extract user's social media details from the profile data
    socialMediaDetails = userProfileData.get('socialMediaDetails', {})

    # Prepare the message to be shared
    message = {
        "message": socialShareMessage,
        "product": productData
    }

    # Share on each social media platform
    for platform, details in socialMediaDetails.items():
        if platform == "facebook":
            shareOnFacebook(details, message)
        elif platform == "twitter":
            shareOnTwitter(details, message)
        elif platform == "instagram":
            shareOnInstagram(details, message)

def shareOnFacebook(details, message):
    """
    Function to share on Facebook.
    """
    url = "https://graph.facebook.com/v2.6/me/messages?access_token={}".format(details['accessToken'])
    headers = {'Content-Type': 'application/json'}
    data = {
        "recipient": {
            "id": details['id']
        },
        "message": message
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.status_code

def shareOnTwitter(details, message):
    """
    Function to share on Twitter.
    """
    url = "https://api.twitter.com/1.1/statuses/update.json?status={}".format(message)
    headers = {'Authorization': 'Bearer {}'.format(details['accessToken'])}
    response = requests.post(url, headers=headers)
    return response.status_code

def shareOnInstagram(details, message):
    """
    Function to share on Instagram.
    """
    url = "https://graph.instagram.com/{}/media?image_url={}&caption={}&access_token={}".format(details['id'], message['product']['imageUrl'], message['message'], details['accessToken'])
    response = requests.post(url)
    return response.status_code
```
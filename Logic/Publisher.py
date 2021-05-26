import requests

class Publisher:
    def __init__(self):
        pass

    def postProfText(self,profile_id,access_token,message):
        #profile_id = 'profile_id'

        #scope: w_member_social,r_liteprofile
        #access_token = 'access_token'

        url = "https://api.linkedin.com/v2/ugcPosts"

        headers = {'Content-Type': 'application/json',
                   'X-Restli-Protocol-Version': '2.0.0',
                   'Authorization': 'Bearer ' + access_token}

        post_data = {
            "author": "urn:li:person:"+profile_id,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": message
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }

        response = requests.post(url, headers=headers, json=post_data)

        return response

    def postOrgText(self,organization_id,access_token,message):
        organization_id = 'organization_id'

        #scope: w_member_social,r_liteprofile,w_organization_social
        access_token = 'access_token'

        url = "https://api.linkedin.com/v2/ugcPosts"

        headers = {'Content-Type': 'application/json',
                   'X-Restli-Protocol-Version': '2.0.0',
                   'Authorization': 'Bearer ' + access_token}


        post_data = {
            "author": "urn:li:organization:"+organization_id,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {
                        "text": message
                    },
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {
                "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
            }
        }

        response = requests.post(url, headers=headers, json=post_data)

        return response
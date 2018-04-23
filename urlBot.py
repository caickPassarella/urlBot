import praw
import win_unicode_console
import giphypop
import GrabzIt
import requests

win_unicode_console.enable()

import grabzItClient

grabzIt = grabzItClient.GrabzItClient("MGQxNzQ0Y2E1ZjIyNGRiNzk3NmFhYTY0Y2M1NzE3ZDg=",
                                      "Pz8/P0M/P2U/Tj8/cz8/ND9dP3Q/JwQ/PykffzI/Uxs=")


def downloadfile(name, url):
    name = name + ".mp4"
    r = requests.get(url)
    print("****Connected****")
    f = open(name, 'wb')
    print("Donloading.....")
    for chunk in r.iter_content(chunk_size=255):
        if chunk:  # filter out keep-alive new chunks
            f.write(chunk)
    print("Done")
    f.close()


def authenticate():
    print('Authenticating...\n')
    redditBot = praw.Reddit(user_agent='veganBot v1.0',
                            client_id="Qp8x9ezydpD64w",
                            client_secret="GTe4JmTN7gsilAanfevx92ItlyA",
                            username='veganBot-',
                            password='recipesAreLife')
    print('Authenticated as {}\n'.format(redditBot.user.me()))
    return redditBot


# The file to store the comments IDs, so we don't have duplicates
commentID_path = 'commentID.txt'


def get_url(redditBot):
    for submission in redditBot.subreddit('videos').new():
        url = submission.url

        if 'youtube' in url:
            youtube_link = url
            downloadfile('youtube', youtube_link)

            # gif_youtube = giphypop.upload(['bot', 'gifBot'], link)
            print('This is a YouTube link: {}'.format(youtube_link))

        elif 'https://clips.twitch.tv' in url:
            twitch_link = url
            try:
                downloadfile('twitch', twitch_link)

            except:
                print('error')
            # gif_twitch = giphypop.upload(['bot', 'gifBot'], twitch_link)
            print('This is a twitch link: {}'.format(twitch_link))

        elif 'https://twitter.com' in url:
            twitter_link = url
            try:
                downloadfile('twitter', twitter_link)

            except:
                print('error')
            # gif_twitter = giphypop.upload(['bot', 'gifBot'], twitter_link)
            print('This is a Twitter link: {}'.format(twitter_link))


def main():
    redditBot = authenticate()
    while True:
        get_url(redditBot)


if __name__ == '__main__':
    main()

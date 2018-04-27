import praw
import win_unicode_console
import requests
import random
from math import inf

win_unicode_console.enable()


def downloadfile(name, url):

    try:
        name = name + str(random.randint(1, 100))
        r = requests.get(url)
        print("****Connected****")
        f = open(name + '.jpg', 'wb')
        print("Donloading.....")
        for chunk in r.iter_content(chunk_size=1):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
        print("Done")
        f.close()

    except Exception as error:
        print(error)

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
    for submission in redditBot.subreddit('memes').hot():
        url_image = submission.url

        downloadfile('image', url_image)

        # gif_youtube = giphypop.upload(['bot', 'gifBot'], link)
        print('Done downloading: {}'.format(url_image))


def main():
    redditBot = authenticate()
    while True:
        get_url(redditBot)


if __name__ == '__main__':
    main()

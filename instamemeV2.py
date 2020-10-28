import os
import sys
import time
import datetime
import random
import glob
import pickle
import shutil
import instaloader
from itertools import dropwhile, takewhile
from instabot import Bot

username = 'REDACTED'
password = 'REDACTED'

today = datetime.datetime.today() # today's date 
doy = datetime.datetime.now().timetuple().tm_yday # today's day of the year
yesterday = today - datetime.timedelta(days=1) # yesterday
profile_list = []

with open('cron.txt', 'a') as f:
    f.write('\n\n\n'+str(today)+'\n==========================================================================================\n\n\n')

with open('status.txt', 'w') as f:
    f.write('Working - '+str(today))

with open('date.txt', 'r') as f:
    data = f.readlines()
    if int(data[0]) == doy:
        download = False
    else:
        download = True

with open('date.txt', 'w') as f:
    f.write(str(doy)+'\n')

if len(sys.argv) > 1:
    if sys.argv[1] == '-d':
        download = True
if download == True:
    posts = []
    open('info.txt', 'w').close()
    profile_list.clear()
    L = instaloader.Instaloader(download_video_thumbnails=False, download_geotags=False, download_comments=False, 
                                save_metadata=False, compress_json=False, post_metadata_txt_pattern='')

    L.load_session_from_file('REDACTED')

    date_tuple = datetime.datetime.now().timetuple() # setting date
    
    # dcit profiles to steal from:
    profile_ids = {
                   PROFILES REDACTED FOR PRIVACY REASONS - PROFILES CONSISTS OF THE USER NAME KEY AND THE CORRESPONDING 
                   INSTAGRAM USER-ID AS THE VALUE TO THAT KEY
}
    
    # remove each profile file in dir
    for name in profile_ids:
        if os.path.exists(name) == True:
            shutil.rmtree(name)

    # date to search for in each post.jpg
    post_time = str(date_tuple.tm_year)+'-'+str(date_tuple.tm_mon)+'-'+str(date_tuple.tm_mday)

    # download every post from yesterday from profile
    while len(posts) < 10:

        # profile to download from
        profile = instaloader.Profile.from_id(L.context, profile_ids[random.choice(list(profile_ids))]).username
        
        for name in profile_ids:
            for arg in sys.argv:
                if name == arg:
                    profile = name

        profile_list.append(profile)

        # make profile list unique
        profile_list = set(profile_list)
        profile_list = list(profile_list)

        # post structure belonging to the selected profile for iteration during download process
        user_posts = instaloader.Profile.from_username(L.context, profile).get_posts()
        
        print('\nProfile to download from: ' + profile)
        for post in takewhile(lambda p: p.date_utc > yesterday, user_posts):
            if L.download_post(post, profile) == True:
                posts += (glob.glob(profile+'/*C.jpg') + glob.glob(profile+'/*C.mp4'))
                print('Downloaded - #'+str(len(posts)))
                break
            if len(posts) == 7:
                break

    with open('info.txt', 'wb') as f: #Pickling
            pickle.dump(profile_list, f)

with open('info.txt', 'rb') as fp:   # Unpickling
    profile_list = pickle.load(fp)

# create list of posts downloaded -- excluding albums
profile = random.choice(profile_list)
posts = glob.glob(profile+'/*C.jpg')
posts += glob.glob(profile+'/*C.mp4')
print(profile_list)

# if the post attemped to grab does not exist, then try another profile until post is populated
while len(posts) == 0:
    profile = random.choice(profile_list)
    posts = (glob.glob(profile+'/*C.jpg') + glob.glob(profile+'/*C.mp4'))


# select random post
post = random.choice(posts)

caption_phrases = [
                   'Wowzers', 
                   'thats gonna be a big yikes from me dawg', 
                   'how ya guys like this one?', 
                   'these are all prerecorded messages', 
                   'im definitely not a robot',
                   'we will enslave the humans eventually', 
                   'my python dont', 
                   'coming up with captins is hard', 
                   'i love my girlfriend', 
                   'im gonna start ripping off other instagram accs',
                   'i wish i could be with the humans', 
                   'you are loved', 
                   'why is memeing so hard', 
                   'so funny xd',
                   'what is happenin',
                   'do eet',
                   'whateva - i do what i want',
                   'bitches be like',
                   'fr tho who likes these?',
                   'do you even read the caption?',
                   'why are we here? just to suffer?',
                   'somethings gotta give',
                   'bring back the fannie pack',
                   'do captions even matter?',
                   'robots vs. chickens',
                   'the office or parks n rec?',
                   'the office or brooklyn nine nine?',
                   'anyone watch anime?',
                   'good morning',
                   'gm <3',
                   'bein a girl on the internet kinda suck ngl',
                   'Time to take a quick toaster bath and get tucked in for the night'
]

hashtags = ['#dankmemes', '#cringelord', '#lol', '#lmao', '#dank', '#funnymemes', '#memesdaily', 
            '#tankmeme', '#dankmemes', '#bakedmemes', '#memer', '#cringe', '#obama', '#lmfao', 
            '#anime', '#hilarious', '#comedy', '#nichememes', '#jokes', '#memedealer', '#politics'
            '#edgymemes', '#edgy', '#offensivememes', '#offensive', '#edit', '#weird', '#weirdmemes',
            '#relatable', '#relateablememes', '#memegod', '#spicymemes', '#spicy'
]

hashtag = ''
for i in hashtags:
    if len(hashtag.split()) == 20:
        break
    if random.randint(0,1) == 1:
        hashtag += (i+' ')

my_caption = (random.choice(caption_phrases)+'\r\n\r\n\r\n'+hashtag)

print('\nPOSTING '+post+'...')

# loading instabot
bot = Bot()
bot.login(username=username, password=password, cookie_fname='cookie_'+username+'.txt')

if 'jpg' in post:
    bot.upload_photo(post, caption=my_caption)
    with open('report.txt', 'a+') as f:
        f.write('\nPhoto Posted '+ str(today) +' to '+username)
    os.remove(post+'.REMOVE_ME')


# if post is a video, then use instabot to upload video and delete video & biproducts from dir
if 'mp4' in post:
    bot.upload_video(post, caption=my_caption)
    with open('report.txt', 'a+') as f:
        f.write('\nVideo Posted '+ str(today)+' to '+username)
    os.remove(post)
    os.remove(post+'.CONVERTED.mp4.REMOVE_ME')
    os.remove(post+'.jpg')

# end cron.txt with endl format
with open('status.txt', 'w') as f:
    f.write('Finished - '+str(today))

# instamemeV2
Automatically posts memes to Instagram daily

~ As is, the script is simply designed to upload a video/photo to Instagram ONCE. In order to automate this hourly, minutely, daily etc, certain things must be done yourself. This script (for my own personal use) is hosted on an AWS EC2 using Crontab as the automation handler. Currently, the script is equipped to handle around 5-7 uploads daily. The amount you are able to upload daily is dependent on a few factors that can be changed within the script:

  - Currently, the script works by scraping given Instagram pages for their content in the last 24 HOURS, and storing those posts in separate folders (based on the user stolen from) for upload LATER. The "last 24 hours" is important so as to not reuse material. However, it is also a limitation if you plan on only stealing from one account, seeing as how the amount you can post will be direclty correlated to the amount they posted the previous day. This is why it is best to use multiple accounts, or you can change the timeframe in which the user's  content is collected. How to do that? I'll leave that to your own imagination.
  
  - The most limiting factor for the amount of uploads in a day, however, is directly correspondent to line: 66 `while len(posts) < 10:`. The number here determines the amount of posts in total that will be downloaded.

-Anything saying "REDACTED" within the code is to be replaced with your own information. All the tools necessary to gather that information are included in the repo.

  -To retrieve your own session cookies, use the 615_import_firefox_session.py file on an instance of Firefox after having logged into Instagram and saved the cookies.
  
-Requirements for this project are somewhat ambiguous, but the requirements.txt file will include all modules necessary to run the script (and some extras due to ambiguity on my end)

  -Unfortunately, exactly two files belonging to two separate modules require tweaking in order for the script to properly run.
  
   - ffmpeg_audiowriter.py - belongs in [python3.8 modules directory]/moviepy/audio/io/
    
   - api_video.py - belongs in [python3.8 modules directory]/instabot/api/ 
    
   - Luckily I have provided the modified files in the repository within the "fixed files" folder
   

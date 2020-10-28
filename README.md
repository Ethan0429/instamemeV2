# instamemeV2
Automatically posts memes to Instagram daily

-Anything saying "REDACTED" within the code is to be replaced with your own information. All the tools necessary to gather that information are included in the repo.
  -To retrieve your own session cookies, use the 615_import_firefox_session.py file on an instance of Firefox after having logged into Instagram and saved the cookies.
-Requirements for this project are somewhat ambiguous, but the requirements.txt file will include all modules necessary to run the script (and some extras due to ambiguity on my end)
  -Unfortunately, exactly two files belonging to two separate modules require tweaking in order for the script to properly run.
    -ffmpeg_audiowriter.py - belongs in [python3.8 modules directory]/moviepy/audio/io/
    -api_video.py - belongs in [python3.8 modules directory]/instabot/api/ 
    -Luckily I have provided the modified files in the repository within the "fixed files" folder
   

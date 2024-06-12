    # wishMe()
    # while True:
    # # if 1:
    #     query = takeCommand().lower()

    #     # Logic for executing tasks based on query
    #     if 'wikipedia' in query:
    #         speak('Searching Wikipedia...')
    #         query = query.replace("wikipedia", "")
    #         results = wikipedia.summary(query, sentences=2)
    #         speak("According to Wikipedia")
    #         print(results)
    #         speak(results)

    #     elif 'open youtube' in query:
    #         webbrowser.open("youtube.com")

    #     elif 'open google' in query:
    #         webbrowser.open("google.com")

    #     elif 'open stackoverflow' in query:
    #         webbrowser.open("stackoverflow.com")   


    #     elif 'play music' in query:
    #         music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
    #         songs = os.listdir(music_dir)
    #         print(songs)    
    #         os.startfile(os.path.join(music_dir, songs[0]))

    #     elif 'the time' in query:
    #         strTime = datetime.datetime.now().strftime("%H:%M:%S")    
    #         speak(f"Sir, the time is {strTime}")

    #     elif 'open code' in query:
    #         codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    #         os.startfile(codePath)

    #     elif 'email to harry' in query:
    #         try:
    #             speak("What should I say?")
    #             content = takeCommand()
    #             to = "harryyourEmail@gmail.com"    
    #             sendEmail(to, content)
    #             speak("Email has been sent!")
    #         except Exception as e:
    #             print(e)
    #             speak("Sorry my friend harry bhai. I am not able to send this email")
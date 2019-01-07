### Note ###
The WebExtension, which can be found under "add-on", connects to the native application and downloads the video using youtube-dl

The native application, which can be found under "app", listens for messages from the WebExtension. When it receives a message, the native application runs youtube-dl in the Downloads folder for the passed url from the WebExtension.

*** Look in your Downloads folder to find your video. ***

### Mac OS/Linux Setup ###
To get this working do the following:

1. Check that the [file permissions](https://en.wikipedia.org/wiki/File_system_permissions) for "youtube-dl-bridge.py" include the `execute` permission.
2. Edit the "path" property of "web_video_dl.json" to point to the location of "youtube-dl-bridge.py" on your computer.
3. copy "web_video_dl.json" to the correct location on your computer. See [App manifest location ](https://developer.mozilla.org/en-US/Add-ons/WebExtensions/Native_manifests#Manifest_location) to find the correct location for your OS.
4. Install the webextension and enjoy!

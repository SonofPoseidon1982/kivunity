This is a very new project simply knocked up to demonstrate a problem I am experiencing in integrating Unity ADS with pygame. It currently works with Kivy but leads to black screen death with Pygame.
Copy KivUnity.Py into the source folder. Follow UnityADS integration instructions (for integrating without Android Studio including adding AAR file to /libs directory and changing the android manifest file)
Import Kivunity
Instantiate the class Unity_handler early on; unity_ads = kivunity.Unity_handler(app_id)
Early on, initialize Unity ads; unity_ads.init_unity()
When ready to show the ad; unity_ads.show_ad(inter_id) 

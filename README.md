This is a very new project simply knocked up to demonstrate a problem I am experiencing in integrating Unity ADS with pygame. 
At the moment I have only got interstitial ads working for the purposes of my own integration.
It currently works with Kivy but leads to black screen death with Pygame.
Copy KivUnity.Py into the source folder. Follow UnityADS integration instructions,e.g.

Add Unity-ads.aar to your /libs folder

Update your buildozer.spec file to include the following:
 
     android.permissions = INTERNET,ACCESS_NETWORK_STATE

Un-comment this or place the aar file in a location of your choice

     # (list) Android AAR archives to add (currently works only with sdl2_gradle
     # bootstrap)
     android.add_aars = ./libs/*.aar

Don't forget to include jnius in your list of requirements
 
Add the following acitivites to your Android manifest file:

        <activity
            android:name="com.unity3d.services.ads.adunit.AdUnitActivity"
            android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
            android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
            android:hardwareAccelerated="true" />

         <activity
            android:name="com.unity3d.services.ads.adunit.AdUnitTransparentActivity"
            android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
            android:theme="@android:style/Theme.Translucent.NoTitleBar.Fullscreen"
            android:hardwareAccelerated="true" />

         <activity
            android:name="com.unity3d.services.ads.adunit.AdUnitTransparentSoftwareActivity"
            android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
            android:theme="@android:style/Theme.Translucent.NoTitleBar.Fullscreen"
            android:hardwareAccelerated="false" />

         <activity
            android:name="com.unity3d.services.ads.adunit.AdUnitSoftwareActivity"
            android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen"
            android:theme="@android:style/Theme.NoTitleBar.Fullscreen"
            android:hardwareAccelerated="false" />

In your main.py, use the following methods;

     Import Kivunity

Instantiate the class Unity_handler early on; 

     unity_ads = kivunity.Unity_handler(app_id)

Early on, initialize Unity ads; 

    unity_ads.init_unity()

When ready to show the ad; 

    unity_ads.show_ad(inter_id) 



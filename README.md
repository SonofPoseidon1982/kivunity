This is a very new project simply knocked up to demonstrate a problem I am experiencing in integrating Unity ADS with pygame. 
It currently works with Kivy but leads to black screen death with Pygame.
Copy KivUnity.Py into the source folder. Follow UnityADS integration instructions,e.g.

Add Unity-ads.aar to your /libs folder

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

In your main.py, use the folowing methods;

     Import Kivunity

Instantiate the class Unity_handler early on; 

     unity_ads = kivunity.Unity_handler(app_id)

Early on, initialize Unity ads; 

    unity_ads.init_unity()

When ready to show the ad; 

    unity_ads.show_ad(inter_id) 



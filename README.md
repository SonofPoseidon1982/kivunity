This project started off as a means of demonstrating a problem I am experiencing in integrating Unity ADS with pygame. 
However, I decided to develop it further to explore the potential of implementing unity ads in both Kivy and pygame.

GENERAL GUIDELINES:

1. Add Unity-ads.aar to your /libs folder

2. Update your buildozer.spec file to include the following:
 
     android.permissions = INTERNET,ACCESS_NETWORK_STATE

3. Un-comment this or place the aar file in a location of your choice

        # (list) Android AAR archives to add (currently works only with sdl2_gradle
        # bootstrap)
        android.add_aars = ./libs/*.aar

4. Don't forget to include jnius in your list of buildozer requirements
 
5. Add the following acitivites to your Android manifest file:

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

Early on, initialize Unity ads, specifying whether it is to be implemebted in testmode or not; 

    #for testmode
    testmode=True
    unity_ads.init_unity(testmode)

INTERSTITIALS:

For interstitials, when ready to show the ad anywhere in your code simply add; 

    unity_ads.show_ad(ad_id) 


REWARD ADS:

** In progress **

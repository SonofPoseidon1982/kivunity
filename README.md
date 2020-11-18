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


PYGAME IMPLEMENTATION:

In Kivy the above implementation is straightforward. However, in pygame there are addition complications due to
the method in which pygame draws graphics to the surface in terms of frames per second. Hence, the main approach
is to paused the fps temporarily until the ad is viewed and then resume the fps.

In UnityAdsListener interface (in kivunity.py) 'ad_shown=True' is returned when the ad has finished slowing:

      @java_method('(Ljava/lang/String;Lcom/unity3d/ads/UnityAds$FinishState;)V')
       def onUnityAdsFinish(self,inter_id,finish_state):
         global ad_shown
         logging.warning("\n\n ADS are FINISHED! "+str(finish_state) + " \n\n")
         #appl_id = u_h.app_id2                                                     
         ad_shown = True 
    
The following method returns True when the ad is shown
 
         def check_ad_status(self):
            return ad_shown

In your main pygame you may have something like this implemented for pausing the app and rendering graphics
per second:

       tmp_sleep=False
       pygame.display.init()
       fps=27
       py_display =pygame.display.set_mode((0, 0),pygame.FULLSCREEN)     
         
       
       while game_loop==True:
         while g_pause = False: 
             #main methods
        
         pygame.display.flip()

         
         py_clock.tick(fps)

If you try to use g_pause=True, it will stop display your game graphics but the fps will continue to update
which will conflict with the full screen ad being shown. So the following methods are added to ensure the
ad is shown without surface conflicts:

       tmp_sleep=False
       pygame.display.init()
       fps=27
       py_display =pygame.display.set_mode((0, 0),pygame.FULLSCREEN)     
         
       
       while game_loop==True:
         if unity_show==True:
              tmp_sleep = False
              unity_ads.show_ad(ad_id)             
              while tmp_sleep==False:
                 tmp_sleep = unity_ads.check_ad_status()
                 time.sleep(1)
              self.g_sleep=False
              py_display =pygame.display.set_mode((0, 0),pygame.FULLSCREEN)     
              print("\n\n Pygame window back into focus \n\n ")

         while self.g_pause = False: 
             #main methods
        
         pygame.display.flip()

         
         py_clock.tick(fps)

#! /usr/bin/python

import re
import sys
import os 
from android.runnable import run_on_ui_thread
from jnius import autoclass, PythonJavaClass, java_method, cast
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

import logging

testmode = True
#inter_id = "12839"
#app_id = "3786901"
ad_id = 0
app_id = 0
app_fin = False
reward_viewed = False
ad_type = "interstitial"

PythonActivity = autoclass("org.kivy.android.PythonActivity")
Unity_ads_listener = autoclass("com.unity3d.ads.IUnityAdsListener")
Unity_ads = autoclass("com.unity3d.ads.UnityAds")
logging.info("\n\n You've reached passed init \n\n")



              

class Unity_handler():
    

   def __init__(self, app_id_2):
     self.a_id = app_id_2
   
   def init_unity(self,test_m):
     global app_id
     global testmode
     testmode = test_m
     app_id = self.a_id  
     self.new_ad_listener = UnityAdsListener()
     #Unity_ads.addListener(new_ad_listener)
     Unity_ads.setListener(self.new_ad_listener)
     self.c_activity = cast('android.app.Activity',PythonActivity.mActivity)
     Unity_ads.initialize(self.c_activity,app_id,testmode)
     #Unity_ads.initialize(PythonActivity.mActivity,app_id,testmode)
       
   def request_type(self,ad_method):
      global ad_type
      ad_type=ad_method
 
   def show_ad(self, id_num):
     # show interstial or reward ad
     global ad_id   
     global app_fin
     app_fin = False
     #show interstial ads
     ad_id = id_num
     logging.info("\n\n self.c_activity="+str(self.c_activity)+"\n\n")
     logging.info("\n\n app_id="+str(app_id)+"\n\n")
     logging.info("\n\n new_ad_listener="+str(self.new_ad_listener)+"\n\n")
     
     if Unity_ads.isReady(ad_id):
          try:
            
            Unity_ads.show(self.c_activity, ad_id)
            
          except:
            logging.info("Unity ads not ready and thus has not been loaded") 
            app_fin = True
     else:
            logging.info("Unity ads not ready and thus has not been loaded") 
            app_fin = True

   def check_ad_status(self):
      if ad_type=="interstitial":
         return app_fin
      elif ad_type=="reward":
         return reward_viewed
 
class UnityAdsListener(PythonJavaClass):
    __javainterfaces__= ['com/unity3d/ads/IUnityAdsListener']
    __javacontext__= 'app'

    @java_method('(Ljava/lang/String;)V')
    def onUnityAdsReady(self,inter_id):
       logging.info("\n\n ADS are ready! "+ str(inter_id) + " \n\n")
       #pass        

    @java_method('(Ljava/lang/String;)V')   
    def onUnityAdsStart(self,inter_id):
       #pass
#       global app_fin
       logging.info("\n\n ADS are starting! " + str(inter_id) + "\n\n")
#       app_fin = False

    @java_method('(Ljava/lang/String;Lcom/unity3d/ads/UnityAds$FinishState;)V')
    def onUnityAdsFinish(self,inter_id,finish_state):
       #pass
       global app_fin
       logging.info("\n\n ADS are FINISHED! "+str(finish_state) + " \n\n")
       #appl_id = u_h.app_id2                                                     
       app_fin = True 
       if ad_type=="reward":
          #If the type is a reward ad
          if finish_state.equals(Unity_ads.FinishState.COMPLETED)==True:
               reward_viewed=True
               logging.info("\n\n Unity Reward AD shown \n\n")
               
          elif finish_state.equals(Unity_ads.FinishState.SKIPPED)==True:
               reward_viewed=False
             
    @java_method('(Lcom/unity3d/ads/UnityAds$UnityAdsError;Ljava/lang/String;)V')
    def onUnityAdsError(self,error, message):
       #pass 
       logging.info("\n\n ADS are in error! \n\n")



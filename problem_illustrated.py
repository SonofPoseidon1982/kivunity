# This file just demonstrates the usage of the methods to outline the problem. Whenever the interstitial ads try to load
# I get a black screen death for reasons unknown. This method works in Kivy


#! /usr/bin/python

import re
import sys
import os 
import datetime
import pygame

import random
from jnius import autoclass, PythonJavaClass, java_method, cast
import logging

PythonActivity = autoclass("org.kivy.android.PythonActivity")
Unity_ads_listener = autoclass("com.unity3d.ads.IUnityAdsListener")
Unity_ads = autoclass("com.unity3d.ads.UnityAds")
logging.warning("\n\n You've reached passed init \n\n")

fps = 25
app_id = "#######"
inter_id = "#####"
testmode = True

pygame.display.init()
display_info = pygame.display.Info()
display_width = display_info.current_w

display_height = display_info.current_h
py_display =pygame.display.set_mode((display_width, display_height),pygame.FULLSCREEN)


pygame.init()
py_clock = pygame.time.Clock()



class Main_screen():

   def build(self):
        self.unity_show=False
        unity_ads.init_unity()
        while self.g_loop==True:
           if self.unity_show==True:
              self.g_sleep=True
              self.unity_show = False
              unity_ads.show_ad(inter_id) 
           
           if self.g_sleep==False:
           # if the game is not paused
           # Here images are blitted on the surface etc at 25 fps.....
           # and when the end of a game level is reached
                 if self.level_completed==True:
                                self.current_level = self.current_level + 1
                                     
                                self.unity_show = True
                                self.start_level()
                 
                 for event_list in pygame.event.get():         
                    if event_list.type == 259: # If pygame is about to pause
                        self.g_sleep=True
                    if event_list.type == 262: # pygame is resumed
                        self.g_sleep=False
                        py_display =pygame.display.set_mode((display_width, display_height),pygame.FULLSCREEN)



           pygame.display.update()
           py_clock.tick(fps) 

   def start_level(self):
       # Here is just example of things thar are blited to the screen
       py_display.blit(game_menu_img,(game_menu_x, game_menu_y))
       py_display.blit(self.py_txt_level, (level_pos_x, report_pos_y))             
       py_display.blit(self.py_txt_score, (score_pos_x, report_pos_y))             
       py_display.blit(self.py_event_record, (event_record_pos_x, event_record_pos_y))
       py_display.blit(button_back_img, (button_back_pos_x, button_back_pos_y))
       py_display.blit(img_panel, (panel_pos_x, panel_pos_y))
       py_display.blit(img_minus, (minus_pos_x, minus_pos_y))
       py_display.blit(img_plus, (plus_pos_x, plus_pos_y))

        
class Unity_handler():
    

   def __init__(self, app_id_2):
     self.a_id = app_id_2
     
   
   def init_unity(self):
     global app_id
     app_id = self.a_id  
     self.new_ad_listener = UnityAdsListener()
     #Unity_ads.addListener(new_ad_listener)
     Unity_ads.setListener(self.new_ad_listener)
     self.c_activity = cast('android.app.Activity',PythonActivity.mActivity)
     Unity_ads.initialize(self.c_activity,app_id,testmode)
     #Unity_ads.initialize(PythonActivity.mActivity,app_id,testmode)
       
 
   def show_ad(self, id_num):
     global inter_id   
     #show interstial ads
     inter_id = id_num
     logging.warning("\n\n self.c_activity="+str(self.c_activity)+"\n\n")
     logging.warning("\n\n app_id="+str(app_id)+"\n\n")
     logging.warning("\n\n new_ad_listener="+str(self.new_ad_listener)+"\n\n")

     if Unity_ads.isReady(inter_id):
          try:
       
            Unity_ads.show(self.c_activity, inter_id)
            
          except:
            logging.warning("Unity ads not ready and thus has not been loaded") 


class UnityAdsListener(PythonJavaClass):
    __javainterfaces__= ['com/unity3d/ads/IUnityAdsListener']
    __javacontext__= 'app'

    @java_method('(Ljava/lang/String;)V')
    def onUnityAdsReady(self,inter_id):
       logging.warning("\n\n ADS are ready! "+ str(inter_id) + " \n\n")
       #pass        

    @java_method('(Ljava/lang/String;)V')   
    def onUnityAdsStart(self,inter_id):
       #pass
       logging.warning("\n\n ADS are starting! " + self(inter_id) + "\n\n")

    @java_method('(Ljava/lang/String;Lcom/unity3d/ads/UnityAds$FinishState;)V')
    def onUnityAdsFinish(self,inter_id,finish_state):
       #pass
       logging.warning("\n\n ADS are FINISHED! "+str(finish_state) + " \n\n")
       

 
    @java_method('(Lcom/unity3d/ads/UnityAds$UnityAdsError;Ljava/lang/String;)V')
    def onUnityAdsError(self,error, message):
       #pass 
       logging.warning("\n\n ADS are in error! \n\n")






main_root = Main_screen()
unity_ads = Unity_handler(app_id)
main_root.build()

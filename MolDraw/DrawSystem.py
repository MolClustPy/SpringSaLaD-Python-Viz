# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 18:27:25 2022

@author: achattaraj
"""
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
import os
from math import atan, sin, cos
from collections import namedtuple
import re
import numpy as np

class Draw_molecules:
    
    def __init__(self, system):
        self.system = system 
    
    @staticmethod
    def draw_circle(SiteObj):
        """
        modify the color string if defined site-color is invalid
        in CSS-style matplotlib implementation (like 'dark_violet') 
        LIME_GREEN : limegreen; Dark_violet : darkviolet
        """
        coor, r = SiteObj.coordinates, SiteObj.radius
        x, y = coor[2], coor[1]
        try:
            if SiteObj.color.lower() == 'white':
                circle = plt.Circle((x,y), radius=r, facecolor='lightsteelblue')
                print("White site color encountered; replaced with lightsteelblue")
            else:
                circle = plt.Circle((x,y), radius=r, facecolor=SiteObj.color)
        except:
            color = SiteObj.color.replace("_","") # "dark_violet" has to be in "darkviolet" format
            circle = plt.Circle((x,y), radius=r, facecolor=color)  
        
        return plt.gca().add_patch(circle)
    
    def draw_line(self, SiteObj1, SiteObj2, width):
        """
        take a pair of sites ; draw a line between the surface (excluding the radius)
        For non-linear molecules, calculates the slope between two spheres and
        place the line points along that direction.
        """
        c1, r1 = SiteObj1.coordinates, SiteObj1.radius
        c2, r2 = SiteObj2.coordinates, SiteObj2.radius
        x1, y1 = c1[2], c1[1]
        x2, y2 = c2[2], c2[1]
        
        try:
            slope = atan((y2-y1)/(x2-x1))  # in radians
            
            # pn: peripherial coordinates of site n
            p1_x, p1_y = x1 + r1 * cos(slope), y1 + r1 * sin(slope)  
            p2_x, p2_y = x2 - r2 * cos(slope), y2 - r2 * sin(slope)
            
            line = plt.Line2D((p1_x, p2_x), (p1_y, p2_y), linewidth=width, color='k')
            
            return plt.gca().add_line(line)
        except:
            print(f"Can't draw line for {SiteObj1.seqNum} & {SiteObj2.seqNum} in {self.molecularName}")
            
    
    @staticmethod
    def mapLinkToSite(Sites, Links):
        siteObj_pair = []
        for link in Links:
            s1, s2 = None, None
            for site in Sites:
                if link.Site1 == site.seqNum:
                    s1 = site
                elif link.Site2 == site.seqNum:
                    s2 = site
            siteObj_pair.append((s1,s2))
        #print(siteObj_pair)
        return siteObj_pair
    
    def displayMolecules(self, Width, saveImage):
        plt.axes()
        for mol, site, link in zip(molNames, SiteList, LinkList):
            coor = np.array([SiteObj.coordinates for SiteObj in site])
        
        
        '''
        coor = np.array([SiteObj.coordinates for SiteObj in self.siteList])
        x_min, x_max = min(coor[:,2]), max(coor[:,2])
        #print(x_min, x_max)
        y_min = min(coor[:,1])
        #print(mod_sites)
        sizes = []
        for site in self.siteList:
            self.draw_circle(site)
            sizes.append(site.radius)
        molLength = self.siteList[-1].coordinates[-1] - self.siteList[0].coordinates[-1]
        Largest_ball = max(sizes) + 2
        #print(molLength,  Largest_ball)
        Linked_Sites = self.mapLinkToSite(self.siteList, self.linkList)
        #print(Linked_Sites)
        for s1, s2 in Linked_Sites:
            self.draw_line(s1, s2, width=Width)
        #plt.axes(frameon=False)
        plt.axis('image')
        
        plt.axis(xmin=x_min-4, xmax=x_max+4, ymin=y_min-Largest_ball, ymax=y_min+Largest_ball)
        plt.xlabel('nm', fontsize=16)
        plt.ylabel('nm', fontsize=16)
        plt.tick_params(axis='x', labelsize=16)
        plt.yticks([y_min-Largest_ball,y_min+Largest_ball])
        #plt.xlim((0,35))
        #Axes.set_ylim((0,5))
        
        #plt.tick_params(labelsize='small')
        if saveImage:
            plt.savefig(self.outPath+"\\{}_pyDraw.png".format(self.molecularName), dpi=400)

        plt.show()
        '''
            
            
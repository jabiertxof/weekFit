#!/usr/bin/env python 
# coding=iso-8859-15
'''
This extension Create week planning

Copyright (C) 2012 Jabiertxo Arraiza, jabier.arraiza@marker.es

Version 0.1 - fitless

TODO:
Comment Better!!!

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
'''

import inkex, sys
from lxml import etree

class Fitless(inkex.Effect):

    def __init__(self):
        inkex.Effect.__init__(self)
        self.OptionParser.add_option('--dia',  action = 'store', 
            type = 'string', dest = 'dia', default = 'LUNES', 
            help = 'Seleccione el día de la semana')
        self.OptionParser.add_option('--sala',  action = 'store', 
            type = 'string', dest = 'sala', default = 'H2', 
            help = 'Seleccione sala')
        self.OptionParser.add_option('--actividad',  action = 'store', 
            type = 'string', dest = 'actividad', default = 'AEREO/STEP MEDIO', 
            help = 'Seleccione el día de la semana')
        self.OptionParser.add_option('--S1',  action = 'store', 
            type = 'string', dest = 'S1', default = 'Sin definir', 
            help = 'Seleccione hora de inicio')
        self.OptionParser.add_option('--E1',  action = 'store', 
            type = 'string', dest = 'E1', default = 'Sin definir', 
            help = 'Seleccione hora de fin')
        self.OptionParser.add_option('--S2',  action = 'store', 
            type = 'string', dest = 'S2', default = 'Sin definir', 
            help = 'Seleccione hora de inicio')
        self.OptionParser.add_option('--E2',  action = 'store', 
            type = 'string', dest = 'E2', default = 'Sin definir', 
            help = 'Seleccione hora de fin')
        self.OptionParser.add_option('--S3',  action = 'store', 
            type = 'string', dest = 'S3', default = 'Sin definir', 
            help = 'Seleccione hora de inicio')
        self.OptionParser.add_option('--E3',  action = 'store', 
            type = 'string', dest = 'E3', default = 'Sin definir', 
            help = 'Seleccione hora de fin')
        self.OptionParser.add_option('--S4',  action = 'store', 
            type = 'string', dest = 'S4', default = 'Sin definir', 
            help = 'Seleccione hora de inicio')
        self.OptionParser.add_option('--E4',  action = 'store', 
            type = 'string', dest = 'E4', default = 'Sin definir', 
            help = 'Seleccione hora de fin')
        self.OptionParser.add_option('--mes', action = 'store', 
            type = 'string', dest = 'mes', default = 'MÉS', 
            help = 'Més')
        self.OptionParser.add_option('--pie1', action = 'store', 
            type = 'string', dest = 'pie1', default = '', 
            help = 'Línea 1 pie')
        self.OptionParser.add_option('--pie2', action = 'store', 
            type = 'string', dest = 'pie2', default = '', 
            help = 'Línea 2 pie')
        self.OptionParser.add_option('--pie3', action = 'store', 
            type = 'string', dest = 'pie3', default = '', 
            help = 'Línea 3 pie')
        self.OptionParser.add_option('--Fitnes19', action = 'store', 
            type = 'string', dest = 'Fitnes19', default = ' ', 
            help = 'Fitnes19')

    def timeStep(self,t):
        return {
            'Sin definir':0,
            '15 minutos':-1,
            '30 minutos':-2,
            '45 minutos':-3,
            '1 hora':-4,
            '6:30':1,
            '6:45':2,
            '7:00':3,
            '7:15':4,
            '7:30':5,
            '7:45':6,
            '8:00':7,
            '8:15':8,
            '8:30':9,
            '8:45':10,
            '9:00':11,
            '9:15':12,
            '9:30':13,
            '9:45':14,
            '10:00':15,
            '10:15':16,
            '10:30':17,
            '10:45':18,
            '11:00':19,
            '11:15':20,
            '11:30':21,
            '11:45':22,
            '12:00':23,
            '12:15':24,
            '12:30':25,
            '12:45':26,
            '13:00':27,
            '13:15':28,
            '13:30':29,
            '13:45':30,
            '14:00':31,
            '14:15':32,
            '14:30':33,
            '14:45':34,
            '15:00':35,
            '15:15':36,
            '15:30':37,
            '15:45':38,
            '16:00':39,
            '16:15':40,
            '16:30':41,
            '16:45':42,
            '17:00':43,
            '17:15':44,
            '17:30':45,
            '17:45':46,
            '18:00':47,
            '18:15':48,
            '18:30':49,
            '18:45':50,
            '19:00':51,
            '19:15':52,
            '19:30':53,
            '19:45':54,
            '20:00':55,
            '20:15':56,
            '20:30':57,
            '20:45':58,
            '21:00':59,
            '21:15':60,
            '21:30':61,
            '21:45':62,
            '22:00':63,
            '22:15':64,
            '22:30':68,
            '22:45':66,
            '23:00':67,
        }.get(t, 'Sin definir')

    def boxY(self,p):
        base = 480;
        stepSizeY = 23;
        return ((p-1)*stepSizeY)+base
    
    def sala(self):
        return {
            'H2':0,
            'H4':1,
            'H0':2,
            'CV':3,
            'OTRAS':4,
            'TODAS':0
        }.get(self.options.sala, 'H2')

    def dia(self):
        return {
            'LUNES':0,
            'MARTES':1,
            'MIÉRCOLES':2,
            'JUEVES':3,
            'VIERNES':4,
            'SÁBADO':5,
            'DOMINGO':6
        }.get(self.options.dia, 'LUNES')

    def boxX(self):
        base = 115
        return base + (self.sala()*60) + (self.dia()*420)
    
    def boxHeight(self,t1,t2):
        posA = self.timeStep(t1)
        posB = self.timeStep(t2)
        if posB < 0:
            posB = posA + (posB * -1)
        stepSizeY = 23;
        return (posB-posA)*stepSizeY

    def boxWidth(self):
        if self.options.sala == 'TODAS':
            ret = 300
        else:
            ret = 60
        return ret

    def boxColor(self):
        color = {
            'AERO-STEP MEDIO':'692d96',
            'AEROBIC INICIACIÓN':'692d96',
            'AEROBIC MEDIO':'692d96',
            'BOSU':'c3c300',
            'BOX':'2d798e',
            'CERRADO':'2d2d2d',
            'CICLO':'646464',
            'CICLO LIVE':'3a3a3a',
            'CORE':'c30000',
            'CROSS':'2d798e',
            'DJ. RESIDENT':'ac5c00',
            'EVENTO':'ac5c00',
            'EVENTO SÁBADO':'ac5c00',
            'EVENTO VIERNES':'ac5c00',
            'FLYING':'c30000',
            'GAP':'c30000',
            'MASTER CLASS':'692d96',
            'PILATES':'008700', 
            'RUNING NORMAL':'692d96',
            'RUNNING LIGHT':'692d96',
            'RUNNING TRAIL':'692d96',
            'STEP INICIACIÓN':'692d96',
            'STEP MEDIO':'692d96',
            'TRAINNING':'c3c300',
            'WELLNESS':'008700',
            'ZUMBA':'2d798e'
        }.get(self.options.actividad, 'AERO-STEP MEDIO')
        return color

    def makeBox(self ,t1,t2,svg):
        if t1 == 'Sin definir':
            return
        if t2 == 'Sin definir':
            return
        posA = self.timeStep(t1)
        posB = self.timeStep(t2)
        if (posB < posA and posB >= 0):
            return;
        idCode = str(posA) + '_' + str(posB) + '_' + str(self.sala()) + '_' + str(self.dia()) + '_' + self.boxColor()
        xpathStr = '//svg:g[@id="datos"]'
        layer = svg.xpath(xpathStr, namespaces=inkex.NSS)
        if layer == []:
            return
        xpathStr = '//svg:g[@id="'+idCode+'"]'
        exist = svg.xpath(xpathStr, namespaces=inkex.NSS)
        if exist != []:
            return
        container = etree.Element("g")
        container.set("id","container_" + idCode)
        layer[0].insert(len(layer[0]),container)
        rect = etree.Element("rect")
        rect.set("id","rect_" + idCode)
        rect.set("width",str(self.boxWidth()))
        rect.set("height",str(self.boxHeight(t1,t2)))
        rect.set("style","fill-opacity:0.72;fill-rule:nonzero;stroke:#c6c6c6;stroke-width:1;stroke-miterlimit:4;stroke-opacity:1;stroke-dasharray:none;marker:none;visibility:visible;display:inline;overflow:visible;enable-background:accumulate;fill:#"+self.boxColor()+";")
        rect.set("x",str(self.boxX()))
        rect.set("y",str(self.boxY(self.timeStep(t1))))
        container.insert(0,rect)
        flowRoot = etree.Element("flowRoot")
        flowRoot.set("id","flowRoot_" + idCode)
        flowRoot.set("transform","translate(0,4)")
        flowRoot.set("{http://www.w3.org/XML/1998/namespace}space","preserve")
        container.insert(1,flowRoot)
        flowRegion = etree.Element("flowRegion")
        flowRegion.set("id","flowRegion_" + idCode)
        flowRoot.insert(0,flowRegion)
        use = etree.Element("use")
        use.set("id","use_" + idCode)
        use.set("x","0")
        use.set("y","0")
        use.set("{http://www.w3.org/1999/xlink}href","#rect_" + idCode)
        flowRegion.insert(0,use)
        words = self.options.actividad.decode('utf-8').split(' ')
        i = 1;
        for word in words:
            flowPara = etree.Element("flowPara")
            flowPara.set("id","flowPara" + str(i) + "_" + idCode)
            if (word == "INICIACIÓN".decode('utf-8') or word == "MEDIO" or word == "SÁBADO".decode('utf-8') or word == "VIERNES"):
                fsize = "7"
            else:
                fsize = "8.7"
            flowPara.set("style","writing-mode:lr;font-size:" + fsize + "px;-inkscape-font-specification:Red October;font-family:Red October;font-weight:normal;font-style:normal;font-stretch:normal;font-variant:normal;fill:#ffffff;text-anchor:middle;text-align:center")
            flowPara.text = word
            flowRoot.insert(i,flowPara)
            i = i+1
        xpathStr = '//svg:text[@id="log"]'
        log = svg.xpath(xpathStr, namespaces=inkex.NSS)
        if log == []:
            return
        tspan = etree.Element("tspan")
        tspan.set("id","tspan_" + idCode)
        tspan.set("{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}role","line")
        tspan.text = self.options.actividad.decode('utf-8') + "_" + self.options.sala.decode('utf-8') + "_" + self.options.dia.decode('utf-8')+ "_" + t1 + "_" + t2
        log[0].insert(len(log[0]),tspan)

    def writeGeneral(self ,svg):
        xpathStr = '//svg:text[@id="pie1"]'
        res = svg.xpath(xpathStr, namespaces=inkex.NSS)
        res[0].text = self.options.pie1.decode('utf-8')
        xpathStr = '//svg:text[@id="pie2"]'
        res = svg.xpath(xpathStr, namespaces=inkex.NSS)
        res[0].text = self.options.pie2.decode('utf-8')
        xpathStr = '//svg:text[@id="pie3"]'
        res = svg.xpath(xpathStr, namespaces=inkex.NSS)
        res[0].text = self.options.pie3.decode('utf-8')
        xpathStr = '//svg:text[@id="mes"]'
        res = svg.xpath(xpathStr, namespaces=inkex.NSS)
        res[0].text = self.options.mes.decode('utf-8')
    
    def effect(self):
        saveout = sys.stdout
        sys.stdout = sys.stderr
        if self.options.actividad == "":
            return
        if self.options.sala == "":
            return
        if self.options.dia == "":
            return
        svg = self.document.getroot()
        self.makeBox(self.options.S1,self.options.E1,svg);
        self.makeBox(self.options.S2,self.options.E2,svg);
        self.makeBox(self.options.S3,self.options.E3,svg);
        self.makeBox(self.options.S4,self.options.E4,svg);
        self.writeGeneral(svg);
        sys.stdout = saveout
    

effect = Fitless()
effect.affect()

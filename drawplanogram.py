#!/usr/bin/env python2
# -*- coding: utf-8 -*-

"""
planogram
~~~~~~~~~~

This script implements a planogram viewer.


Usage: python2 planogram.py -p <planogram.csv>

:copyright: (c) 2015 by Daniele Liciotti.
:license: Apache2, see LICENSE for more details.
:date: 2015-10-28
"""

import argparse
import csv

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random

def show(planogram_path):
    """

    :rtype : image of planogram
    """
    figPlanogram = plt.figure()

    with open(planogram_path, "rb") as f:
        reader = csv.reader(f, delimiter=";")
        ax1 = figPlanogram.add_subplot(111, aspect='equal')
        x = [0,0,0,0,0] #planogram with 5 plane
        y = 0
        sumfac = 0
        labels = []
        vecPatch = []
        shelfDistance = 50
        nShelves = 4
        for i, line in enumerate(reader):
            if i!= 0:
                width = float(line[3])
                height = float(line[4])
                nameProd = str(line[0])
                noFacing = int(line[5])
                noPlane = int(line[1])
                sumfac += noFacing

                labels.append(nameProd)
                ax1.text(x[nShelves + 1 - noPlane - 1]+(width/2),
                        (nShelves + 1 - noPlane-1)*shelfDistance+(height*1.05),
                        i, horizontalalignment='center',
                        verticalalignment='bottom',
                        fontsize=7,
                        rotation='horizontal')
                r = lambda: random.randint(0,255)	
                myColor = (40 + (i) + 90 * (i%2)) % 255
                #color = '#%02X%02X%02X' % (r(),r(),r())
                #color = '#%02X%02X%02X' % ((125 + pow(-1,i+1) * (i) ) % 255,(125 + pow(-1,i+1) * (i)) % 255,(125 + pow(-1,i+1) * (i)) % 255)
                color = '#%02X%02X%02X' % (myColor,myColor,myColor)
                for facing in range(0, noFacing):
                    rect = patches.Rectangle(
                        (x[nShelves + 1 - noPlane-1], (nShelves + 1 - noPlane-1)*shelfDistance),        # (x,y)
                        width,                                  # width
                        height,                                 # height
                        facecolor=color,
                        fill=True,
                        linewidth=1,
                    )
                    ax1.add_patch(rect)
                    x[nShelves + 1 - noPlane-1] += width
                vecPatch.append(rect)

    #figPlanogram.legend(vecPatch, labels)

    plt.rcParams.update({'font.size': 5})
    axes = figPlanogram.gca()
    axes.set_xlim([0,max(x)])
    axes.set_ylim([0,shelfDistance*(4+1)])

    figPlanogram.show()
    figPlanogram.waitforbuttonpress()

    figPlanogram.savefig('planogram.pdf', dpi=1200, bbox_inches='tight')

def main():
    """The entry point"""
    # set and parse the arguments list
    p = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter, description="")
    p.add_argument('--p', dest='planogram_path', action='store', default='', help='path Planogram')
    args = p.parse_args()
    # show the capture!
    show(args.planogram_path)

if __name__ == '__main__':
    main()
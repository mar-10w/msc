#!/usr/bin/env python3

import rospy
import heapq

from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

GRID = 30

start = (2,2)
goal = (28,28)

obstacles = set()

# Obstacle 1
for i in range(5,20):
    obstacles.add((10,i))

# Obstacle 2
for i in range(10,25):
    obstacles.add((20,i))

def heuristic(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])

def astar(start,goal):

    open_list=[]

    heapq.heappush(open_list,(0,start))

    came_from={}

    g={start:0}

    while open_list:

        current=heapq.heappop(open_list)[1]

        if current==goal:

            path=[]

            while current in came_from:
                path.append(current)
                current=came_from[current]

            path.append(start)

            path.reverse()

            return path

        x,y=current

        neighbors=[

        (x+1,y),
        (x-1,y),
        (x,y+1),
        (x,y-1)

        ]

        for n in neighbors:

            if n[0]<0 or n[0]>=GRID:
                continue

            if n[1]<0 or n[1]>=GRID:
                continue

            if n in obstacles:
                continue

            new_cost=g[current]+1

            if n not in g or new_cost<g[n]:

                g[n]=new_cost

                priority=new_cost+heuristic(goal,n)

                heapq.heappush(open_list,(priority,n))

                came_from[n]=current

    return []

def make_points(cells):

    pts=[]

    for c in cells:

        p=Point()

        p.x=c[0]
        p.y=c[1]
        p.z=0

        pts.append(p)

    return pts

rospy.init_node("astar_demo")

pub=rospy.Publisher("visualization_marker",Marker,queue_size=10)

rate=rospy.Rate(1)

path=astar(start,goal)

while not rospy.is_shutdown():

    marker=Marker()

    marker.header.frame_id="map"

    marker.header.stamp=rospy.Time.now()

    marker.ns="path"

    marker.id=0

    marker.type=Marker.LINE_STRIP

    marker.action=Marker.ADD

    marker.scale.x=0.2

    marker.color.r=1.0
    marker.color.g=0.0
    marker.color.b=0.0
    marker.color.a=1.0

    marker.points=make_points(path)

    pub.publish(marker)

    obs=Marker()

    obs.header.frame_id="map"

    obs.header.stamp=rospy.Time.now()

    obs.ns="obstacle"

    obs.id=1

    obs.type=Marker.CUBE_LIST

    obs.action=Marker.ADD

    obs.scale.x=1
    obs.scale.y=1
    obs.scale.z=0.2

    obs.color.r=0
    obs.color.g=0
    obs.color.b=1
    obs.color.a=1

    obs.points=make_points(obstacles)

    pub.publish(obs)

    s=Marker()

    s.header.frame_id="map"

    s.ns="start"

    s.id=2

    s.type=Marker.SPHERE

    s.action=Marker.ADD

    s.pose.position.x=start[0]
    s.pose.position.y=start[1]

    s.scale.x=0.8
    s.scale.y=0.8
    s.scale.z=0.8

    s.color.g=1
    s.color.a=1

    pub.publish(s)

    g=Marker()

    g.header.frame_id="map"

    g.ns="goal"

    g.id=3

    g.type=Marker.SPHERE

    g.action=Marker.ADD

    g.pose.position.x=goal[0]
    g.pose.position.y=goal[1]

    g.scale.x=0.8
    g.scale.y=0.8
    g.scale.z=0.8

    g.color.r=1
    g.color.g=1
    g.color.a=1

    pub.publish(g)

    rate.sleep()
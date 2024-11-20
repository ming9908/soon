import { Tabs } from 'expo-router';
import React from 'react';

import { TabBarIcon } from '@/components/navigation/TabBarIcon';
import { Colors } from '@/constants/Colors';

export default function TabLayout() {
  return (
    <Tabs
      screenOptions={{
        tabBarActiveTintColor: Colors.main.soon,
        headerShown: false,
      }}>
      <Tabs.Screen
        name="soon"
        options={{
          title: '',
          tabBarIcon: ({ color, focused }) => (
            <TabBarIcon name={focused ? 'flower' : 'flower-outline'} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="calendar"
        options={{
          title: '',
          tabBarIcon: ({ color, focused }) => (
            <TabBarIcon name={focused ? 'calendar-clear' : 'calendar-clear-outline'} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="home"
        options={{
          title: '',
          tabBarIcon: ({ color, focused }) => (
            <TabBarIcon name={focused ? 'home' : 'home-outline'} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="community"
        options={{
          title: '',
          tabBarIcon: ({ color, focused }) => (
            <TabBarIcon name={focused ? 'chatbubbles' : 'chatbubbles-outline'} color={color} />
          ),
        }}
      />
      <Tabs.Screen
        name="setting"
        options={{
          title: '',
          tabBarIcon: ({ color, focused }) => (
            <TabBarIcon name={focused ? 'settings' : 'settings-outline'} color={color} />
          ),
        }}
      />
    </Tabs>
  );
}

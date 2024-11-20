import { Calendar } from 'react-native-calendars';

import { ThemedView as View } from '../../components/ThemedView';
import { SoonStyles as styles } from '../../constants/Styles';
import React from 'react';

export default function SoonCalendar () {
  return (
    <View style={styles('').content}>
      <Calendar
        onDayPress={day => {
          console.log('selected day', day);
        }}
      />
    </View>
  );
}

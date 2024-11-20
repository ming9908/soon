import { SoonText as Text } from '../../components/SoonText';
import { ThemedView as View } from '../../components/ThemedView';
import { SoonStyles as styles } from '../../constants/Styles';
import React, { useEffect, useState } from 'react';
import Thumbnail from '../../components/Thumbnail';

export default function HomeScreen () {
  const [hot, setHot] = useState([]);
  const [popular, setPopular] = useState([]);
  const [recent, setRecent] = useState([]);

  useEffect(() => {

  }, []);

  return (
    <View style={styles('').content}>
      <View>
        <Text type={'subtitle'}>오늘의  HOT!</Text>
        <View style={styles('').thumbnailList}>
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          <Thumbnail
            info={{
              source: '',
              text: '',
            }}
          />
          ß
        </View>
      </View>
      <Text style={styles('').noti}>요즘은 고구마가 대세!</Text>
    </View>
  );
}

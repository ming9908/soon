import { SoonText as Text } from '../../components/SoonText';
import { ThemedView as View } from '../../components/ThemedView';
import { SoonStyles as styles } from '../../constants/Styles';
import React from 'react';

export default function Setting () {
  return (
    <View style={styles('').content}>
      <View>
        <Text type="subtitle">공지사항</Text>
        <Text type="subtitle">자주 찾는 질문</Text>
        <Text type="subtitle">알림설정</Text>
        <Text type="subtitle">이용약관</Text>
        <Text type="subtitle">개인정보처리방침</Text>
      </View>
    </View>
  );
}

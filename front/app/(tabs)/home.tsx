import { Agenda } from 'react-native-calendars';

import { ThemedView as View } from '../../components/ThemedView';
import { SoonStyles as styles } from '../../constants/Styles';
import React, { useEffect, useState } from 'react';
import Todo from '../../components/Todo';

export default function Home () {
  const [todo, setTodo] = useState([
    {
      type: '',
      plant: '',
      plantImg: '',
      plantNm: '',
      text: '',
    },
  ]);

  useEffect(() => {
    async function init () {
      // const todo = await
      const todo = [
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '로즈마리',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '로요미',
          text: '',
        },
        {
          type: '물',
          plant: '수국',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '',
          text: '',
        },
        {
          type: '분갈이',
          plant: '장미허브',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '괴물',
          text: '',
        },
        {
          type: '영양제',
          plant: '애플민트',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '애플칙',
          text: '',
        },
        {
          type: '영양제',
          plant: '수국',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '',
          text: '',
        },
        {
          type: '환기',
          plant: '스투키',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '',
          text: '',
        },
        {
          type: '물',
          plant: '고수',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '',
          text: '',
        },
        {
          type: '기타',
          plant: '',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '',
          text: '유튜브 보기',
        },
        {
          type: '기타',
          plant: '',
          plantImg: 'https://reactjs.org/logo-og.png',
          plantNm: '',
          text: '식물 사전 구경',
        },
      ];
      setTodo(todo);
    };
    init();
  }, []);

  return (
    <View style={styles('').content}>
      <Agenda
        disalbedPan={true}
        disableWeekScroll={true}
        displayLoadingIndicator={false}
        allowSelectionOutOfRange={false}
        firstDay={new Date(new Date().setDate(new Date().getDate() - 3)).getDay()}
        minDate={new Date(new Date().setDate(new Date().getDate() - 3)).toISOString()}
        maxDate={new Date(new Date().setDate(new Date().getDate() + 3)).toISOString()}
      />
      {todo[0]['type'] && <Todo todo={todo} />}
    </View>
  );
}
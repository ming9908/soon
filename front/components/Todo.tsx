// import { ThemedText as Text } from '@/components/ThemedText';
import { ThemedView as View } from '../components/ThemedView';
import { Colors } from '../constants/Colors';
import { SoonStyles as styles, textEllipsis } from '../constants/Styles';
import React, { useEffect, useState } from 'react';
import Avartar from './Avartar';
import { SoonText as Text } from './SoonText';
import Thumbnail from './Thumbnail';

export default function Todo({ todo }) {
  const [water, setWater] = useState(null);
  const [air, setAir] = useState(null);
  const [tonic, setTonic] = useState(null);
  const [repot, setRepot] = useState(null);
  const [other, setOther] = useState(null);

  useEffect(() => {
    const water = todo.filter((todo) => {
      return todo.type === '물';
    });
    const tonic = todo.filter(todo => {
      return todo.type === '영양제';
    });
    const repot = todo.filter(todo => {
      return todo.type === '분갈이';
    });
    const air   = todo.filter(todo => {
      return todo.type === '환기';
    });
    const other = todo.filter(todo => {
      return todo.type === '기타';
    });

    function init () {
      setWater(water);
      setTonic(tonic);
      setRepot(repot);
      setAir(air);
      setOther(other);
    }
    init();
  }, []);
  return (
    <View style={{
      // ...styles.container,
      gap: 16
      }}>
      {water && <TodoCard todo={water} style={{ backgroundColor: Colors.todo.water, color: Colors.todo.waterText }} />}
      {tonic && <TodoCard todo={tonic} style={{ backgroundColor: Colors.todo.tonic, color: Colors.todo.tonicText }} />}
      {repot && <TodoCard todo={repot} style={{ backgroundColor: Colors.todo.repot, color: Colors.todo.repotText }} />}
      {air && <TodoCard todo={air} style={{ backgroundColor: Colors.todo.water, color: Colors.todo.waterText }} />}
      {other && <TodoCard todo={other} style={{ backgroundColor: Colors.todo.other, color: Colors.todo.otherText }} />}
    </View>
  );
}

function TodoCard ({ todo, style }) {
  return (
    <View style={styles(style).card}>
      {
        todo[0]['type'] === "기타"
        ? (
            <>
              <View style={styles(style).cardTitle}>오늘 할 일!</View>
              <View style={styles(style).todoList}>
                {
                  todo.map((item, index) => {
                    return(
                    <Text type={'default'} key={index}>{index + 1}. {item.text}</Text>
                    )
                  })
                }
              </View>
            </>
          )
        : (
            <>
              <View style={styles(style).cardTitle}>{todo[0]['type']} 필요한 친구들!</View>
              <View style={styles(style).avartarList}>
                {
                  todo.map((item, index) => {
                    return(
                    <Avartar
                      key={index}
                      profile={{
                        source: item.plantImg,
                        name: !item.plantNm ? item.plant : item.plantNm,
                      }}
                    />
                    )
                  })
                }
              </View>
            </>
          )
      }
    </View>
  )
};
import React, { useEffect, useState } from 'react';
import {
  ImageBackground,
  StyleSheet,
  TouchableOpacity,
} from 'react-native';

import { SoonText as Text } from '../components/SoonText';
import { ThemedView as View } from '../components/ThemedView';
import { Colors, basic } from '../constants/Colors';
import CommonModal from '../components/modal/common/commonModal';
import Login from '../components/modal/user/Login';

export default function Index () {
  const [loginShown, setLoginShow] = useState(false);
  const [singinShown, setSigninShow] = useState(false);
  const [passwordShown, setPasswordShow] = useState(false);

  const onLoginButtonClick = () => {
    setLoginShow(!loginShown);
  }
  const onSinginButtonClick = () => {
    setSigninShow(!singinShown);
  }
  const onPasswordButtonClick = () => {
    setPasswordShow(!passwordShown);
  }

  useEffect(() => {

  }, []);

  return (
    <ImageBackground
      source={require('../assets/images/splash.png')}
      resizeMode={"cover"}
      style={styles.image}
    >
      <TouchableOpacity
        style={styles.button}
        // onPress={() => navigation.navigate('Contact')}
        onPress={onLoginButtonClick}
        >
        <Text style={styles.buttonText}>Login</Text>
      </TouchableOpacity>
      <View style={styles.imageTextBackground}>
        <TouchableOpacity onPress={onSinginButtonClick}><Text style={styles.imageText}>회원가입</Text></TouchableOpacity>
        <Text style={styles.imageText}> / </Text>
        <TouchableOpacity onPress={onPasswordButtonClick}><Text style={styles.imageText}>비밀번호 찾기</Text></TouchableOpacity>
      </View>
      
      <CommonModal
        isVisible={loginShown}
        onClose={onLoginButtonClick}
        modalTitle={'로그인'}
      >
        <Login />
      </CommonModal>
      
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
  image: {
    flex: 1,
    justifyContent: 'center',
    position: 'relative',
    textAlign: 'center',
    alignItems: 'center',
    overflow: 'hidden',
  },
  button: {
    backgroundColor: basic.white,
    borderRadius: 50,
    width: '70%',
    height: '5%',
    bottom: 70,
    position: 'absolute',
    textAlign: 'center',
    alignItems: 'center',
    justifyContent: 'center',

  },
  buttonText: {
    color: Colors.splash,
    fontWeight: '500',
    fontFamily: "Itim",
  },
  imageTextBackground: {
    width: '70%',
    position: 'absolute',
    textAlign: 'right',
    alignItems: 'flex-end',
    justifyContent: 'flex-end',
    backgroundColor: 'transparent',
    flexDirection: 'row',
    bottom: 40,
  },
  imageText: {
    fontWeight: 500,
    color: basic.white,
  },
});

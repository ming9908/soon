/**
 * Below are the colors that are used in the app. The colors are defined in the light and dark mode.
 * There are many other ways to style your app. For example, [Nativewind](https://www.nativewind.dev/), [Tamagui](https://tamagui.dev/), [unistyles](https://reactnativeunistyles.vercel.app), etc.
 */

const tintColorLight = '#0a7ea4';
const tintColorDark = '#fff';
const soon = '#85C56F';

const reactDefaultGrey = '#687076';
const reactDarkModeGrey = '#9BA1A6';
const reactDefaultBlack= '#151718';

export const bootstrap = {
  primary: '#0d6efd',
  secondary: '#6c757d',
  success: '#198754',
  warn: '#ffc107',
  danger: '#dc3545',
  info: '#0dcaf0',
};

export const basic = {
  black: '',
  white: '#fff',
  grey: '#808080',
  lightgrey: '#eaeaea',
}

export const Colors = {
  light: {
    text: '#11181C',
    background: tintColorDark,
    tint: tintColorLight,
    icon: reactDefaultGrey,
    tabIconDefault: reactDefaultGrey,
    tabIconSelected: tintColorLight,
  },
  dark: {
    text: '#ECEDEE',
    background: reactDefaultBlack,
    tint: tintColorDark,
    icon: reactDarkModeGrey,
    tabIconDefault: reactDarkModeGrey,
    tabIconSelected: tintColorDark,
  },
  soon: soon,
  splash: '#40765E',
  link: tintColorLight,

  main: {
    soon: soon,
  },

  thumbnail: '#D9D9D9',

  todo: {
    water: '#EFF9FE',
    waterText: '#3591D7',
    tonic: '#FEFCEF',
    tonicText: '#A6D735',
    repot: '#FEF7EF',
    repotText: '#D78935',
    other: '#F6F4F2',
    otherText: basic.grey,
  },
  vege: {
    pupleYam: '#CB9FE0',
  },
};

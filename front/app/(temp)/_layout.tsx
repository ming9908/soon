import { Stack, Slot } from 'expo-router';

import Header from '../../components/Header';
import Footer from '../../components/Footer';

const BasicLayout = () => {
  return (
    <>
      <Header />
      <Slot />
      <Footer />
    </>
  );
};

export default BasicLayout;
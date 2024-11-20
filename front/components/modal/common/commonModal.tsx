import { SoonText as Text } from '../../SoonText';
import { ThemedView as View } from '../../ThemedView';
import { PropsWithChildren } from 'react';
import { Modal, Pressable, StyleSheet } from 'react-native';
import EvilIcons from '@expo/vector-icons/EvilIcons';
import { Colors, basic } from '../../../constants/Colors';

type Props = PropsWithChildren<{
  isVisible: boolean;
  onClose: () => void;
  modalTitle: string;
}>;

export default function CommonModal ({ isVisible, children, modalTitle, onClose }: Props) {
  return (
    <Modal animationType="slide" transparent={true} visible={isVisible} style={styles.modalContainer}>
      <View style={styles.modalContent}>
        <View style={styles.titleContainer}>
          {modalTitle && <Text style={styles.title}>{modalTitle}</Text>}
          <Pressable onPress={onClose} style={styles.button}>
            <EvilIcons name="close" color={basic.grey} size={18}/>
          </Pressable>
        </View>
        <View style={styles.contentContainer}>
            {children}
        </View>
        
      </View>
    </Modal>
  );
}

const styles = StyleSheet.create({
    modalContainer: {
        flex: 1,
        overflow: 'scroll',
    },
    modalContent: {
        height: '40%',
        // height: 'auto',
        width: '80%',
        borderRadius: 20,
        position: 'absolute',
        bottom: 70,
        left: '10%',
        
    },
    titleContainer: {
        height: '10%',
        top: 0,
        position: 'absolute',
        flexDirection: 'row',
        alignItems: 'center',
        marginVertical: 20,
        width: '100%',
    },
    title: {
        fontSize: 16,
        marginLeft: 20,
    },
    contentContainer: {
        top: '10%',
        position: 'absolute',
        alignItems: 'center',
        margin: 30,
    },
    button: {
        position: 'absolute',
        textAlign: 'right',
        alignItems: 'flex-end',
        justifyContent: 'flex-end',
        marginLeft: '90%',
    }
});

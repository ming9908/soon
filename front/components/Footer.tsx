import AntDesign from '@expo/vector-icons/AntDesign';


import { SoonText as Text } from '../components/SoonText';
import { ThemedView as View } from '../components/ThemedView';

export default function Footer () {
    return (
        <View style={{ flexDirection: 'row' }}>
            <AntDesign name="copyright" size={16} color="black" />
            <Text>copyright</Text>
        </View>
    );
}
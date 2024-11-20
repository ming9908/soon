import Ionicons from '@expo/vector-icons/Ionicons';
import AntDesign from '@expo/vector-icons/AntDesign';
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';
import EvilIcons from '@expo/vector-icons/EvilIcons';

import { SoonText as Text } from '../components/SoonText';
import { ThemedView as View } from '../components/ThemedView';
import { Colors } from '../constants/Colors';
import { useThemeColor } from '../hooks/useThemeColor';

export default function Header ({ props }) {
    const color = useThemeColor({ light: 'black', dark: 'white' }, 'background');

    return (
        <View
            style={{
                height: 50,
                flexDirection: 'row',
            }}
        >
            <EvilIcons name="chevron-left" size={36} color="black" />
            <View style={{}}>
                <Text
                    type='default'
                    style={{
                        textAlign: 'center'
                    }}
                >header</Text>
            </View>
            <MaterialCommunityIcons name="bell-outline" size={24} color="black" />
            <MaterialCommunityIcons name="bell-badge" size={24} color="black" />
            <View style={{width: '5%'}}></View>
            
            
        </View>
    );
}
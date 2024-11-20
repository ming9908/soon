import React from 'react';
import { View, Image } from 'react-native';

import { SoonStyles as styles } from '../constants/Styles';

export default function Avartar ({ profile }) {
    return (
        <View>
            <View style={styles('').avartar}>
                <Image
                    source={{ uri: profile.source }} /** example */
                    resizeMode='cover'
                    style={styles('').avartarImage}
                />
            </View>
            <View style={styles('').avartarLabel}>{profile.name}</View>
        </View>
    )
}
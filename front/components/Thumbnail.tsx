import React from 'react';
import { View, Image } from 'react-native';

import { SoonStyles as styles, textEllipsis } from '../constants/Styles';
import { SoonText as Text } from './SoonText';

export default function Thumbnail ({ info }) {
    return (
        <View style={{width: 85}}>
            <View style={styles('').thumbnail}>
                <Image
                    source={{ uri: info.source }} /** example */
                    resizeMode='cover'
                    style={styles('').thumbnailImage}
                />     
            </View>
            {info.text && <Text>{info.text}</Text>}
        </View>
            
    )
}
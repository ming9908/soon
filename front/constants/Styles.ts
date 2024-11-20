import { StyleSheet } from 'react-native';
import { Colors, basic } from '../constants/Colors';


export const SoonStyles = (props) => StyleSheet.create({
  container: {
    flex: 1,
    // padding: 24,
    // backgroundColor: Colors.lightgrey,
  },
  content: {
    flex: 1,
    padding: 16,
    gap: 16,
    overflow: 'scroll',
    // backgroundColor: Colors.lightgrey,
  },
  title: {
    marginTop: 16,
    paddingVertical: 8,
    borderWidth: 4,
    borderColor: '#20232a',
    borderRadius: 6,
    backgroundColor: '#61dafb',
    color: '#20232a',
    textAlign: 'center',
    fontSize: 30,
    fontWeight: 'bold',
  },
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  header: {
    height: 30,
    overflow: 'hidden',
  },
  headerImage: {
    color: basic.grey,
    bottom: -90,
    left: -35,
    position: 'absolute',
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },

  knobContainer: {
    position: 'absolute',
    left: 0,
    right: 0,
    height: 24,
    bottom: 0,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: 'transparent'// normally it is  appStyle.calendarBackground
  },
  knob: {
    width: 40,
    height: 4,
    borderRadius: 3,
    backgroundColor: 'transparent'    //normally it is e8ecf0
  },

  card: {
    borderRadius: 20,
    minWidth: '90%',
    height: 150,
    backgroundColor: props.backgroundColor,
  },
  cardTitle: {
    marginLeft: 15,
    marginTop: 10,
    marginBottom: 15,
    backgroundColor: 'transparent',
    color: props.color,
    fontWeight: 600,
  },

  noti: {
    borderRadius: 5,
    minWidth: '90%',
    height: 25,
    backgroundColor: Colors.vege.pupleYam,
    textAlign: 'center',
    color: 'white',
    justifyContent: 'center'
  },

  avartarList: {
    flexDirection: 'row',
    backgroundColor: 'transparent',
    paddingLeft: 10,
    paddingRight: 10,
    overflow: 'scroll',
    overflow: 'auto',
    whiteSpace: 'nowrap',
  },
  avartar: {
    width: 70,
    height: 70,
    borderRadius: 50,
    backgroundColor: Colors.thumbnail,
    alignItems: 'center',
    justifyContent: 'center',
    margin: 4,
  },
  avartarLabel: {
    textAlign: 'center',
  },
  avartarImage: {
    width: '100%',
    height: '100%',
    borderRadius: 50,
  },

  todoList: {
    flexDirection: 'column',
    backgroundColor: 'transparent',
    paddingLeft: 10,
    paddingRight: 10,
  },

  thumbnailList: {
    flexDirection: 'row',
    backgroundColor: 'transparent',
    paddingTop: 10,
    overflow: 'scroll',
    overflow: 'auto',
    whiteSpace: 'nowrap',
  },
  thumbnail: {
    width: 80,
    height: 80,
    borderRadius: 20,
    backgroundColor: Colors.thumbnail,
    alignItems: 'center',
    justifyContent: 'center',
  },
  thumbnailImage: {
    width: '100%',
    height: '100%',
    borderRadius: 20,
  },

});

export const textEllipsis =  {
  backgroundColor: 'transparent',
  color: Colors.light.text,
  overflow: 'hidden',
  'white-space': 'nowrap',
  'text-overflow': 'ellipsis',
  'word-break': 'break-all',
  // numberOfLines: 1,
  // ellipsizeMode: 'tail',
}
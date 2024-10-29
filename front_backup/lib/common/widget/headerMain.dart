import 'package:flutter/material.dart';
import 'package:soon_front/common/common.dart';

// Widget headerMain () {
//   return (

//   );
// }

Widget headerOther (headerTitle) {
  return (
    AppBar(
      backgroundColor: transparency,
      title: Text(headerTitle),
      elevation: 0,
      centerTitle: false,
      /** leading => 타이틀 텍스트 왼쪽 정렬(주로 햄버거 버튼) */
      leading: const IconButton(onPressed: null, icon: Icon(Icons.menu)),
      /** actions => 타이틀 텍스트 오른쪽 정렬(위젯 배열 사용 가능) */
      actions: const [
        IconButton(onPressed: null, icon: Icon(
          Icons.notifications,
            // Icons.notifications_active,
            color: warn,
            size: 30,
          ),
        ),
        IconButton(onPressed: null, icon: Icon(
          Icons.search,
            color: warn,
            size: 30,
          ),
        )
      ],)
  );
}